# Send a message to p2 asking for the temperature
# Wait for the result then print it out
import socket

def p3_get_temp_from_p2():
        local_host = '192.168.1.252'
        remote_ip = "192.168.1.253"
        port = 5000

        mySocket = socket.socket()
        mySocket.connect((local_host,port))

        message = input(" -> ")

        while message != 'q':
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
                        s.send(message.encode())
                        data = mySocket.recv(1024).decode()

                        print ('Received from server: ' + data)

                        message = input(" -> ")
                        s.close()
                except:
                    print('Send data failed')
                    break




        mySocket.close()

p3_get_temp_from_p2()
