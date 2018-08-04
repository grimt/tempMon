# Send a message to p2 asking for the temperature
# Wait for the result then print it out
import socket

def get_temp_from_p2():
        host = '192.168.1.252'
        port = 5000

        mySocket = socket.socket()
        mySocket.connect((host,port))

        message = input(" -> ")

        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()

                print ('Received from server: ' + data)

                message = input(" -> ")

        mySocket.close()
