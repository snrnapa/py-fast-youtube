# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## getting start

### Eslintの設定

```
yarn add eslint --dev
.eslintrc.jsonの作成
yarn create @eslint/config
yarn add --dev eslint-config-airbnb-typescript
```

### Prettierのインストール

```

yarn add --dev prettier
yarn --dev add eslint-config-prettier
.prettierrc.json ファイルの作成（手動）
```

```json:.prettierrc.json
.prettierrc.json

{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2,
  "useTabs": false
}
```

- .vscode/settings.json ファイルの作成（手動）

```json:settings.json
{
"editor.defaultFormatter": "esbenp.prettier-vscode",
"editor.formatOnSave": true,
"editor.codeActionsOnSave": {
  "source.fixAll.eslint": true
}
}
```

### material ui

```
yarn add @mui/material @emotion/react @emotion/styled
yarn add @mui/icons-material
```

### セッティング

sudo cat /etc/nginx/sites-available/default
sudo vi /etc/nginx/sites-available/default

location /ydl {
proxy_pass http://localhost:5173;
}

sudo service nginx reload

sudo ufw status

sudo ufw allow 5173/tcp
sudo ufw reload
sudo ufw status
