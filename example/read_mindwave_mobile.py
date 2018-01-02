import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap

if __name__ == '__main__':
#    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader = MindwaveDataPointReader("CC:78:AB:15:40:93")
    mindwaveDataPointReader.start()
    if (mindwaveDataPointReader.isConnected()):    
        while(True):
            try:
                dataPoint = mindwaveDataPointReader.readNextDataPoint()
                if (not dataPoint.__class__ is RawDataPoint):
                    print dataPoint
            except IndexError:
                pass
    else:
        print(textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " "))
        
