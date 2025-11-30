## 参考サイト

- [samconfig1](https://github.com/aws/aws-sam-cli/blob/develop/docs/sam-config-docs.md)
- [samconfig2](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html)
- [samconfig3](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/using-sam-cli-configure.html)
- [疑似パラメータ](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html)
- [Globals Section](https://github.com/aws/serverless-application-model/blob/develop/docs/globals.rst)
- [Template Format](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/template-formats.html)
- [Parameters](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html)
- [SAM Policy](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-policy-template-list.html)
- [CI/CD](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-generating-example-ci-cd-others.html)


## SAM CLI

### プロジェクトの初期化

```bash
sam init
```

### CI/CD初期化

- 作成されたリソースはCloudFormationコンソール画面から削除
- devやprodごとにそれぞれ実行
- OIDCで特定のSaaSのリポジトリのブランチに対してのみ権限を付与するIAM Roleを作成すべき


```bash
# 1. pipeline設定ファイルの生成 (pipelineconfig.toml、github workflowを作成)
sam pipeline init
# 2. pipelineconfig.tomlに基づきCI/CD実行に必要なIAM Role等を作成
sam pipeline bootstrap
```

### CloudFormation Templateチェック

```bash
sam validate --lint --template template.yaml
```

### Build

```bash
sam sync --watch
```

### python version確認

```bash
# インストール済みのPythonバージョンを確認
py --list

# python3.12のcfn-lintをuninstall
py -3.12 -m pip uninstall cfn-lint

# 環境変数のPathをとおして再起動
```

### 開発環境セットアップ

```bash
# 仮想環境を作成
uv venv --python 3.13

# 仮想環境を有効化
## Linux
source .venv/bin/activate
## Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 外部ライブラリをインストール
uv pip install -r layer/requirements.txt
uv pip install -r tests/requirements.txt

# テスト実行
## htmlcov/index.htmlでカバレッジが確認可能
pytest --cov=src tests/ --cov-report=html
## VSCode拡張機能Coverage Guttersを利用する場合
pytest --cov=src tests/ --cov-report=xml
```

### プロジェクト初期化

```bash
# pyproject.tomlを作成
uv init
# 外部ライブラリ手動追加
uv add tenacity
uv add --dev pytest
# 外部ライブラリをpyproject.tomlに従ってインストール
# project.tomlからrequirements.txtを作成
uv sync
uv sync --no-dev # 本番依存のみ
uv pip compile pyproject.toml -o layer/requirements.txt # 本番のみ
```

### プロンプト

[starship](https://starship.rs/ja-JP/)

