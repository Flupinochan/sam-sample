## 参考サイト

- [samconfig1](https://github.com/aws/aws-sam-cli/blob/develop/docs/sam-config-docs.md)
- [samconfig2](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html)
- [samconfig3](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/using-sam-cli-configure.html)
- [pseudo parameters](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html)
- [Globals Section](https://github.com/aws/serverless-application-model/blob/develop/docs/globals.rst)
- [Template Format](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/template-formats.html)
- [Parameters](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html)
- [SAM Policy](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-policy-template-list.html)
- [CI/CD](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-generating-example-ci-cd-others.html)


## SAM CLI

```bash
# init project
sam init

# deploy cicd
sam pipeline init
sam pipeline bootstrap

# validate/build/deploy
sam validate --config-file samconfig/samconfig-dev.toml --template-file template.yaml
sam build --config-file samconfig/samconfig-dev.toml --template-file template.yaml
sam sync --watch --config-file samconfig/samconfig-dev.toml --template-file template.yaml
sam deploy --config-file samconfig/samconfig-dev.toml --template-file template.yaml
sam delete --config-file samconfig/samconfig-dev.toml
```
