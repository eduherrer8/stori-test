import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent
TEMPLATE_FILES_ROOT = os.path.join(BASE_DIR, "templates")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")

DEFAULT_SENDER = "no-reply@stori.com"
