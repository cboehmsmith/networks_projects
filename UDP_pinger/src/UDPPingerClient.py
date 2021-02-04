from socket import *
from timeit import *
from datetime import datetime


def main():

    serverName = '127.0.0.1'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    ping_ID = 1
    t = Timer()

    # send 10 pings via UDP
    while ping_ID < 11:
        clientSocket.settimeout(1)
        time = t.timeit()

        # client message is one line formatted as follows:
        # "Ping <sequence_number> <time>"
        clientMsg = "Ping " + str(ping_ID) + " " + str(datetime.now().time())
        clientSocket.sendto(clientMsg.encode(), (serverName, serverPort))
        ping_ID += 1

        # if server responds, print response
        # server response consists of capitalized echo of client message plus the calculated RTT
        try:
            response = clientSocket.recv(1024)
            print("RESPONSE: " + str(response.decode()) + "     RTT: " + str(time) + " seconds")
        except timeout:
            print("Request timed out")

    clientSocket.close()


main()
