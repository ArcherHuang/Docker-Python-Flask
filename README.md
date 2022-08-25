# Docker Python Flask

## Flow
![](./Images/flow.png)

## Login
```
ssh ACCOUNT@IP
```

## Install Docker Engine
```
scp ./Script/install-docker.sh ACCOUNT@IP:/home/ACCOUNT

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
sudo docker prune -a
```