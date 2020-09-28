#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python3 python-dev python3-pip ffmpeg supervisor nginx mysql-server
pip install --user --upgrade virtualenv
sudo rm -rf /var/www/backend