import boto3
import settings
import calendar
from datetime import datetime
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from html_template import HTMLTemplate
from mails_data import EMAIL_DATA, SUMMARY


def format_summary(data):
    data['months'] = {
        calendar.month_name[int(month_num)]: value
        for month_num, value in data['months'].items()
    }


def send_message(email_type, template_data=None):
    try:
        client = boto3.client("ses", region_name=settings.AWS_S3_REGION_NAME)
        template_data = template_data or {}
        email = EMAIL_DATA.get(email_type, None)
        if not email or not template_data:
            raise AssertionError()
        if email_type == SUMMARY:
            format_summary(template_data["summary"])
        print(template_data)
        jinja_client = HTMLTemplate(email["template"])
        body = jinja_client.render(template_data)
        print(body)
        recipients = template_data["recipients"]
        message = MIMEMultipart()
        subject = email["subject"]
        text_body = MIMEBase("text", "html")
        text_body.set_payload(body)
        message.attach(text_body)
        subject = email["subject"]
        message["Subject"] = subject
        message["From"] = "no-reply@stori.com"
        message["To"] = ",".join(recipients)
        client.send_raw_email(
            Source=settings.DEFAULT_SENDER,
            Destinations=recipients,
            RawMessage={"Data": message.as_string()},
        )
    except Exception as error:
        # handle error
        print(error, "*"*100)
