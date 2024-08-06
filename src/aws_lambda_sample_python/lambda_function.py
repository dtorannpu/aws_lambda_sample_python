from http import HTTPStatus

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.validation import (SchemaValidationError,
                                                        validate)

from aws_lambda_sample_python import schemas

logger = Logger()


@logger.inject_lambda_context
def handler(event: dict, context: LambdaContext) -> dict:
    try:
        logger.info("test")
        logger.info("hoge")

        validate(event=event, schema=schemas.INPUT)

        return {
            "statusCode": HTTPStatus.OK,
            "body": "hello world",
        }
    except SchemaValidationError as exception:
        logger.exception(exception)
        return {"statusCode": HTTPStatus.BAD_REQUEST, "body": str(exception)}
