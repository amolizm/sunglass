#!/bin/bash

sudo apt install brightnessctl
sudo chmod +s $(which brightnessctl)

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pyinstaller light.py --onefile
