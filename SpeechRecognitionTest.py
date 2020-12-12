import speech_recognition as sr
import pyttsx3
import serial
import pyfirmata
from time import sleep

##Arduino_Serial = serial.Serial('com4',9600)  #Create Serial port object called arduinoSerialData
engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate
r = sr.Recognizer()

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

WAKE = "hey tyson"
WAKE1 = "hi tyson"
WAKE2 = "hello tyson"
board = pyfirmata.Arduino('COM4')
while True:

    with sr.Microphone() as source:

        
        audio = r.listen(source)

        
        try:
            text = r.recognize_google(audio).lower()
            print("You said: {}".format(text))
        except:

            text = ""
            print("sorry, did not hear that!")

        if text.count(WAKE) or text.count(WAKE1) or text.count(WAKE2):

            engine.say("How Can I Help?")
            print("Say Something!")
            engine.runAndWait()
            engine.stop()
            
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio).lower()
                print("You said: {}".format(text))

            except:

                text = ""
                print("sorry, did not hear that!")

            #print("You said: {}".format(text))
            


                
            if "lights on" in text or "turn on lights" in text or "turn on the lights" in text or "turn on all lights" in text:                   #if the entered data is 1 
                
                ##print (Arduino_Serial.readline())           #read the serial data and print it as line
                #print ("Enter 1 to ON LED and 0 to OFF LED")
                sleep(0.2)
                #Arduino_Serial.write(int(1))
                board.digital[8].write(1)
                board.digital[9].write(1)
                board.digital[10].write(1)
                board.digital[12].write(1)
                board.digital[13].write(1)
                ##Arduino_Serial.write(ord('1'))             #send 1 to arduino
                print ("LED ON")

            elif "lights off" in text or "turn off lights" in text or "turn off the lights" in text or "turn off all lights" in text:                   #if the entered data is 1 
                
                ##print (Arduino_Serial.readline())           #read the serial data and print it as line
                #print ("Enter 1 to ON LED and 0 to OFF LED")
                sleep(0.2)
                #Arduino_Serial.write(int(1))
                board.digital[8].write(0)
                board.digital[9].write(0)
                board.digital[10].write(0)
                board.digital[12].write(0)
                board.digital[13].write(0)
                ##Arduino_Serial.write(ord('1'))             #send 1 to arduino
                print ("LED ON")

            elif "how hot is it inside the house" in text or "temperature inside my house" in text or "what is the temperature inside" in text or "temperature inside" in text:

                #TODO: Activate DHT Sensor And Get The Temp And The Humidity From The Arduino To This, Python Program, And Round It To The Nearest Whole Degree!
                print("Activate DHT Sensor And Get The Temp And The Humidity From The Arduino To This, Python Program, And Round It To The Nearest Whole Degree!")