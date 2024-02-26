import json

import requests

from messages import send_message


def lambda_handler(event, context):
    response = {
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({}),
        "statusCode": requests.codes.ok,
    }
    try:
        data = json.loads(event["body"])
        send_message(data["template"], data["info"])
        response["statusCode"] = requests.codes.ok
    except Exception as error:
        response["statusCode"] = requests.codes.internal_server_error
        response["body"] = json.dumps(
            {
                "errorMessage": f"Unexpected error {error}",
            }
        )
    return response
