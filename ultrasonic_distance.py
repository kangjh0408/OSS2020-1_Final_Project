# Ultra-Sonic
import RPi.GPIO as GPIO 
import time 

# OLED
import Adafruit_GPIO.SPI as SPI 
import Adafruit_SSD1306 
from PIL import Image 
from PIL import ImageDraw 
from PIL import ImageFont 

# Ultra-Sonic Pin-map
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
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE,max_speed_hz=8000000)) 
disp.begin() 
disp.clear() 
disp.display() 
font=ImageFont.load_default()

print "Calibrating...."
time.sleep(2)

print "Place the object...." 

try: 
    while True: 
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

        if distance<=100 and distance>=5: 
            print "distance:",distance,"cm"
            i=1
        if distance>100 and i==1: 
            print "It's over one meter..."
            i=0
        
        # Setting for OLED
        OLED_print = "distance:",distance,"cm"
        image = Image.new('1',(disp.width, disp.height)) 
        draw = ImageDraw.Draw(image) 
        draw.rectangle((0,0,disp.width-1,disp.height-1),outline=1,fill=0) 
        draw.text((8,8),'2020 OSS Final Projcet',font=font,fill=255) 
        draw.text((8,16),str(OLED_print),font=font,fill=255) 
        
        # Display Image 
        disp.image(image) 
        disp.display()
        time.sleep(2)

except KeyboardInterrupt: 
    GPIO.cleanup()
