import pika
import json


def send_message(message, queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    connection.close()


if __name__ == '__main__':
    print("Sending messages")
    email_message = {"recipient": "matheussimao2101@gmail.com", "content": "Hello via Email!"}
    whatsapp_message = {"recipient": "+55 19 99645-4087", "content": "Hello via WhatsApp!"}

    send_message(email_message, 'email_queue')
    # send_message(whatsapp_message, 'whatsapp_queue')
