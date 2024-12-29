# デプロイ
```
mkdir -p api/static
cp -r view/dist/* api/static/
```

# バックエンド
```python
python3 -m venv venv
source api/venv/bin/activate
pip3 install -r requirements.txt
```
## Getting Start

```python
python3 main.py
```

## pip check
```
pip freeze
```
## やめるとき
```
deactivate
```

## ソフト化
```
pyinstaller --onefile main.py
```


## 参考サイト
[ラムダでの実装](https://qiita.com/Shinkijigyo_no_Hitsuji/items/cedd1825e5437663d3ce)