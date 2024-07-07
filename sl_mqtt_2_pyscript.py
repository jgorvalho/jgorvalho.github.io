import random
from paho.mqtt import client as mqtt_client
import json
import time
from js import document

broker = 'mqtt.streamline.pt'
port = 1883
topic = "application/4e85f534-31b7-4f51-ba15-2ecd63e5f5f5/device/a84041feb1875df6/event/up"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
username = "mwg"
password = "6KbTvz7b9XxS"
nivel_baixo = 0
nivel_alto = 0
mom=""

        
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc, properties):
        if rc == 0:
            #print("Connected to MQTT Broker!")
        else:
            #print(rc)
            #print(f"Failed to connect, return code: {rc}")

    #client = mqtt_client.Client(client_id)
    client = mqtt_client.Client(client_id=client_id, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
    
    client.username_pw_set(username, password)
    
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, message):
        global message_received
        time.sleep(1)
        message_received=str(message.payload.decode("utf-8"))
        
        msg=json.loads(message_received)
        
        #print(f"Received `{message.payload.decode()}` from `{message.topic}` topic")
        #print(msg)
        
        obj=msg["object"]
        nivel_baixo = obj["AVI2_V"]
        nivel_alto = obj["AVI1_V"]
        #print(f"Nivel do fundo: {nivel_baixo}")
        #print(f"Nivel do topo: {nivel_alto}")
        mom=msg["time"]
        #print(mom)
        document.getElementById("mom-value").innerHTML = mom
        document.getElementById("nivel-baixo-value").innerHTML = nivel_baixo
        document.getElementById("nivel-alto-value").innerHTML = nivel_alto
        

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    #print(f"nivel baixo: {nivel_baixo}")
    #print(f"nivel alto: {nivel_alto}")
    #print(f"dia e hora: {mom}")
    
    client.loop_forever()

if __name__ == '__main__':
    run()