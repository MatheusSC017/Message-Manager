# Message-Manager

This project aims to create a messaging system to manage messages sent via email and WhatsApp, working on them in an asynchronous and scalable way. It also has the functionality to save logs and send personalized messages for each type of subject.

**Note**: The project was based on the premise of being used in another project on my GitHub, this being a vehicle API, so the messages and subjects are configured as such.

## [Video about the project in PT-BR](https://share.vidyard.com/watch/YzRf1mSsK6e97Ddvq7iPs1?)

## Structure
### Consumers
This folder contains the files to start consumer queues for email and Whatsapp

### dags
This is the Dag file used to create a scheduled function using Airflow to supply the queues by calling an API

### testapi
Testing API to test the use of the DAG

### producer
File to test consumers if you don't want to use the DAG, you can send messages directly from this file and check the consumers' operation without initializing the DAGs or TestApi

## Installation
1. Clone the repository on your device
2. Go to the project directory
3. Create a virtual environment on your device
> python -m venv venv 

4. Run the virtual environment, if you are using the Windows operating system, use the following command
> venv/Scripts/activate

But if you use Linux OS or MAC use the command below
> source venv/Scripts/activate

5. Install the libraries saved in the requirements.txt file, if you are using the PIP package manager you can use the following command
> pip install -r requirements.txt

6. Create the .env file with the next parameters, regarding the email password, read [Google's documentation](https://support.google.com/mail/answer/185833?hl=en) on how to create an application password.
```
PORT=465
PASSWORD=insert_the_password_app
EMAIL=insert_your_email@email.com
```

7. Run as many instances as you want of the WhatsApp email consumer
> python consumers/email_consumer.py
> python consumers/whatsapp_consumer.py
