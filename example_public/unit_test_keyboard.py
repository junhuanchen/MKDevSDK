from msvcrt import kbhit
from lib.mkhid import MKHID
import time
try:
    self = MKHID()
    while not kbhit() and self.device.is_plugged():

        print('self.getState()', self.getState())
        print('self.isCaps()', self.isCaps())
        print('self.isNumLock()', self.isNumLock())

        # 输出 ABCDEF 或 abcdef
        self.keyboard.press_key(b"\x04\x05\x06\x07\x08\x09")
        self.writeCmd(self.keyboard.getCmd())
        time.sleep(0.1)
        self.keyboard.clean_key()
        self.writeCmd(self.keyboard.getCmd())
        time.sleep(1)

except Exception as e:
    print(e)