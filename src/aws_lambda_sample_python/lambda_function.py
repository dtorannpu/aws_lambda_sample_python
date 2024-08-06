from http import HTTPStatus

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.validation import validator

from aws_lambda_sample_python import schemas

logger = Logger()


@logger.inject_lambda_context
@validator(inbound_schema=schemas.INPUT)
def handler(event: dict, context: LambdaContext) -> dict:
    logger.info("test")
    logger.info("hoge")
    return {
        "statusCode": HTTPStatus.OK,
        "body": "hello world",
    }
