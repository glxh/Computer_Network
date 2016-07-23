from socker import *
serverName = "hostname"
serverPort = 12000
clientSocket = socker(AF_INET,SOCK_DGRAM)
message = raw_inpot('Inpot lowercase sentence:')
clientSocket.sendto(message,(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
clientSocket.close()
