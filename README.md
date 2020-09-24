# RPi-Cluster-Alert
This repo is to make a system which alerts the user in various ways (locally and remotely) if any RPi in his cluster becomes dead.

Each RPI in cluster will be called a Node. Each Node will be running 2 services
- agent.service : this service send the data to cloud informing its presence
- tracker.service : this service listens to data about other nodes from the cloud and perform local notification if other nodes becomes non-responsive
Note : these services can be installed individually as per needs

Commands to control the services
```
- sudo systemctl stop agent.service/tracker.service
- sudo systemctl start agent.service/tracker.service
- sudo systemctl restart agent.service/tracker.service
- sudo systemctl status agent.service/tracker.service
```

### On the cloud App we can view the status of the cluster of RPi's

### For remote notification we are sending a SMS on Mobile phone with the name of the Raspberry Pi

Here is an Architecture of the system

<img src="https://github.com/samteck/RPi-Cluster-Alert/blob/master/rpi-cluster-alert.png" width="1000">

### Current system Explanation

We are having 2 raspberry pi's
1. John Snow (RPi-2) running ubuntu server 18.04.5 in headless mode
2. Khal Drogo (RPi-4) running raspbain with LXDE desktop

They both are sending the MQTT packets to the broker(configured in config.ini)

### MQTT Broker : Mosquitto Broker on an Azure VM instance (B1S) with username/password authentication

### NodeRed App : Backend app is deployed on another Azure VM and having a UI component where we can view the individual RPi's. This app also calls SMS API's

### Remote Access to RPI
Although the RPI's can be ssh, VNC from the local network, there might arise a situation where we need to control it from Public Internet in those cases we need to some provision for remote access.

RPi with Desktop Environment : VNC (similar to RDP)
RPi with headless Mode : remote.it (https://iot.samteck.net/enablers/networking/ssh-connection-public-internet/)

### RPi GPIO (https://iot.samteck.net/raspberry-pi/basics/raspberry-pi-gpio-pins/)
RPi's will be having a LED and Buzzer for local Notification
