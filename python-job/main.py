import base64
import os
import sys
import time
from azure.storage.queue import ( QueueService )
from datetime import datetime, timedelta

from dotenv import load_dotenv
load_dotenv()

def get_env_variable(env_name):
    return str(os.getenv(env_name))

# Azure Storage Queue connection details
STORAGE_ACCOUNT_NAME = get_env_variable("STORAGE_ACCOUNT_NAME")
STORAGE_ACCOUNT_KEY = get_env_variable("STORAGE_ACCOUNT_KEY")
QUEUE_NAME = get_env_variable("QUEUE_NAME")

# Python job to be executed
def run_python_job(messages, queue_service):
    for message in messages:
        # Decode the Base64-encoded message content to string
        decoded_message = base64.b64decode(message.content).decode('utf-8')            
            
        # Process and display the message
        print("Received message:", decoded_message)

        # Optionally, you can delete the message from the queue after processing
        queue_service.delete_message(QUEUE_NAME, message.id, message.pop_receipt)
    # Your Python job code goes here
    print("Python job executed successfully!")

def check_queue_and_run_job():
    queue_service = QueueService(account_key=STORAGE_ACCOUNT_KEY, account_name=STORAGE_ACCOUNT_NAME)
    
    # Create the queue
    if not queue_service.exists(QUEUE_NAME):
        queue_service.create_queue(QUEUE_NAME)

    # Check if there are any messages in the queue
    messages = queue_service.get_messages(queue_name=QUEUE_NAME)
    if messages:
        # Run the Python job
        run_python_job(messages, queue_service)        


def main():
    try:
        # Consume and display messages initially
        check_queue_and_run_job()

        next_check = datetime.now() + timedelta(minutes=5)
        print(f"Scheduling next queue check at {next_check}")
        # Run the loop every 5 minutes
        while True:
            time.sleep(300)  # 300 seconds = 5 minutes
            check_queue_and_run_job()
    except KeyboardInterrupt:
        print("\nStopping the job...")
        sys.exit(0)    

if __name__ == "__main__":
    main()