import pytest
from dataclasses import dataclass
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
    event = {}

    response = handler(event, lambda_context)

    assert response["statusCode"] == 200
    assert response["body"] == "hello world"
