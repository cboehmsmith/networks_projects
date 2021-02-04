# UDP Pinger
### Cat Smith for CS5700/Summer 2020

A simple UDP server and client. Currently the server address is hard-coded to the local host address (127.0.0.1) and 
port 12000.

To run the program, first run UDPPingerServer.py. Then run UDPPingerClient.py in a separate terminal window. Neither 
program requires user input. UDPPingerClient will send 10 pings. If the server responds, the client will print the 
response and the RTT; if the server does not respond within the timeout window of 1 second the client will print a 
"Request timed out" message. 