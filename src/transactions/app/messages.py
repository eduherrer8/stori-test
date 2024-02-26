import requests


def send_email(summary):
    url = "http://host.docker.internal:3000/utils/mails"
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
    requests.request("POST", url, json=email_info, headers=headers)
