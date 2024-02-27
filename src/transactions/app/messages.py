import requests

from settings import EMAIL_SERVER


def send_email(summary):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "insomnia/2023.5.8"
    }
    email_info = {
        "template": "Summary",
        "info": {
            "recipients": ["some@stori.com", "some1@stori.com"],
            "summary": summary
        }
    }
    requests.request("POST", EMAIL_SERVER, json=email_info, headers=headers)
