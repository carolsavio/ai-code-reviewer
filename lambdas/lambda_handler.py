import json

def lambda_handler(event, context):

    if "code" not in event:

        raise Exception("Code not provided")

    if "language" not in event:

        raise Exception("Language not provided")

    return event