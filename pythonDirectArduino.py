import speech_recognition as sr
import pyttsx3
import serial
from pyfirmata import Arduino, util
import time

'''
board = Arduino("COM4")
loopTimes = input('How many times would you like the LED to blink: ')
print("Blinking " + loopTimes + " times.")
for x in range(int(loopTimes)):
  board.digital[11].write(1)
  time.sleep(0.2)
  board.digital[11].write(0)
  time.sleep(0.2)
'''
import pyfirmata
import time

board = pyfirmata.Arduino('COM4')

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)