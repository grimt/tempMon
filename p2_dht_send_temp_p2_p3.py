
# Send temperatre measured from DHT to pi3

import sys
import os
import Adafruit_DHT
import time
import socket   #for sockets
import datetime

import gc





port = 5000;

remote_ip = '192.168.1.253' # pi3 ip address

gc_count = 0


while True:

    humidity, temperature = Adafruit_DHT.read(22, 4)
    current_time =  datetime.datetime.now()
    print ('Time: ' + str(current_time))

    if humidity is not None and temperature is not None:
        data = (str(current_time.strftime("%Y-%m-%d %H:%M")) + ',' + str(format(temperature,'0.2f')) )
    	#create an INET, STREAMing socket
        try:
        	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
        	print ('Failed to create socket')
        	sys.exit()

        try:
        	s.connect((remote_ip , port))
        except:
        	print ('connection refused')

        try :
        	#Connect to remote server
                s.sendall(data.encode())
                print ('Sent temperature:' + data)
        except:
        	#Send failed
        	print ('Send failed')
        s.close()

    else:
        print ('Failed to get reading. Try again!')
        

# Suspect repeated allocation of socket may be chewing up memory so garbage collect
    if gc_count > 5:
        gc_count = 0
        gc.collect()
    else:
        gc_count += 1
    time.sleep(2)
