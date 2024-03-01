#Bibliotheken
import RPi.GPIO as GPIO
import time
 
#GPIO definieren (Modus, Pins, Output)
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 24
GPIO_ECHO = 23
#GPIO_TRIGGER = 26
#GPIO_ECHO = 19
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)



def entfernung():
    #print ("Trigger auf true")
    # Trig High setzen
    GPIO.output(GPIO_TRIGGER, True)
 
    # Trig Low setzen (nach 0.01ms)
    time.sleep(0.00001)
    #print ("Trigger auf false")
    GPIO.output(GPIO_TRIGGER, False)
 
    Startzeit = time.time()
    Endzeit = time.time()
 
    # Start/Stop Zeit ermitteln
    temp = GPIO.input(GPIO_ECHO)
    while GPIO.input(GPIO_ECHO) == 0:
        print ("GPIO Echo (0): ")
        Startzeit = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        print ("GPIO Echo (1): ")
        Endzeit = time.time()
 
    # Vergangene Zeit
    Zeitdifferenz = Endzeit - Startzeit
    #print ("Start: " % Startzeit)
    #print ("Ende: " % Endzeit)
    # Schallgeschwindigkeit (34300 cm/s) einbeziehen
    entfernung = (Zeitdifferenz * 34300) / 2
 
    return entfernung
 
if __name__ == '__main__':
    try:
        print ("Starte Abstandsmessung...")
        while True:
            distanz = entfernung()
            print ("Distanz = %.1f cm" % distanz)
            time.sleep(1)
 
        # Programm beenden
    except KeyboardInterrupt:
        print("Programm abgebrochen")
        GPIO.cleanup()
    
