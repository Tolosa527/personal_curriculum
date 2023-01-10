import smtplib
from email.message import EmailMessage
from config import get_config_variable

GMAIL_API_KEY = get_config_variable("gmail_api_key")
GMAIL_NAME = get_config_variable("gmail_name")

def send_email(*args, **kwargs):
    email   = kwargs['email']
    name    = kwargs['name']
    message = kwargs['message']
    subject = kwargs['subject']

    msg = EmailMessage()

    msg.set_content(message)

    msg['Subject'] = subject
    msg['From']    = email
    msg['To']      = GMAIL_NAME

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(GMAIL_NAME, GMAIL_API_KEY)
        server.send_message(msg)
        server.quit()
        return
    except Exception as e:
        print("[fatal-error] - {}".format(e))
        raise(e)