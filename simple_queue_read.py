# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:45:11 2019

@author: Paolo
"""

import os
import pika

amqp_url='introduire son adresse'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP


channel = connection.channel()
channel.queue_declare(queue='presentation')


def callback(ch,method,properties,body):
    print("[X] Received %r" % body)


channel.basic_consume(queue='presentation',
                      on_message_callback=callback,
                      auto_ack=True)
    
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()