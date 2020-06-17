This is a README.md file for 2020-1 OSS Final Project.<br/> 
Subject: "Real-Time Intruder Alert System"
==============
My name is Jiho Kang, 21500014.  
'OSS_2020-1_Final_Projcet.py' was written by *Jiho Kang*.<br/>
The function of the sensor operation is used through an open source library.<br/> 
*An example of each sensor module was used to write code into one System('OSS_2020-1_Final_Project.py')*
-

Open Source and Example Link
- 
1. UltraSonic sensor(HC-SR04) 
	* https://www.electronicshub.org/raspberry-pi-ultrasonic-sensor-interface-tutorial/ 

2. 128x64 OLED(Adafruit Monochrome 0.96) 
	* https://github.com/adafruit/Adafruit_Python_SSD1306
3. Piezo Buzzer(SZH-SDBJ-007, Low+Passive) 
	* https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
4. Socket 
	* https://wiki.python.org/moin/Udpcommunication

What does this project do?
-
The subject of the project is the Real-Time Intruder Alert System.<br/>
 
Function
* Detect Intruder by using **Ultrasonic sensor**. 
* Mark the distance measured by ultrasonic sensors on **OLED**. 
* **Buzzer** makes warning sound when within a certain distance range. 
* The measured distance is transferred to the server using **Wi-Fi**. 

Why is this project useful?
- 
Cadillac(Car Manfacturing Co.) adopted an ultrasonic sensor that prevents intrusions by detecting internal movements after the door is locked. This example shows the efficiency of ultrasonic sensors. It is expected that damage caused by intruders will be greatly reduced by using ultrasonic sensors and by immediately sending warning messages to users using Wi-Fi communication.

How do I get started? 
-
Python Module Install<br/>
1. Ultrasonic Sensor (HC-SR04), Piezo Buzzer (SZH-SDBJ-007 ,Low+Passive) 
	* sudo pip install RPi.GPIO  
1. OLED (Monochrome 0.96 128x64 OLED graphic display ada-326) 
	* git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
1. Socket 
	* sudo pip install socket.py 

PIN-MAP<br/>
|GPIO.BCM | HC-SR04 | 
|-------- | ------- | 
|      23 |    TRIG |
|      24 |    ECHO | 
|      5V |     VCC | 
|     GND |     GND |   

|GPIO.BCM | OLED(SPI)| 
|-------- | -------- | 
|       6 |      RST | 
|      12 |       DC |  
|     GND |      GND | 
|      5V |      VCC | 
|(SCLK)11 |      CLK | 
|(MOSI)10 |     DATA | 
|      12 |       DC | 

|GPIO.BCM | Buzzer | 
|-------- | ------ | 
|    3.3V |    VCC | 
|     GND |    GND | 
|      26 |    I/O |

Where can I get more help, if I need it? 
- 
If you have any questions, feel free to contact email address below:<br/>
Email Address: 21500014@handong.edu 

YouTube video link address 
-  
You can see the operation of this project.<br/>
Link: https://youtube.com/watch?v=tPhkbKHc6fw&t=13s 

