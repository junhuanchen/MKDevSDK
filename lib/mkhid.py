import sys
import time
import pywinusb.hid as hid

class Mouse:

    def __init__(self):
        self.cmd = bytearray(b'\x00' * 16)
        self.cmd[0], self.cmd[1], self.cmd[2] = 0xBD, 0x02, 0x00

    def move(self, x, y, init=True):
        if init:
            self.__init__()
        # print(x, y)

        if x > 0x7F:
            x = 0x7F
        if x < -0x7F:
            x = -0x7F
        if x < 0:
            x = 0xFF - abs(x + 1)

        if y > 0x7F:
            y = 0x7F
        if y < -0x7F:
            y = -0x7F
        if y < 0:
            y = 0xFF - abs(y + 1)

        self.cmd[4], self.cmd[5] = x, y

    def press(self, pos, init=True): # left 0 center 2 right 1
        if init:
            self.__init__()
        self.cmd[3] = self.cmd[3] | (0x1 << pos)

    def release(self, pos, init=True): # left 0 center 2 right 1
        if init:
            self.__init__()
        self.cmd[3] = self.cmd[3] & ~(0x1 << pos)

    # 0x01 向前一格 0x00 和 0x80 停下 0xFF 向后一格
    def scroll(self, pos, init=True):
        if init:
            self.__init__()
        # print(pos)
        if (pos < 0):
            pos = 0xFF - abs(pos + 1)

        # print(pos)
        self.cmd[6] = pos

    def getCmd(self):
        return self.cmd

class Keyboard:

    def __init__(self):
        self.cmd = bytearray(b'\x00' * 16)
        self.cmd[0], self.cmd[1], self.cmd[2] = 0xBD, 0x01, 0x00

    def press(self, pos, init=True): # left: Control 0 Shift 1 Alt 2 GUI 3
        if init:
            self.__init__()
        self.cmd[3] = self.cmd[3] | (0x1 << pos)

    def release(self, pos, init=True): # left: Control 0 Shift 1 Alt 2 GUI 3
        if init:
            self.__init__()
        self.cmd[3] = self.cmd[3] & ~(0x1 << pos)

    def quick_key(ascii_key): # "ABCDEF" to b"\x04\x05\x06\x07\x08\x09"
        pass

    def press_key(self, keys, init=True):
        if init:
            self.__init__()
        pos, stop = 5, 5 + len(keys)
        if stop > 11:
            stop = 11
        while pos < stop:
            self.cmd[pos] = keys[pos - 5]
            pos = pos + 1

    def clean_key(self, init=True):
        if init:
            self.__init__()
        pos = 5
        while pos < 11:
            self.cmd[pos] = 0x00
            pos = pos + 1

    def getCmd(self):
        return self.cmd

class MKHID:

    def __init__(self):
        devs = hid.HidDeviceFilter(vendor_id=0x2019, product_id=0x0769).get_devices()
        # print(devs)
        if (len(devs)):
            self.device = devs[0]
            self.device.open()
            self.device.set_raw_data_handler(self.readData)
            self.output_report = self.device.find_output_reports()[0]

            self.mouse = Mouse()
            self.keyboard = Keyboard()
            self.keyboard_state = 0
        else:
            self.device = None
            raise Exception("Please insert hardware")

    def __del__(self):
        if (self.device != None):
            self.device.close()

    def readData(self, data):
        if (data[0] == 0x00):
            if data[1] == 0x11:
                self.keyboard_state = data[3]

    def getState(self):
        self.writeCmd(b'\xBD\x03')
        time.sleep(0.05)
        return self.keyboard_state

    def isCaps(self):
        return (self.keyboard_state & 0x2) == 0x2

    def isNumLock(self):
        return (self.keyboard_state & 0x1) == 0x1

    def writeCmd(self, data):
        while (len(data) < 64):
            data += b'\x00'
        self.output_report.set_raw_data(b'\x00' + data)
        self.output_report.send()

    def unit_test_write(self):

        tmp = b'\xBD\x01\x02\x39\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        self.writeCmd(tmp)

        tmp += b'\xBD\x02\x01\x01\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        self.writeCmd(tmp)

        tmp += b'\xBD\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        self.writeCmd(tmp)

        tmp += b'\xBD\x02\x01\x00\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        self.writeCmd(tmp)

    def unit_test_hardware(self):
        from msvcrt import kbhit

        try:
            while not kbhit() and self.device.is_plugged():
                self.unit_test_write()
                time.sleep(0.5)
        except Exception as e:
            print(e)

    def unit_test_mouse(self):
        from msvcrt import kbhit

        try:
            while not kbhit() and self.device.is_plugged():

                self.mouse.press(0)
                self.mouse.press(1)
                self.mouse.press(2)

                self.mouse.scroll(1)

                self.mouse.move(128, -128)

                # print(self.mouse.getCmd())

                self.writeCmd(self.mouse.getCmd())

                time.sleep(0.1)

                self.mouse.release(0)
                self.mouse.release(1)
                self.mouse.release(2)

                self.mouse.scroll(-1)

                self.mouse.move(-128, 128)

                # print(self.mouse.getCmd())

                self.writeCmd(self.mouse.getCmd())

                time.sleep(0.1)

        except Exception as e:
            print(e)

    def unit_test_keyboard(self):
        from msvcrt import kbhit

        try:
            while not kbhit() and self.device.is_plugged():
                print('self.getState()', self.getState())
                print('self.isCaps()', self.isCaps())
                print('self.isNumLock()', self.isNumLock())

                self.keyboard.press_key(b"\x04\x05\x06\x07\x08\x09")

                # print(self.keyboard.getCmd())

                self.writeCmd(self.keyboard.getCmd())

                time.sleep(0.1)

                self.keyboard.clean_key()

                # print(self.keyboard.getCmd())

                self.writeCmd(self.keyboard.getCmd())

                time.sleep(1)

        except Exception as e:
            print(e)

if __name__ == '__main__':
    pass
    # MKHID().unit_test_mouse()
    # MKHID().unit_test_hardware()
    # MKHID().unit_test_keyboard()
