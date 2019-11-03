# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:40:20 2019

@author: Paolo
"""

import pika

import os
import pika


mode='_SEND' #set 'SEND' mode is you will to send rather than receive messages


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)



amqp_url='introduire son adresse'


# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='hello')


if mode == 'SEND':
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
                          
    print(" [x] Sent 'Hello World!'")
    
    connection.close()
else:
        
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,                          
                          auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()