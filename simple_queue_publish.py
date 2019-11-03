# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:44:04 2019

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

channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='Paolo!')

print("[X] Hello '")