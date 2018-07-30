# NOTE: This scrpt requires python3

import sys
import Adafruit_DHT
import time

while True:
    #humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    humidity, temperature = Adafruit_DHT.read(22, 4)


    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).  
# If this happens try again!

    if humidity is not None and temperature is not None:
        print ('Temp= ' + str(format(temperature,'0.2f')))
    else:
        print ('Failed to get reading. Try again!')
    time.sleep(2)
