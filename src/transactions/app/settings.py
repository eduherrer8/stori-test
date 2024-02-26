import os
from decimal import Decimal

ENVIRONMENT = os.getenv("ENVIRONMENT")

DYNAMODB_URL = os.getenv("DYNAMODB_URL")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

FILE_PATH = "txns.csv"

DEFAULT_ENV = "local"

CENT = Decimal("0.01")
