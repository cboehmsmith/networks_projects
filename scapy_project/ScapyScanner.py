from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11, Dot11Elt

# def chan_hop(iface):
#    num = 1
#   stop = False
#   while not stop:
#        time.sleep(.5)
#        os.system("iwconfig %s channel %d" % iface, num)
#        dig = int(random.random() * 14)
#        if dig != 0 and dig != num:
#            num = dig


found_bssids = []


def findSSID(pkt):
    if pkt.haslayer(Dot11Beacon):
        if pkt.getlayer(Dot11).addr2 not in found_bssids:
            found_bssids.append(pkt.getlayer(Dot11).addr2)
            ssid = pkt.getlayer(Dot11Elt).info
            if ssid == "" or pkt.getlayer(Dot11Elt).ID != 0:
                print("Hidden Network Detected")
            print("Network Detected: %s" % ssid)


if __name__ == "__main__":

    print('Start')

    # sniff("your_file.pcap", findSSID, 0)
    scapy_cap = rdpcap('scapy.pcap')
    for packet in scapy_cap:
        findSSID(packet)
    print("End")
