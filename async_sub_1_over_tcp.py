# async_sub_1_over_tcp.py
#
# https://pypi.org/project/asyncio-mqtt/

import asyncio
import asyncio_mqtt as aiomqtt
import paho.mqtt as mqtt

client_params_D = {
        "hostname": "127.0.0.1",  # The only non-optional parameter
        "port": 1883,
        "username": None,
        "password" : None,
        "logger": None,
        "client_id": None,
        "tls_context": None,
        "tls_params": None,
        "proxy": None,
        "protocol": mqtt.client.MQTTv311,
        "will": None,
        "clean_session": None,
        "transport": "tcp",
        "keepalive": 60,
        "bind_address": "",
        "bind_port": 0,
        "clean_start": mqtt.client.MQTT_CLEAN_START_FIRST_ONLY,
        "properties": None,
        "message_retry_set": 20,
        "socket_options": (),
        "max_concurrent_outgoing_calls": None,
        "websocket_path": None,
        "websocket_headers": None}

topic = "eastside/camera1"

async def main():
    async with aiomqtt.Client(**client_params_D) as client:
        async with client.messages() as messages:
            # setting qos > 0 seems to avoid frequent disconnects ...
            await client.subscribe("eastside/camera1", qos=1)
            async for message in messages:
                print(f"[eastside/camera1] : {message.payload}")
                    
if __name__ == "__main__":
        
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

