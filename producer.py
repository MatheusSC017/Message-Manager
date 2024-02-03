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

    # email_message = {
    #     "recipient": "emaildeteste@gmail.com",
    #     "client": "Matheus",
    #     "date": "16/02/2024",
    #     "vehicle": "Ford K, 2003",
    #     "branch": "Parque Nacional da Tijuca, Alto da Boa Vista, Rio de Janeiro/RJ",
    #     "subject": "appointment"
    #     }
    # send_message(email_message, 'email_queue')
    #
    # email_message = {
    #     "recipient": "emaildeteste@gmail.com",
    #     "client": "Matheus",
    #     "start_date": "21/01/2024",
    #     "end_date": "04/02/2024",
    #     "vehicle": "Ford K, 2003",
    #     "branch": "Parque Nacional da Tijuca, Alto da Boa Vista, Rio de Janeiro/RJ",
    #     "subject": "devolution"
    #     }
    # send_message(email_message, 'email_queue')
    #
    # email_message = {
    #     "recipient": "emaildeteste@gmail.com",
    #     "client": "Matheus",
    #     "start_date": "21/01/2024",
    #     "end_date": "04/02/2024",
    #     "vehicle": "Ford K, 2003",
    #     "subject": "late devolution"
    #     }
    # send_message(email_message, 'email_queue')

    whatsapp_message = {
        "recipient": "+55 19 12345-6789",
        "client": "Matheus",
        "date": "21/01/2024",
        "vehicle": "Ford K, 2003",
        "subject": "appointment"
    }
    send_message(whatsapp_message, 'whatsapp_queue')
