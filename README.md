This is a README.md file for 2020-1 OSS Final Project
==========
My name is Jiho Kang, 21500014.  
'OSS_2020-1_Final_Projcet.py' was written by *Jiho Kang* 
using an open-source library.
-

Project Outline
-
The subject of the project is the Real-Time Intruder Alert System. 
 
Function 
- 
* Detect Intruder by using **Ultrasonic sensor**. 
* Mark the distance measured by ultrasonic sensors on **OLED**. 
* **Buzzer** sounds when within a certain distance range. 
* The measured distance is transferred to the server using **WIFI**. 

Python module install
- 
1. Ultrasonic Sensor (HC-SR04), Piezo Buzzer (SZH-SDBJ-007 ,Low+Passive) 
	* sudo pip install RPi.GPIO  
1. OLED (Monochrome 0.96 128x64 OLED graphic display ada-326) 
	* git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
1. Socket 
	* sudo pip install socket.py 

PIN-MAP 
- 
|GPIO.BCM | HC-SR04 | 
|-------- | ------- | 
|      23 |    TRIG |
|      24 |    ECHO | 
|      5V |     VCC | 
|     GND |     GND |  

