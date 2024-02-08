import pika
import json


def send_message(message, queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    connection.close()


if __name__ == '__main__':
    """
    Below is the list of fields for requesting messages via email.
    
    appointment:
        ["recipient", "client", "date", "vehicle", "branch", "subject", ]
    devolution:
        ["recipient", "client", "start_date", "end_date", "vehicle", "branch", "subject", ]
    late devolution:
        ["recipient", "client", "start_date", "end_date", "vehicle", "subject", ]
        
    Below is the list of fields for requesting messages via Whatsapp.
    
    appointment:
        ["recipient", "client", "date", "vehicle", "subject", ]
    devolution:
        ["recipient", "client", "date", "vehicle", "subject", ]
    late devolution:
        ["recipient", "client", "vehicle", "subject", ]
    """
    print("Sending test messages")

    email_messages_json = open('email_messages.json')
    for email in json.load(email_messages_json):
        send_message(email, 'email_queue')

    whatsapp_messages_json = open('whatsapp_messages.json')
    for whatsapp in json.load(whatsapp_messages_json):
        send_message(whatsapp, 'whatsapp_queue')
