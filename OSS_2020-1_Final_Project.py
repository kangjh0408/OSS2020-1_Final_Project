import RPi.GPIO as GPIO 
import time 
import datetime 
import socket
import Adafruit_GPIO.SPI as SPI 
import Adafruit_SSD1306 
from PIL import Image 
from PIL import ImageDraw 
from PIL import ImageFont 

# Ultra-Sonic pin-map
TRIG=23 
ECHO=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT) # TRIG
GPIO.setup(ECHO, GPIO.IN)  # ECHO
GPIO.output(TRIG,False)
i=0 

# OLED pin-map 
RST=6
DC=12 
SPI_PORT=0
SPI_DEVICE=0
disp=Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE,max_speed_hz=8000000)) 
disp.begin() 
disp.clear() 
disp.display() 
font=ImageFont.load_default()

# Piezo Buzzer pin-map 
Buzzer=26 
GPIO.setup(Buzzer, GPIO.OUT)
piezo=GPIO.PWM(Buzzer,440) # (channel, frequency)
piezo.start(100) # Low+Passive  

# UDP_WIFI
UDP_IP="192.168.43.71"
UDP_PORT=50000
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

print "Start"
time.sleep(2)

print "Detect the intruder within 2 meters" 

try: 
    while True: 
	# Measure distance by Ultrasonic
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0: 
            pulse_start = time.time()
        
        while GPIO.input(ECHO)==1: 
            pulse_end = time.time() 

        pulse_duration = pulse_end - pulse_start 
        distance = pulse_duration * 17150 
        distance = round(distance+1.15,2)

        if distance<=200 and distance>=5: 
            print "distance:",distance,"cm" 
	    now=time.localtime()
	    message1_UDP="Intruder Detected within two meters!" 
	    message2_UDP="%04d/%02d/%02d %02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec) 	
	    message3_UDP="distance:",distance,"cm"
	    sock.sendto(message1_UDP, (UDP_IP, UDP_PORT)) 
	    sock.sendto(message2_UDP, (UDP_IP, UDP_PORT)) 
	    sock.sendto(str(message3_UDP), (UDP_IP, UDP_PORT))
            i=1
        if distance>200 and i==1: 
            print "It's over two meter..."
            i=0

	# Piezo Buzzer
	if distance<=200 and distance>=5: 
	    piezo.ChangeDutyCycle(40) 
	else : 
	    piezo.ChangeDutyCycle(100) 

        # Setting for OLED
        distance_OLED_print = distance,"cm"
        image = Image.new('1',(disp.width, disp.height)) 
        draw = ImageDraw.Draw(image) 
        draw.rectangle((0,0,disp.width-1,disp.height-1),outline=1,fill=0) 
        draw.text((8,8),'2020-1 OSS',font=font,fill=255) 
	draw.text((8,16),'Final Project',font=font,fill=255) 
        draw.text((8,24),'Distance:',font=font,fill=255)
        draw.text((8,32),str(distance_OLED_print),font=font,fill=255)
        
	# Display Image 
        disp.image(image) 
        disp.display()
        time.sleep(2)

except KeyboardInterrupt: 
    piezo.stop()
    disp.clear() 
    disp.display()
    GPIO.cleanup() 
