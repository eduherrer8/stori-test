import os
from decimal import Decimal

ENVIRONMENT = os.getenv("ENVIRONMENT")

DYNAMODB_URL = os.getenv("DYNAMODB_URL")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

FILE_PATH = "txns.csv"

DEFAULT_ENV = "local"

CENT = Decimal("0.01")

EMAIL_SERVER = os.getenv(
    "EMAIL_SERVER", "http://host.docker.internal:3000/utils/mails")
