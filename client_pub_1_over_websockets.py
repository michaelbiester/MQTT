# client_pub_1_over_websockets.py
# publishes messages to MQTT broker
# uses a websocket connection between publisher and broker
"""
from paho library
https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#usage-and-api

some useful hints found in:
http://www.steves-internet-guide.com/mqtt-python-beginners-course/
"""

import paho.mqtt.client as mqtt
import time

print(f"Some useful error codes")
print(f"mqtt.MQTT_ERR_SUCCESS: {mqtt.MQTT_ERR_SUCCESS}")
print(f"mqtt.MQTT_ERR_NO_CONN: {mqtt.MQTT_ERR_NO_CONN}")
print(f"mqtt.MQTT_ERR_QUEUE_SIZE : {mqtt.MQTT_ERR_QUEUE_SIZE}\n")


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("publisher -> connecting to broker")
    print(f"Connected with result code  : {rc}\n")


# The callback for when a PUBLISH message is received from the server.
def on_publish(client, userdata, mid):
    print(f"result from publish: {mid}\n")
    
transport_tcp = "tcp" 
transport_ws = "websockets"   
client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport=transport_ws)

client.on_connect = on_connect
client.on_publish = on_publish

# port_tcp = 1883
port_ws = 15675 # default port if RabbitMQ is used with MQTT and websocket support
ip_address = "127.0.0.1"

# using ws_options() with a proper path is essential (although little information could be found)
client.ws_set_options(path="/ws")
client.loop_start()
client.connect(ip_address, port=port_ws, keepalive=60)

# start publishing messages
topic = "eastside/camera1"

for k in range(30):
    time.sleep(3.0)
    msg_nr = k
    msg = str(f"\nmessage nr: {msg_nr}")
    pub_info = client.publish(topic, payload=msg, retain=True, qos=1)
      
client.loop_stop()    
client.disconnect() 
   
