import configparser
import argparse
import paho.mqtt.client as paho
import time

def on_connect(unused_client, unused_userdata, unused_flags, rc):
    """Callback for when a device connects."""
    print('on_connect')

def on_publish(unused_client, unused_userdata, unused_mid):
    """Paho callback when a message is sent to the broker."""
    print('on_publish')


def main():
    # Construct the argument parser
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-c", "--client", required=True, help="mqtt client name")
    ap.add_argument("-t", "--topic", required=True, help="raspberry pi topic")
    #ap.add_argument("-tt", "--track-rpi", required=True, help="track raspberry pi topic")
    args = vars(ap.parse_args())

    client = str(args['client'])
    topic = str(args['topic'])

    print(client)
    print(topic)

    # Read local `config.ini` file.
    config = configparser.ConfigParser()                                     
    config.read('./config.ini')

    # Get values from our .ini file
    broker = config.get('MQTT', 'HOST')
    port = config.get('MQTT', 'PORT')
    username = config.get('MQTT', 'USERNAME')
    password = config.get('MQTT', 'PASSWORD')

    print(broker + port)

    client1= paho.Client(client)                           #create client object                          
    client1.on_connect = on_connect                       #assign function to callback
    client1.on_publish = on_publish                       #assign function to callback
    client1.username_pw_set(username=username,password=password)
    client1.connect(broker,port)                                 #establish connection

    while 1 :

        ret= client1.publish(topic,"{\"status\":\"on\"}")
        time.sleep(5)

if __name__ == '__main__':
    main()