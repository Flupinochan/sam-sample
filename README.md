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
