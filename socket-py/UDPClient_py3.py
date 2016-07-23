from socket import *
serverName = "115.28.188.45"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('Inpot lowercase sentence:')
clientSocket.sendto(message,(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
printf(modifiedMessage)
clientSocket.close()
