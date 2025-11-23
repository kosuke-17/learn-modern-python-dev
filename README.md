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

- カスタマイズするにはこのサイトを参照
  - https://docs.astral.sh/ruff/tutorial/#configuration

### vscodeでリンタ・フォーマッタを動かす

- vscodeの拡張機能である「Ruff」を入れると可視化してくれる
- Cursorのグローバル設定でリンターを設定する
  - path :`~/Library/Application Support/Cursor/User/settings.json`


```json
{
    "[python]": { // Python用設定
        "editor.formatOnSave": true, // ファイル保存時に自動でフォーマットする

        "editor.codeActionsOnSave": { // ファイル保存時に
            "source.fixAll": "explicit", // 問題を修正
            "source.organizeImports": "explicit" // import文を整理
        },
        // PythonフォーマッターとしてRuffを使用
        "editor.defaultFormatter": "charliermarsh.ruff" 
    },
}
```

- [参考](https://note.com/yunichee/n/nda29a9ecfe42)

### インストール
```bash
uv add --dev ruff
```

### 検証

```bash
uv run ruff check main.py
```

### --fixを指定することで、エラーを修正する

- 消せる修正はするが、消せないエラーもある。

```bash
uv run ruff check --fix main.py
```



### フォーマット

```bash
uv run ruff format main.py
```

- ドットの場合はファイル内の全体をフォーマットする

```bash
uv run ruff format .
```

## mypy: 静的型検査

- pythonは動的型付け言語
- プログラム中に型の整合性チェックを行う言語は静的型付け言語という
- mypyはPythonで静的型付け言語風の型検査を行うツール
  - 型ヒントを読み取る

```bash
uv add --dev mypy
```

```bash
uv run mypy src/type_hint.py
```

- すべてのpyファイルを検査

```bash
uv run mypy .
```

### vscodeでpythonの型チェックをする

- vscodeの拡張機能である「Mypy Type Checker」を入れると可視化してくれる

## poethepoet(poe:ポウと言われることが多い): uv向きのタスクランナー

- 毎回呼ぶのはめんどくさい

```bash
uv run ruff format .
uv run ruff check --fix .
uv run mypy .
```

### インストール

```bash
uv add --dev poethepoet
```

### 定義

`pyproject.toml`に以下を記載
```toml
[tool.poe.tasks]
format = "uv run ruff format ."
lint = "uv run ruff check ."
type-check = "uv run mypy ."

check = ["format", "lint", "type-check"]
```

- 実行結果

```terminal
Poe => uv run ruff format .
3 files left unchanged
Poe => uv run ruff check .
All checks passed!
Poe => uv run mypy .
Success: no issues found in 3 source files
```

## pre-commitのライブラリを用いて.gitのpre-commit時にアクションする

```bash
uv add --dev pre-commit
```

`.pre-commt-config.yaml`の作成

```bash
# 実行すると.git/hooks/pre-commitが自動生成される
uv run pre-commit install
```


- 余談
  - 以下のcursor設定をすると末尾を意識しなくて良い

```
Files: Insert Final Newline
有効にすると、ファイルの保存時に改行を末尾に挿入します。
```

```
ユーザー > ファイル > Excludeに.gitが非表示となる設定が自動でされている。
そのため、「**/.git」の選択を削除する
```
