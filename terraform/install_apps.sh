#!/bin/bash

# Install nginx
sudo dnf install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# Install docker
sudo dnf install -y docker
sudo systemctl start docker
sudo systemctl enable docker

# Fix docker permissions
sudo chmod 666 /var/run/docker.sock

# Install docker compose plugin manually (not in AL2023 default repos)
DOCKER_CONFIG=${DOCKER_CONFIG:-/usr/local/lib/docker}
sudo mkdir -p $DOCKER_CONFIG/cli-plugins
sudo curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
  -o $DOCKER_CONFIG/cli-plugins/docker-compose
sudo chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose

# Verify
docker --version
docker compose version