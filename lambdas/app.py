def lambda_handler(event, context):

    if "language" not in event:
        raise Exception("Language not provided")

    if "code" not in event:
        raise Exception("Code not provided")

    if not event["code"].strip():
        raise Exception("Empty code")

    return {
        "language": event["language"],
        "code": event["code"]
    }