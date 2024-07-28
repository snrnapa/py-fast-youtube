#!/bin/bash
cd /home/napa/prod/ydl/py-fast-youtube
pm2 delete "ydl-back"
git checkout master
git pull
pm2 start "python3 main.py" --name "ydl-back"