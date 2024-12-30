# 環境構築

本プロジェクトは、下記２つを vscode の拡張機能の dev containers より、dokcer image を作成市、開発を行います。

- python
- react

ctrl + shift + P の dev container のコンテナ作成より、環境を作成できます。

# デプロイ

deploy.sh に処理をまとめています。

## Getting Start

```python
python3 main.py
```

## pip check

```
pip freeze
```

## ソフト化

```
pyinstaller --onefile main.py
```
