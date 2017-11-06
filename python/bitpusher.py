import time
import serial
from transloc_data import *


class ArduinoBridge(object):
    def __init__(self):
       
        #PORTS = ['/dev/ttyACM0', '/dev/ttyACM1']
        #just try to connect to these ports on the raspberry pi for serial data to the arduino
        for port in PORTS:
            try:
                print 'connecting to', port
                self.port = serial.Serial(port, 115200, rtscts=True, dsrdtr=True)
            except:
                print 'failed to connect'
                continue
            break
    #writing to the arduino probably with updates
    def write(self, updates, elapsed=0):
        out = []
        for w in updates:
            #woohoo updates 
            next = [
                w.index,
                (w.start >> 8) & 0xFF,
                w.start & 0xFF,
                (w.end >> 8) & 0xFF,
                w.end & 0xFF,
                (w.color >> 16) & 0xFF,
                (w.color >> 8) & 0xFF,
                w.color & 0xFF,
            ]
            out = out + next
        t0 = time.time()
        self.port.write(''.join(map(chr, out)))
        self.port.write(chr(0xFF))
        #write to arduino finished woohoo
        time.sleep(SLEEP_TIME)
