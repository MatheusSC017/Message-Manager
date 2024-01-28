import pywhatkit as pwk
import smtplib, ssl
import os
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()


def send_email(recipient, message):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", os.getenv("PORT"), context=context) as server:
        server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        server.sendmail(os.getenv("EMAIL"), recipient, message)


def send_whatsapp_message(recipient, message):
    try:
        now = datetime.now()
        pwk.sendwhatmsg(recipient, message, now.hour, now.minute + 1)
        print("Message Sent!")
    except:
        print("Error in sending the message")
