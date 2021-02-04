import pickle
import sys
from socket import *
from SimpleTransportSegment import SimpleTransportSegment, SegmentType


def create_segments(file_in, win_size):
    segments = []
    index = 0

    with open(file_in, "rb") as input_file:
        while True:
            # set max payload size to 512 bytes
            payload = input_file.read(512)
            # empty byte string indicates end of file has been reached
            if payload == b"":
                input_file.close()
                break
            else:
                new_seg = SimpleTransportSegment(SegmentType.DATA, win_size, index, len(payload), payload)
                segments.append(new_seg)
                index += 1
                # index = index % 256

    return segments


class SimpleTransportClient(object):

    def __init__(self, server_name, server_port, my_socket):
        self.server_name = server_name
        self.server_port = server_port
        self.my_socket = my_socket
        self.my_socket.connect((server_name, server_port))

    def send_segments(self, segments, win_space):

        base = 0
        next_seq = 0
        # TIMEOUT WINDOW INITIALIZED HERE
        timeout_window = 2.0

        while True:
            try:
                if next_seq < base + win_space:
                    outgoing = pickle.dumps(segments[next_seq])
                    self.my_socket.send(outgoing)
                    if base == next_seq:
                        self.my_socket.settimeout(timeout_window)
                    next_seq += 1

                incoming = self.my_socket.recv(1024)

                # whenever an acknowledgement packet is received
                if incoming:
                    new_ack = pickle.loads(incoming)
                    print("Acknowledgement received.")
                    base = new_ack.seq + 1
                    if base == next_seq:
                        self.my_socket.settimeout(None)
                    else:
                        self.my_socket.settimeout(timeout_window)
                    if new_ack.seq == len(segments):
                        print("All acknowledgements received. Transmission complete.")
                        self.my_socket.close()
                        sys.exit(1)
            except timeout:
                print("Timeout event. Resetting timer.")
                self.my_socket.settimeout(timeout_window)
                for index in range(base, next_seq):
                    outgoing2 = pickle.dumps(segments[index])
                    self.my_socket.send(outgoing2)


def main():

    try:
        dns = sys.argv[1]
        port = int (sys.argv[2])
        window = int (sys.argv[3])
        input_file = sys.argv[4]
    except IndexError:
        print("Arguments expected. Correct command line argument formatted as follows:")
        print("python3 SimpleTransportClient.py <destination_DNS_name> <destination_port_number> <window_size> "
              "<input_file>")
        sys.exit(1)

    client = SimpleTransportClient(dns, port, socket(AF_INET, SOCK_DGRAM))
    segment_list = create_segments(input_file, window)
    client.send_segments(segment_list, window)


main()
