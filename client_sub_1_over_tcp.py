# client_sub_1_over_tcp.py
# subscribes to messages on MQTT broker
# uses a TCP connection between publisher and broker
"""
from paho library
https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#usage-and-api

some useful hints found in:
http://www.steves-internet-guide.com/mqtt-python-beginners-course/

"""

import paho.mqtt.client as mqtt
import time
from argparse import ArgumentParser

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("subscriber -> connecting to broker")
    print(f"Connected with result code  : {rc}")
    result, mid = client.subscribe(topic=userdata['topic'], qos=userdata['qos'])
    print(f"client.subscribe return: result={result}; mid={mid}\n")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"message received    : {str(msg.payload.decode('utf-8'))}")
    print(f"message topic       : {msg.topic}")
    print(f"message qos         : {msg.qos}")
    print(f"message retain flag : {msg.retain}\n")
    
def on_subscribe(client, userdata, mid, granted_qos):
    print(f"subscribed: mid:{mid} ; granted_qos:{granted_qos}\n")
    
if __name__ == "__main__"    :
    
    parser = ArgumentParser()
    parser.add_argument('--timer', '-t', type=float, default=100.0, help="loop stops after <timer> seconds; default=100.0")
    args = parser.parse_args()
    
    transport_tcp = "tcp" # default port if RabbitMQ is used with MQTT and TCP
    # transport_ws = "websockets"   
    userdata_D = {"topic": "eastside/camera1", "qos": 1}
    client = mqtt.Client(client_id="", clean_session=True, userdata=userdata_D, protocol=mqtt.MQTTv311, transport=transport_tcp)
    
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe

    port_tcp = 1883
    # port_ws = 15675 # default port if RabbitMQ is used with MQTT and websocket support
    ip_address = "127.0.0.1"
    
    client.connect(ip_address, port=port_tcp, keepalive=60)
 
    # subscribe to this topic -> done in the on_connect callback
    # topic = "eastside/camera1"
    # client.subscribe(topic)
    
    client.loop_start()

    try:
        print(f"timeout set to: {args.timer} seconds\n")
        time.sleep(args.timer)
    finally:
        print(f"stopping loop after: {args.timer} seconds\n")
        client.loop_stop()
        client.disconnect()

