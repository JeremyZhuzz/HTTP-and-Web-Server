#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
host = sys.argv[1]
port = int(sys.argv[2])

serverSocket.bind((host,port))
serverSocket.listen(10)
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept()
            
    try:
        message = connectionSocket.recv(1024)              
        filename = message.split()[1]                 
        f = open(filename[1:]) 

        outputdata = f.read()               
        #Send one HTTP header line into socket
        connectionSocket.send("GET /""HTTP/1.1 200OK\r\n\r\n".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
       	connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
