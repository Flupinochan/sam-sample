"""テスト: lambda_handler.py"""
# ruff: noqa: E402

from dotenv import load_dotenv

load_dotenv()
import importlib
import sys
from dataclasses import dataclass
from unittest.mock import patch

import pytest
from aws_lambda_powertools.utilities.typing import LambdaContext

from src.app import lambda_handler

TEST_EVENT = {"message": "hello world"}


@pytest.fixture
def lambda_context() -> LambdaContext:
    """LambdaContextのモック"""

    @dataclass
    class MockLambdaContext:
        function_name: str = "local_test_function"
        memory_limit_in_mb: int = 512
        invoked_function_arn: str = (
            "arn:aws:lambda:ap-northeast-1:12345678910:function:local_test_function"
        )
        aws_request_id: str = "12345678-2182-154f-163f-5f0f9a621d72"

    return MockLambdaContext()  # type: ignore[return-value]


def test_lambda_handler_success(
    lambda_context: LambdaContext,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """正常系"""
    lambda_handler(TEST_EVENT, lambda_context)
    # ログの確認
    assert "Lambda実行開始" in caplog.text
    assert "hello world" in caplog.text
    assert "Lambda実行終了" in caplog.text
    assert "Lambda実行エラー" not in caplog.text


def test_lambda_handler_failure(
    lambda_context: LambdaContext,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """異常系"""
    # main関数で例外を発生させるようにモック
    with patch("src.app.main") as mock_main:
        mock_main.side_effect = Exception("エラー発生")
        # 例外発生の確認
        with pytest.raises(Exception, match="エラー発生"):
            lambda_handler(TEST_EVENT, lambda_context)
        # ログの確認
        assert "Lambda実行開始" in caplog.text
        assert "hello world" not in caplog.text
        assert "Lambda実行終了" not in caplog.text
        assert "Lambda実行エラー" in caplog.text


def test_missing_environment_variable_raises_key_error(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """環境変数が存在しない場合にKeyErrorが発生すること"""
    # 環境変数を空にしてモジュールをリロード
    with patch.dict("os.environ", {}, clear=True):
        if "src.app" in sys.modules:
            with pytest.raises(KeyError):
                importlib.reload(sys.modules["src.app"])
        else:
            with pytest.raises(KeyError):
                pass
    assert "環境変数の取得に失敗しました" in caplog.text
