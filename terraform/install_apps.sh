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

# Install docker-compose (plugin method - recommended)
sudo dnf install -y docker-compose-plugin

# Verify
docker --version
docker compose version