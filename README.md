# multi-container-app
Repo for Youtube Video to create Multiplie Container in One Web App in Azure.


1. To Push the Nginx Docker to ACR

    ```
    docker build -f ./Dockerfile -t nginx:dev27042024 .
    docker tag nginx:dev27042024 multicontainerstrg.azurecr.io/nginx:dev27042024
    docker push multicontainerstrg.azurecr.io/nginx:dev27042024
    ```

2. To Push the Python-Job Docker to ACR

    ```
    docker build -f ./Dockerfile -t python-job:dev27042024 .
    docker tag python-job:dev27042024 multicontainerstrg.azurecr.io/python-job:dev27042024
    docker push multicontainerstrg.azurecr.io/python-job:dev27042024
    ```    

3. Up the Multi-Container in Docker Compose.

docker-compose --env-file ./.env up

