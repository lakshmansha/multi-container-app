# multi-container-app
Repo for Youtube Video to create Multiplie Container in One Web App in Azure.


1. To Push the Nginx Docker to ACR

    ```
    docker build -f ./Nginx/Dockerfile -t nginx:dev .
    docker tag nginx:dev multicontainerstrg.azurecr.io/nginx:dev
    docker push multicontainerstrg.azurecr.io/nginx:dev
    ```

2. To Push the Python-Job Docker to ACR

    ```
    docker build -f ./Dockerfile -t python-job:dev .
    docker tag python-job:dev multicontainerstrg.azurecr.io/python-job:dev
    docker push multicontainerstrg.azurecr.io/python-job:dev
    ```    

3. Up the Multi-Container in Docker Compose.

