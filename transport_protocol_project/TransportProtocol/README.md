#DESCRIPTION

####A simple emulation of a transport protocol that includes three files:
####    1) SimpleTransportSegment.py, a utility class for creating transport data and acknowledgment "segments"
####    2) SimpleTransportServer.py, which listens for incoming segments
####    3) SimpleTransportClient.py, which initiates a connection and sends segments

#HOW TO RUN IT

####The server must be run first, using the following input to the command line:
####python3 SimpleTransportServer.py <listening_port_number> <window_size> <output_file>
####All three parameters are required. Once the server indicates it is running ("The server is ready to receive" will appear on the screen), then the client can be run using the following input to the command line:
####python3 SimpleTransportClient.py <destination_DNS_name> <destination_port_number> <window_size> <input_file>
####Again, all arguments are required. 