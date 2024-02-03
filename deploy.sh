#!/bin/bash
pm2 delete "ydl-back"
git checkout master
git pull
pm2 start "python3 -m uvicorn main:app --reload" --name "ydl-back"