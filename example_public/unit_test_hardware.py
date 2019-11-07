from msvcrt import kbhit
from lib.mkhid import MKHID
import time
try:
    self = MKHID()
    while not kbhit() and self.device.is_plugged():
        tmp = b'\xBD\x01\x02\x39\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        self.writeCmd(tmp)

        tmp += b'\xBD\x02\x01\x01\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        self.writeCmd(tmp)

        tmp += b'\xBD\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        self.writeCmd(tmp)

        tmp += b'\xBD\x02\x01\x00\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        self.writeCmd(tmp)
        time.sleep(0.5)
except Exception as e:
    print(e)