# Some Demo Programs for MQTT

Tested with RabbitMQ / MQTT message broker on Windows 10 with Python 3.10.6

The test programs demonstrate publishing and subcribing to a topic.

There are versions which use `TCP` and `websockets` as a transport protocol.

**TCP :**

requires import: `import paho.mqtt.client as mqtt`

**Websockets:**

requires imports: 

`import asyncio`

`import asyncio_mqtt as aiomqtt`

`import paho.mqtt as mqtt`
