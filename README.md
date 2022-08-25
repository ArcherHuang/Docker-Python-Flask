# Docker Python Flask

## Contents
- [Flow](#flow)
- [VM Login](#login)
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

## Login
* On local
  ```
  ssh ACCOUNT@IP
  ```

## Install Docker Engine
* On local
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
```
scp flask-sample/* ACCOUNT@IP:/home/ACCOUNT/flask-sample
```

## Build Docker Image
```
sudo docker build -t mmosconii/docker-python:0.1 .
```

## List Docker Image
```
sudo docker images
```

## Create Folder
```
cd ~
mkdir dataset-out
mkdir model-out

echo "hello" > ~/dataset-out/1.txt
echo "world" > ~/model-out/2.txt
```

## Add VM Port
* Login Azure Portal from Browser > Click `Networking` > Click `Add inbound security rule` > Click `Destination port ranges` > Input `80` > Click `Add`

## Run Docker Image
```
sudo docker run -d -p 80:80 --name=test-dev -v /home/ACCOUNT/dataset-out:/dataset -v /home/ACCOUNT/model-out:/model mmosconii/docker-python:0.1
```

# Check Docker Container
```
sudo docker ps -a
```

# Docker Container Log
```
sudo docker logs -f test-dev
```

# Into the Container
```
sudo docker exec -it test-dev bash
```

# Stop Container
```
sudo docker ps -a
sudo docker stop CONTAINER-ID
```

# Remove Container
```
sudo docker ps -a
sudo docker rm CONTAINER-ID
```

# Remove Docker Image
```
sudo docker image prune -a
```

## Contributor
* [Huang, Cheng-Chuan](https://github.com/ArcherHuang)

## License
This sample is licensed under the [MIT](./LICENSE) license.
