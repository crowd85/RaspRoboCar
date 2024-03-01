#Bibliotheken
import RPi.GPIO as GPIO
import time
 
#GPIO definieren (Modus, Pins, Output)
GPIO.setmode(GPIO.BCM)

TRIGGER_LINKS = 24
ECHO_Links = 23

TRIGGER_RECHTS = 25
ECHO_RECHTS = 12

SOUND = 26

GPIO.setup(TRIGGER_LINKS, GPIO.OUT)
GPIO.setup(ECHO_Links, GPIO.IN)

GPIO.setup(TRIGGER_RECHTS, GPIO.OUT)
GPIO.setup(ECHO_RECHTS, GPIO.IN)

GPIO.setup(SOUND, GPIO.OUT)

def SoundDistance(myValue):
	p = GPIO.PWM(SOUND, myValue)
	p.start(80)
	time.sleep(0.5)

def entfernung(myTrigger, myEcho):
    #print ("Trigger auf true")
    # Trig High setzen
    GPIO.output(myTrigger, True)

    # Trig Low setzen (nach 0.01ms)
    time.sleep(0.00001)
    #print ("Trigger auf false")
    GPIO.output(myTrigger, False)
 
    Startzeit = time.time()
    Endzeit = time.time()
 
    # Start/Stop Zeit ermitteln
    while GPIO.input(myEcho) == 0:
        Startzeit = time.time()
 
    while GPIO.input(myEcho) == 1:
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
			distanz_Rechts = "unknown/r"
			distanz_Links = "unknown/l"
			#print ("Starte Links")
			distanz_Links = entfernung(TRIGGER_LINKS,ECHO_Links)
			#print ("Starte Rechts")
			distanz_Rechts = entfernung(TRIGGER_RECHTS,ECHO_RECHTS)
			
			print ("Distanz Links = %.1f cm" % distanz_Links, "Distanz Rechts = %.1f cm" % distanz_Rechts)
			
			if 100 <= distanz_Links <= 150:
				print ("Achtung! Weniger als 150")
				SoundDistance(241)
			elif 50 <= distanz_Links <= 99:
				print ("Achtung! Weniger als 100")
				SoundDistance(441)
			elif 20 <= distanz_Links <= 49:
				print ("Achtung! Weniger als 50")
				SoundDistance(741)
			elif 15 <= distanz_Links <= 19:
				print ("Achtung! Gleich gibt es einen Unfall!!")
				SoundDistance(941)
			elif 10 <= distanz_Links <= 14:
				print ("Achtung! Gleich gibt es einen Unfall!!")
				SoundDistance(1141)
			elif 5 <= distanz_Links <= 9:
				print ("Achtung! Gleich gibt es einen Unfall!!")
				SoundDistance(1341)
			elif 1 <= distanz_Links <= 4:
				print ("Achtung! Gleich gibt es einen Unfall!!")
				SoundDistance(1541)
			else:
				print ("Alles gut")
				time.sleep(0.5)
			#time.sleep(1)
			#print ("Distanz Rechts = %.1f cm" % distanz_Rechts)
			#time.sleep(0.5)
 
        # Programm beenden
    except KeyboardInterrupt:
        print("Programm abgebrochen")
        GPIO.cleanup()
    
