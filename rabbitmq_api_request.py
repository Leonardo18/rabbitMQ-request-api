#!/usr/local/bin/python


from flask import Flask
import crython
import requests
import json
import re


app = Flask(__name__)


@crython.job(second='10')
def run():
    host = '{RABBITMQ_HOST_URL} EX: localhost:5672'
    vhost = '{VHOST} EX: %2f'
    queue_name = '{QUEUE_NAME} EX: My.First.Queue'
    user = '{USER} EX: admin'
    password = '{PASSWORD} EX. admin'

    # In that case, always is invoking rabbit to return information about some queue. 
    # Rabbit have any other methods in your API, that can be invoked, just changing url in call_rabbitmq_api_get_queue_infos or doing some other new method
    res = call_rabbitmq_api_get_queue_infos(host, vhost, queue_name, user, password)
    print ("json returned")
    print (json.dumps(res.json(), indent=4))
    
    
    print ("get queue count messages")
    q_messages_count = get_queue_count_messages(res.json())
    print (q_messages_count)


crython.start()


@app.route("/health")
def health():
    return "OK"


def call_rabbitmq_api_get_queue_infos(host, vhost, queue_name, user, password):
  url = 'http://%s/api/queues/%s/%s' % (host, vhost, queue_name)
  rabbitmq_queue_infos = requests.get(url, auth=(user, password))
  return rabbitmq_queue_infos


def get_queue_count_messages(json_value):
  # Here can pass some key of json to get value, in this case, we are getting the count of messages in the queue
  messages_count = json_value["messages"]
  return messages_count
