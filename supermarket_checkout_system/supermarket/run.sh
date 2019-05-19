#!/bin/bash

cd /home/pi/darknet
./darknet detector test /home/pi/darknet/cfg/supermarket/obj.data /home/pi/darknet/cfg/supermarket/yolov3-tiny_deploy.cfg /home/pi/darknet/backup/supermarket/yolov3-tiny_2500.weights /home/pi/Desktop/supermarket/train_image/D2S_001408.jpg
cd
cd Desktop/supermarket
python calculate.py

cd 
cd /home/pi/Desktop/supermarket/current_record
rm predictions