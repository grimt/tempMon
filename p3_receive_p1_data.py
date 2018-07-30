# This is for the LOCAL pi3 
# Accept and parse a message from pi1.

import socket
import sys

 
HOST = '192.168.1.253'   # IP address of receiver - i.e. this device 
PORT = 5000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print 'Socket created'
   
try:
    s.bind((HOST, PORT))
except socket.error :
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
                    
print ('Socket bind complete')
            
s.listen(10)
print ('Socket now listening')

#conn, addr = s.accept()
                      
#now keep talking with the client
while 1:
#wait to accept a connection - blocking call
    conn, addr = s.accept()
    # print 'Connected with ' + addr[0] + ':' + str(addr[1])
                                           
    temp_str = conn.recv(1024).decode()
    print ('Received: ' + str(temp_str ))
conn.close()
s.close()
