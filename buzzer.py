import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM) 

buzzer=26 
scale=[261,294,329,349,392,440,493,523] 
GPIO.setup(buzzer,GPIO.OUT) 

p=GPIO.PWM(buzzer,261) # (channel, frequency) 

p.start(40) 
try: 
    for i in range(8): 
        p.ChangeFrequency(scale[i]) # freq is the new frequency in Hz
        print "Current frequency:",scale[i],"Hz"
        time.sleep(1)  
        p.ChangeDutyCycle(100)
        time.sleep(1) 
        p.ChangeDutyCycle(40)
    p.stop() 
    GPIO.cleanup()
except KeyboardInterrupt:
    p.stop() 
    GPIO.cleanup() 

