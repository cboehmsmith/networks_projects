import pickle
from socket import *
from SimpleTransportSegment import *
import sys


def main():

    try:
        server_port_str = sys.argv[1]
        window_size = sys.argv[2]
        curr_file_name = sys.argv[3]
    except IndexError:
        print("Arguments expected. Correct command line argument formatted as follows:")
        print("python3 SimpleTransportServer.py <listening_port_number> <window_size> <output_file>")
        exit()

    try:
        server_port = int(server_port_str)
    except ValueError:
        print("Invalid argument. Port number must be an integer.")
        exit()

    # expected bytes in incoming segments' payloads
    # a payload less than this length indicates end of transmission
    expected_seg_length = 512

    conn = socket(AF_INET, SOCK_DGRAM)
    conn.bind(('', server_port))
    # times out after 5 min to prevent indefinite connection
    conn.settimeout(300.0)
    print("The server is ready to receive.")
    expected_seq = 0
    while True:
        try:
            incoming, return_address = conn.recvfrom(1024)
            if incoming:
                segment_in = pickle.loads(incoming)
                if segment_in.seq == expected_seq:
                    file = open(curr_file_name, "ab")
                    file.write(segment_in.payload)
                    file.close()
                    expected_seq = segment_in.seq + 1
                    ack_seg = SimpleTransportSegment(SegmentType.ACK, 0, expected_seq, 0, "")
                    outgoing_ack = pickle.dumps(ack_seg)
                    conn.sendto(outgoing_ack, return_address)
                    if segment_in.length < expected_seg_length:
                        print("Transmission complete.")
                        conn.close()
                        sys.exit(1)
        except timeout:
            print("No transmission received. Connection timed out after 5 minutes.")
            conn.close()
            sys.exit(1)


main()
