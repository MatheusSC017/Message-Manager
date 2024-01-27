import pywhatkit as pwk
from datetime import datetime


def send_email(recipient, message):
    pass


def send_whatsapp_message(recipient, message):
    try:
        now = datetime.now()
        pwk.sendwhatmsg(recipient, message, now.hour, now.minute + 1)
        print("Message Sent!")
    except:
        print("Error in sending the message")
