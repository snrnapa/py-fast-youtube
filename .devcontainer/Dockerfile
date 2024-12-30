# Pythonのベースイメージを使用
FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

# MinGW（Windows向けのクロスコンパイラ）をインストール
RUN apt-get update && \
    apt-get install -y gcc-mingw-w64-x86-64

# Node.js を 20.x にインストール
RUN curl -sL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# npm を最新バージョンにインストール
RUN npm install -g npm@latest

# 作業ディレクトリを指定
WORKDIR /workspace