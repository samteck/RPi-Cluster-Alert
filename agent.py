######################
#Project Title : RPi Cluster Alert
#Module        : agent to send heartbeat signals
#Author        : Samarth Gupta
#Date          : 24/09/2020
#Version       : 1.0

import configparser
import argparse
import paho.mqtt.client as paho
import time

def on_connect(unused_client, unused_userdata, unused_flags, rc):
    """Callback for when a device connects."""
    print('sucessfully connected')

def on_publish(unused_client, unused_userdata, unused_mid):
    """Paho callback when a message is sent to the broker."""
    print('status message published')

def main():
    try:
        # Construct the argument parser
        ap = argparse.ArgumentParser()

        # Add the arguments to the parser
        ap.add_argument("-c", "--client", required=True, help="mqtt client name")
        ap.add_argument("-t", "--topic", required=True, help="raspberry pi topic")
        #ap.add_argument("-tt", "--track-rpi", required=True, help="track raspberry pi topic")
        args = vars(ap.parse_args())

        client = str(args['client'])
        topic = str(args['topic'])
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
    except:
        print('please check the config file')

    try:
        client1= paho.Client(client)                           #create client object
        client1.on_connect = on_connect                       #assign function to callback
        client1.on_publish = on_publish                       #assign function to callback
        client1.username_pw_set(username=username,password=password)
        client1.connect(broker,port)                                 #establish connection
    except:
        print('connection to broker unsuccessfull')

    while 1 :
        try:
            ret= client1.publish(topic,"{\"status\":\"on\"}")
        except:
            print('can not publish the data')
        time.sleep(5)

if __name__ == '__main__':
    main()
