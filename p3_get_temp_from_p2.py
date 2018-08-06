# Send a message to p2 asking for the temperature
# Wait for the result then print it out
# corresponding pi2 code is p2_reply_temp.py
import socket
import time

def p3_get_temp_from_p2():
        local_host = "192.168.1.253"
        remote_ip = "192.168.1.252"
        port = 5000

        mySocket = socket.socket()
        mySocket.bind((local_host,port))
        mySocket.listen(10)
        gtPause = input(" -> ")
        while True: 
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except socket.error:
                print ('Failed to create socket')
                break
            try:
                s.connect((remote_ip , port))
            except:
                print ('connection refused')

            try:
                message = "p3:TEMP"
                print ('Sending ' + message)
                s.send(message.encode())
                s.close()
            except:
                print('Send data failed')

            conn, addr = mySocket.accept()
            print ("Connection from: " + str(addr))
            data = conn.recv(1024).decode()
            print ('Received from server: ' + data)
            conn.close()

            s.close()
            time.sleep(5)

p3_get_temp_from_p2()
