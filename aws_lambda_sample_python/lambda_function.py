from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


@logger.inject_lambda_context
def handler(event: dict, context: LambdaContext) -> dict:
    logger.info("test");
    logger.info("hoge");
    return {
        "statusCode": 200,
        "body": "hello world",
    }
