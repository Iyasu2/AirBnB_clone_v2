#!/usr/bin/env bash
#update nginx configuration
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo 'Hello, World!' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/^server {/a \        location \/hbnb_static\/ {\n                alias \/data\/web_static\/current\/;\n        }' /etc/nginx/sites-available/default
sudo service nginx restart
