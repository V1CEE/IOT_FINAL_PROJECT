import paho.mqtt.client as mqtt
import time
import random

# broker IP address:
broker = "mqtt-dashboard.com"
running_time = 90  # in sec
topic = 'pr/home/AC_Filter/sts'
port = 1883  # Standard port for MQTT


def on_log(client, userdata, level, buf):
    print("log: " + buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code= ", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("DisConnected result code " + str(rc))


def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("message received: ", m_decode)


r = random.randrange(1, 10000)  # for creating unique client ID
ClientName = "IOT_test-" + str(r)
client = mqtt.Client(ClientName, clean_session=True)  # create new client instance

client.on_connect = on_connect  # bind call back function
client.on_disconnect = on_disconnect
# client.on_log=on_log
client.on_message = on_message

print("Connecting to broker ", broker)
client.connect(broker, port)  # connect to broker

client.loop_start()
client.publish(topic,
               '{"type":"set_state", "action":"set_value", "addr":0, "cname":"ONOFF", "value":1}')  # Publish to topic
client.subscribe(topic)  # Subscribe to topic
time.sleep(running_time)
client.loop_stop()
client.disconnect()  # disconnect
print("End of script run")
