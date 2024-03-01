#!/bin/bash

#echo "Wechsel Verzeichnis für Cam-Uebertragung"
#cd "Desktop/Sun/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/mjpg-streamer/mjpg-streamer"
echo "Starte LiveCam Uebertragung"
sh "Desktop/Sun/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/mjpg-streamer/mjpg-streamer/start.sh"

#echo "Wechsel Verzeichnis für Robo-Server"
#cd "Desktop/Sun/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server"
echo "Starte Robo-Server"
python 'Desktop/Sun/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/tcp_server.py'
