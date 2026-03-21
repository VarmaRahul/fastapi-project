#!/bin/bash

#install nginx
sudo yum install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx

#install docker
sudo apt-get update
sudo apt-get install -y docker.io
sudo chmod 666 /var/run/docker.sock
#sudo usermod -aG docker $USER
#newgrp docker
sudo systemctl enable docker
sudo systemctl start docker
docker --version

#install docker compose
sudo apt install -y docker-compose
docker-compose version


#sudo echo "<h1> This server is built from Terraform </h1>" | sudo tee /usr/share/nginx/html/index.html