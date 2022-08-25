# Docker Python Flask

## Contents
- [Flow](#flow)
- [Logging in to VM](#logging-in-to-vm)
- [Install Docker Engine](#install-docker-engine)
- [Upload flask-sample to VM](#upload-flask-sample-to-vm)
- [Build Docker Image](#build-docker-image)
- [List Docker Image](#list-docker-image)
- [Create Folders and Add files](#create-folder)
- [Add VM Port](#add-vm-port)
- [Run Docker Image](#run-docker-image)
- [Check Docker Container](#check-docker-container)
- [Docker Container Log](#docker-container-log)
- [Into the Container](#into-the-container)
- [Stop Container](#stop-container)
- [Remove Container](#remove-container)
- [Remove Docker Image](#remove-docker-image)
- [Contributor](#contributor)
- [License](#license)

## Flow
![](./Images/flow.png)

## Logging in to VM
* On Local
  ```
  ssh ACCOUNT@IP
  ```

## Install Docker Engine
* On Local
  ```
  scp ./Script/install-docker.sh ACCOUNT@IP:/home/ACCOUNT
  ```
* On VM
  ```
  cd ~
  
  chmod 777 install-docker.sh

  sudo ./install-docker.sh
  ```

## Upload flask-sample to VM
* On Local
  ```
  scp flask-sample/* ACCOUNT@IP:/home/ACCOUNT/flask-sample
  ```

## Build Docker Image
* On VM
  ```
  sudo docker build -t mmosconii/docker-python:0.1 .
  ```

## List Docker Image
* On VM
  ```
  sudo docker images
  ```

## Create Folder
* On VM
  ```
  cd ~

  mkdir dataset-out

  mkdir model-out

  echo "hello" > ~/dataset-out/1.txt

  echo "world" > ~/model-out/2.txt
  ```

## Add VM Port
* On Chrome
  * Login Azure Portal from Browser > Click `Networking` > Click `Add inbound security rule` > Click `Destination port ranges` > Input `80` > Click `Add`
  ![](./Images/Port1.png)
  ![](./Images/Port2.png)

## Run Docker Image
* On VM
  ```
  sudo docker run -d -p 80:80 --name=test-dev -v /home/ACCOUNT/dataset-out:/dataset -v /home/ACCOUNT/model-out:/model mmosconii/docker-python:0.1
  ```

## Check Docker Container
* On VM
  ```
  sudo docker ps -a
  ```

## Docker Container Log
* On VM
  ```
  sudo docker logs -f test-dev
  ```

## Into the Container
* On VM
  ```
  sudo docker exec -it test-dev bash
  ```

## Stop Container
* On VM
  ```
  sudo docker ps -a
  
  sudo docker stop CONTAINER-ID
  ```

## Remove Container
* On VM
  ```
  sudo docker ps -a
  
  sudo docker rm CONTAINER-ID
  ```

## Remove Docker Image
* On VM
  ```
  sudo docker image prune -a
  ```

## Contributor
* [Huang, Cheng-Chuan](https://github.com/ArcherHuang)

## License
This sample is licensed under the [MIT](./LICENSE) license.
