# Receive message from p3, Send back
# Latest temperature as stored in a File
# Corresponding pi3 code is p3_get_temp_from_p2.py
# Next get the data from a file and send it back

import socket
from lib.libFile import readDataFromFile

def p2_send_temp_p3():
    local_host = "192.168.1.252"
    remote_ip = "192.168.1.253"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((local_host,port))

    mySocket.listen(10)
    while True:
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        if not data:
            print('Error receiving data')
            conn.close()
        else:
            if str(data) == "p3:TEMP":
                print ("from connected  user: " + str(data))
                data = readDataFromFile('../datafiles/p2CurrentTemperature.txt')
                print ("sending: " + str(data))
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                except socket.error:
                    print ('Failed to create socket')
                    conn.close()
                    continue
                try:
                    s.connect((remote_ip , port))
                except:
                    print ('connection refused')
                    conn.close()
                    continue
                try:
                    s.send(data.encode())
                    s.close()
                except:
                    print('Send data failed')
            else:
                print("unknown message")
        conn.close()
p2_send_temp_p3()
