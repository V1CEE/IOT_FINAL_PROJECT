import paho.mqtt.client as mqtt
import time
import random
from mqtt_init import *
from icecream import ic
from datetime import datetime, timedelta


def time_format():
    return f'{datetime.now()}  Manager|> '


ic.configureOutput(prefix=time_format)
ic.configureOutput(includeContext=False)


def on_log(client, userdata, level, buf):
    ic("log: " + buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        ic("connected OK")
    else:
        ic("Bad connection Returned code= ", rc)


def on_disconnect(client, userdata, flags, rc=0):
    ic("DisConnected result code " + str(rc))


def send_msg(client, topic, message):
    ic("Sending Message: " + message)
    client.publish(topic, message)


def client_init(cname):
    r = random.randrange(1, 10000000)
    ID = str(cname + str(r + 21))
    client = mqtt.Client(ID, clean_session=True)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_log = on_log
    client.username_pw_set(username="manager", password="manager")
    ic("Connecting to broker ", "broker.hivemq.com")
    client.connect("broker.hivemq.com", 1883)
    return client


def main():
    cname = "Filter-Change-Reminder-"
    client = client_init(cname)
    client.loop_start()
    start_time = datetime.now()  # Record the start time

    try:
        while True:
            elapsed_time = datetime.now() - start_time
            if elapsed_time >= timedelta(seconds=filter_replacement_threshold):
                ic("ALERT: a month has passed since the last filter change!")
                send_msg(client, "HomeAutomation/FilterChange",
                         "ALERT: a month has passed since the last filter change!")
                start_time = datetime.now()  # Reset start time
            time.sleep(1)
    except KeyboardInterrupt:
        client.disconnect()
        ic("Interrupted by keyboard")

    client.loop_stop()
    client.disconnect()
    ic("End of script run")


if __name__ == '__main__':
    main()
