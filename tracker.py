######################
#Project Title : RPi Cluster Alert
#Module        : tracker to detect and notify dead raspberry pi
#Author        : Samarth Gupta
#Date          : 24/09/2020
#Version       : 1.0

import configparser
import argparse
import paho.mqtt.client as paho
import time
import json
import RPi.GPIO as IO

# setting mode for GPIO pins and disabling intial GPIO warnings
led = 2
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(led,IO.OUT)

def on_connect(client, userdata, flags, rc):
    """Callback for when a device connects."""
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    """Paho callback when a message is received."""
    print(msg.topic+" "+str(msg.payload))
    json_data = json.loads(msg.payload)
    check_breakdown(json_data['status'])

#check if other pi is down or not
def check_breakdown(str):
    if (str == "on"):
        print('its ON baby')
        IO.output(led,IO.LOW)
    elif (str == "off"):
        print('its GONE baby')
        i = 0
        while i<10:
            glitter()
            i+=1

# led light on-off            
def glitter():
    IO.output(led,IO.HIGH)
    time.sleep(1)
    IO.output(led,IO.LOW)
    time.sleep(1)

def main():
    try:
        # Construct the argument parser
        ap = argparse.ArgumentParser()

        # Add the arguments to the parser
        ap.add_argument("-c", "--client", required=True, help="mqtt client name")
        ap.add_argument("-r", "--rpi", required=True, help="track raspberry pi topic")
        args = vars(ap.parse_args())

        client = str(args['client'])
        rpi = str(args['rpi'])
    except:
        print('please check the arguments passed')

    try:
        # Read local `config.ini` file.
        config = configparser.ConfigParser()                                     
        config.read('./config.ini')

        # Get values from our .ini file
        broker = config.get('MQTT', 'HOST')
        port = int(config.get('MQTT', 'PORT'))
        username = config.get('MQTT', 'USERNAME')
        password = config.get('MQTT', 'PASSWORD')
        #led = int(config.get('RPi', 'LED'))
        #print(led)
    except:
        print('please check the config file')

    try:
        client2= paho.Client(client,clean_session=False)                           #create client object                          
        client2.on_connect = on_connect                       #assign function to callback
        client2.on_message = on_message                       #assign function to callback
        client2.username_pw_set(username=username,password=password)
        client2.connect(broker,port)                             #establish connection
        client2.subscribe(rpi)
        client2.loop_forever()
    except:
        print('connection to broker unsuccessfull')

if __name__ == '__main__':
    main()
