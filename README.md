# How To Build and Deploy a Flask Application Using Docker on Ubuntu

## Contents
- [Files](#files)
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
- [Check API from Browser](#check-api-from-browser)
- [Docker Container Log](#docker-container-log)
- [Into the Container](#into-the-container)
- [Use Postman to Check API](#use-postman-to-check-api)
- [Copy a file from Container to VM](#copy-a-file-from-container-to-vm)
- [Copy a file from VM to Container](#copy-a-file-from-vm-to-container)
- [Stop Container](#stop-container)
- [Remove Container](#remove-container)
- [Remove Docker Image](#remove-docker-image)
- [Contributor](#contributor)
- [License](#license)

## Files
| No |  Folder   |   Comment    |
|:----:|:-------------:|:---:|
|  1 |      [Script](https://github.com/ArcherHuang/Docker-Python-Flask/tree/main/Script)      | Install Docker package using this script |
|  2 | [flask-sample](https://github.com/ArcherHuang/Docker-Python-Flask/tree/main/flask-sample) | Build an web app by using Python and Flask |

## Flow
![](./Images/Docker-flow.png)
![](./Images/flow.png)

## Logging in to VM
* On Local
  ```
  ssh VM-ACCOUNT@VM-IP
  ```

## Install Docker Engine
* On Local
  ```
  Download https://github.com/ArcherHuang/Docker-Python-Flask Repository
  
  cd to Docker-Python-Flask Repository
  
  scp ./Script/install-docker.sh VM-ACCOUNT@VM-IP:~
  ```
* On VM
  ```
  cd ~
  
  chmod 777 install-docker.sh

  sudo ./install-docker.sh
  ```

## Upload flask-sample to VM
* On VM
  ```
  mkdir ~/flask-sample
  ```
* On Local
  ```
  scp flask-sample/* VM-ACCOUNT@VM-IP:~/flask-sample
  ```

## Build Docker Image
* On VM
  ```
  cd ~/flask-sample

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
  mkdir ~/dataset-out ~/model-out

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
  sudo docker run -d -p 80:80 --name=test-dev -v ~/dataset-out:/dataset -v ~/model-out:/model mmosconii/docker-python:0.1
  ```

## Check Docker Container
* On VM
  ```
  sudo docker ps -a
  ```

## Check API from Browser
* On Local
  * http://VM-IP
  ![](./Images/check-api.png)

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

## Use [Postman](https://www.postman.com/) to Check API
* GET API
  * GET http://VM-IP
  ![](./Images/Postman-GET-API.png)
* POST API
  * POST http://VM-IP/store
  * Body
    ```
    {
      "run": 6611
    }
    ```
  ![](./Images/Postman-POST-API.png)
  * Check if the `/model/data.json` file is exist on Container
    ![](./Images/Postman-POST-API-Detail.png)

## Copy a file from Container to VM
* On VM
```
echo "Lucky seven" > ~/filename.txt

sudo docker ps -a

sudo docker cp CONTAINER-ID:/app/filename.txt ~/777.txt
```

## Copy a file from VM to Container
```
sudo docker ps -a

sudo docker cp ~/filename.txt CONTAINER-ID:/app/filename.txt 
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
