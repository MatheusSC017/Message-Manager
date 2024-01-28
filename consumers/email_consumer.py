from consumer import consumer, email_callback

consumer('e-mail', 'email_queue', email_callback)
