from dataclasses import dataclass
from http import HTTPStatus

import pytest

from aws_lambda_sample_python.lambda_function import handler


@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = (
            "arn:aws:lambda:ap-northeast-1:000000000:function:test"
        )
        aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"

    return LambdaContext()


def test_lambda_handler(lambda_context):
    event = {
        "user_id": "111",
        "project": "test",
        "ip": "192.168.0.1",
    }

    response = handler(event, lambda_context)

    assert response["statusCode"] == HTTPStatus.OK
    assert response["body"] == "hello world"


def test_lambda_handler_validate_error(lambda_context):
    event = {"user_id": "111", "project": "test"}

    response = handler(event, lambda_context)

    assert response["statusCode"] == HTTPStatus.BAD_REQUEST
