# learn-modern-python-dev

## pipとの違い

- インストール速度が速い
- 依存関係の文書化が容易
  - uvは`pyproject.toml`を確認する
  - pipは`pip freeze > requirements.txt`などで依存関係を書き出す

## コードの品質管理
ruff, mypy

## 初期化

```bash
uv init
```


## 仮想環境の構築済みでライブラリインストール

```bash
uv add <ライブラリ名>
```

```bash
uv add --dev <ライブラリ名>
```

## ファイル実行実行
```bash
uv run xxx.py
```

## uvが作成した実行環境でwhichする

```bash
uv run which python
```

## uvを同期

```bash
uv sync
```

## Pythonのバージョンを管理

```bash
uv python list
```

```bash
uv python install 3.12.10
```


## Ruff

RuffはAstralが提供するリンタ・フォーマッタ

### インストール
```bash
uv add --dev ruff
```

### 検証’

```bash
uv run ruff check main.py
```

### --fixを指定することで、エラーを修正する

- 消せる修正はするが、消せないエラーもある。

```bash
uv run ruff check --fix main.py
```

