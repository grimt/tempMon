# Receive message from p3, Send back
# Latest temperature as stored in a File
# Nect get the data from a file and send it back

import socket

def p2_send_temp_p3():
    host = "192.168.1.253"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))

            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())

    conn.close()

    p2_send_temp_p3()
