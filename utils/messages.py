import pywhatkit as pwk
import smtplib, ssl
import os
from jinja2 import Environment, FileSystemLoader
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

# Load the Jinja environment
template_env = Environment(loader=FileSystemLoader(searchpath="../templates"))


def send_email(recipient, client, date, vehicle, branch, subject):
    context = ssl.create_default_context()
    email_template = template_env.get_template("email/appointment.html")
    email_content = email_template.render(subject=subject.title(), client=client, date=date, vehicle=vehicle, branch=branch)

    # Create the email message
    msg = MIMEText(email_content, 'html')
    msg['Subject'] = f"{subject.title()} of {vehicle}"
    msg['From'] = os.getenv("EMAIL")
    msg['To'] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", os.getenv("PORT"), context=context) as server:
        server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        server.sendmail(os.getenv("EMAIL"), recipient, msg.as_string())


def send_whatsapp_message(recipient, message):
    try:
        now = datetime.now()
        pwk.sendwhatmsg(recipient, message, now.hour, now.minute + 1)
        print("Message Sent!")
    except:
        print("Error in sending the message")
