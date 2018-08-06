# Read temp from DHT
# Add local time whem temp was Read
# Save data to a failed
# Append data to an archive

import sys
import Adafruit_DHT
import time
import datetime
from lib.libFile import  writeDataToFile
from lib.libFile import appendDataToFile

def p2AppendAmbTempToFile (temp):
    # append the temperature to a file to allow analysis of temperature changes.
    localDate = datetime.datetime.date(datetime.datetime.now()).strftime('%d/%m/%Y')
    localtime = datetime.datetime.time(datetime.datetime.now()).strftime('%H:%M:%S')
    data = localDate  + ' ' + localtime + ',' + temp + "\n"
    #print(data)
    appendDataToFile('../datafiles/p2ArchiveTemperature.txt', data)


def p2WriteAmbTempToFile (temp):
    # Write the temperature to a file. This will be the latest temperature
    data = temp + "\n"
    #print (data)
    writeDataToFile('../datafiles/p2CurrentTemperature.txt', data)

def p2ReadFromDHT():
    errorCount = 0
    while True:
        #humidity, temperature = Adafruit_DHT.read_retry(22, 4)
        humidity, temperature = Adafruit_DHT.read(22, 4)


        # Note that sometimes you won't get a reading and
        # the results will be null (because Linux can't
        # guarantee the timing of calls to read the sensor).
        # If this happens try again!

        if humidity is not None and temperature is not None:
            #print ('Temp= ' + str(format(temperature,'0.2f')))
            tempStr = str(format(temperature,'0.2f'))
            p2AppendAmbTempToFile(tempStr)
            p2WriteAmbTempToFile(tempStr)
        else:
            errorCount = errorCount + 1
            print ('Failed to get reading. Try again: ' + str(errorCount))
        time.sleep(2)

p2ReadFromDHT()
