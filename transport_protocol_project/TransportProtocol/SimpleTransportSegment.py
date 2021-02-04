from enum import Enum


class SegmentType(Enum):
    DATA = 0x1
    ACK = 0x2


class SimpleTransportSegment(object):

    def __init__(self, seg_type=SegmentType.ACK, win=0, seq=-1, length=0, payload=""):
        self.seg_type = seg_type
        self.win = win
        self.seq = seq
        self.length = length
        self.payload = payload
