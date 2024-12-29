#!/bin/bash

# React ビルド
echo "Building React app..."
cd view || exit
npm run build || exit
cd ..

# FastAPI ディレクトリにコピー
echo "Copying build files to FastAPI static directory..."
mkdir -p api/static
cp -r view/dist/* api/static/

echo "Build and copy completed!"

# 仮想環境を作成し、必要なパッケージをインストール
cd api
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt

# pyinstallerでビルド
echo "Building executable with pyinstaller..."
pyinstaller --onefile --add-data "static:static" main.py
mkdir -p dist/static
cp -r ./static/* ./dist/static



echo "Deployment completed!"
cd ..
