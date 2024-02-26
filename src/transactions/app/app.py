from collections import defaultdict
from datetime import datetime
from decimal import Decimal
import json
import csv

import requests
from db import save_request
import settings
from messages import send_email
from decimal import ROUND_HALF_UP


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)


def read_file():
    transactions = []
    with open(settings.FILE_PATH, 'r') as csvfile:
        next(csvfile)
        reader = csv.DictReader(
            csvfile,
            fieldnames=[
                "transaction_id",
                "operation_date",
                "transaction_amount"
            ],
        )
        for row in reader:
            transactions.append(row)
    return transactions


def save_transactions(transactions):
    file_date = str(datetime.now().date())
    for transaction in transactions:
        save_request(
            transaction["transaction_id"],
            file_date,
            {
                "operation_date": transaction["operation_date"],
                "transaction_amount": transaction["transaction_amount"]
            }
        )


def get_transactions_summary(transactions):
    total_debit = 0
    total_credit = 0
    total_amout = Decimal("0.00")
    transactions_by_month = defaultdict(int)
    for transaction in transactions:
        amount = Decimal(transaction["transaction_amount"])
        month = transaction["operation_date"].split("/")[0]
        if amount <= Decimal("0.00"):
            total_debit += 1
        else:
            total_credit += 1
        total_amout = amount
        transactions_by_month[int(month)] += 1

    return {
        "total": total_amout.quantize(settings.CENT, ROUND_HALF_UP),
        "credit":
            (total_amout/total_credit).quantize(settings.CENT, ROUND_HALF_UP),
        "debit":
            (total_amout/total_debit).quantize(settings.CENT, ROUND_HALF_UP),
        "months": dict(sorted(transactions_by_month.items()))
    }


def lambda_handler(event, context):
    response = {
        "statusCode": requests.codes.ok,
        "headers": {"Content-Type": "application/json"},
    }
    try:
        transactions = read_file()
        save_transactions(transactions)
        summary = get_transactions_summary(transactions)
        send_email(summary)
    except Exception as error:
        # handle error
        response["statusCode"] = requests.codes.internal_server_error
        response["body"] = json.dumps({"error": str(error)})
    else:
        response["body"] = json.dumps(
            {"data": transactions, "summary": summary},
            cls=DecimalEncoder
        )
    return response
