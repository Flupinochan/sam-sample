"""_summary_"""

import os

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging.formatter import LambdaPowertoolsFormatter
from aws_lambda_powertools.utilities.parser import event_parser
from aws_lambda_powertools.utilities.typing import LambdaContext
from pydantic import BaseModel

# ロガー、トレーサー初期化
formatter = LambdaPowertoolsFormatter(
    log_record_order=["level", "message", "timestamp", "location"],
)
logger = Logger(logger_formatter=formatter)
tracer = Tracer()

# 環境変数取得
try:
    POWERTOOLS_METRICS_NAMESPACE: str = os.environ["POWERTOOLS_METRICS_NAMESPACE"]
except KeyError:
    logger.exception("環境変数の取得に失敗しました")
    raise


class LambdaEvent(BaseModel):
    """Lambdaイベント引数定義"""

    message: str


@tracer.capture_method
def main(message: str) -> None:
    """メイン処理"""
    logger.info(message)


@event_parser(model=LambdaEvent)
@logger.inject_lambda_context()
@tracer.capture_lambda_handler
def lambda_handler(event: LambdaEvent, _context: LambdaContext) -> dict:
    """エントリーポイント"""
    logger.info("Lambda実行開始")

    try:
        main(event.message)
        logger.info("Lambda実行終了")
    except Exception:
        logger.exception("Lambda実行エラー")
        raise

    return {"message": "Hello from Function!"}
