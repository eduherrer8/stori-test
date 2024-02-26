
import boto3
import settings


def _get_ddb_connection():
    dynamodb_client = None
    if settings.ENVIRONMENT == settings.DEFAULT_ENV:
        dynamodb_client = boto3.resource(
            "dynamodb",
            endpoint_url=settings.DYNAMODB_URL
        )
    else:
        dynamodb_client = boto3.resource("dynamodb")
    return dynamodb_client


def save_request(
        transaction_id,
        file_date,
        data,
) -> None:
    dynamo_db = _get_ddb_connection()
    try:
        table = dynamo_db.Table("Transactions")
        table.put_item(
            Item={
                "transactionID": transaction_id,
                "fileDate": file_date,
                **data
            }
        )
    except Exception as e:
        # handle error
        print(e, "/"*100)
