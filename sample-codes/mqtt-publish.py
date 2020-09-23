# Test program to check the Broker Status

import paho.mqtt.client as paho

# Eclipse Broker Address
broker="***********"
port=1883
#username_pw_set(username="*******",password="******")

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

client1= paho.Client("RPi-1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection

ret= client1.publish("John Snow","on")                   #publish