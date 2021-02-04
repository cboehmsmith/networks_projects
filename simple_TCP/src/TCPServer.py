from socket import *


def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        swapSentence = sentence.swapcase()[::-1]
        connectionSocket.send(swapSentence.encode())
        connectionSocket.close()


main()