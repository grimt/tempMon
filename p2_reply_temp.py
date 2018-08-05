# Receive message from p3, Send back
# Latest temperature as stored in a File
# Nect get the data from a file and send it back

import socket

def p2_send_temp_p3():
    local_host = "192.168.1.252"
    remote_ip = "192.168.1.253"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((local_host,port))

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
            try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except socket.error:
                    print ('Failed to create socket')
                    break 
            try:
                    s.connect((remote_ip , port))
            except:
                    print ('connection refused')

            try :
                    s.sendall(data.encode()) 
                  #  conn.send(data.encode())
                    s.close()
            except:
                print('Send data failed')
                break

p2_send_temp_p3()
