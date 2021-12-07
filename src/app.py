import sys

from aws_lambda_powertools import Tracer

tracer = Tracer()


@tracer.capture_lambda_handler
def handler(event, context):
    return f"Hello from AWS Lambda using Python {sys.version}! - v1"
