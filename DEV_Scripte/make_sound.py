#Bibliotheken
import RPi.GPIO as GPIO
import time
 
#GPIO definieren (Modus, Pins, Output)
GPIO.setmode(GPIO.BCM)
SOUND = 26

GPIO.setup(SOUND, GPIO.OUT)

p = GPIO.PWM(SOUND, 241)
p.start(50)
time.sleep(0.5)
GPIO.cleanup()
