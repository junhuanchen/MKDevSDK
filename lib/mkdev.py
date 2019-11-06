from lib.mkhid import MKHID
import pyautogui as pag
import time

class MkDevice(MKHID):
    screenWidth, screenHeight = pag.size()

    def __init__(self):
        MKHID.__init__(self)

    def keyboard_click(self, key, interval=0.1):
        self.keyboard.press_key(key)
        self.writeCmd(self.keyboard.getCmd())
        time.sleep(interval)
        self.keyboard.clean_key()
        self.writeCmd(self.keyboard.getCmd())
        time.sleep(interval)

    def mouse_click(self, key = 0, interval=0.05):
        self.mouse.press(key)
        self.writeCmd(self.mouse.getCmd())
        time.sleep(interval)
        self.mouse.release(key)
        self.writeCmd(self.mouse.getCmd())
        time.sleep(interval)

    def mouse_scroll(self, value, interval=0.1):
        self.mouse.scroll(value)
        self.writeCmd(self.mouse.getCmd())
        time.sleep(interval)
        self.mouse.scroll(0)
        self.writeCmd(self.mouse.getCmd())
        time.sleep(interval)

    def mouse_move_click(self, go_x, go_y, key = 0, lock=False, interval=0.05):
        go_x, go_y = int(go_x), int(go_y)

        self.mouse.press(key, True)
        self.writeCmd(self.mouse.getCmd())
        time.sleep(interval)

        x, y = pag.position()
        while go_x != x or go_y != y:

            if lock:
                x, y = pag.position()

            # print((go_x, go_y), (x, y))

            tmp_x = -(x - go_x)
            if tmp_x < -0x7F:
                tmp_x = -0x7F
            if tmp_x > 0x7F:
                tmp_x = 0x7F
            x = x + tmp_x

            tmp_y = -(y - go_y)
            if tmp_y < -0x7F:
                tmp_y = -0x7F
            if tmp_y > 0x7F:
                tmp_y = 0x7F
            y = y + tmp_y

            # print(tmp_x, tmp_y)

            self.mouse.move(int(tmp_x), int(tmp_y), False)

            self.writeCmd(self.mouse.getCmd())

            time.sleep(interval)

        self.mouse.release(key, False)
        self.writeCmd(self.mouse.getCmd())
        time.sleep(interval)

    def mouse_move(self, go_x, go_y, lock=False, interval=0.05):
        go_x, go_y = int(go_x), int(go_y)

        x, y = pag.position()
        while go_x != x or go_y != y:

            if lock:
                x, y = pag.position()

            # print((go_x, go_y), (x, y))

            tmp_x = -(x - go_x)
            if tmp_x < -0x7F:
                tmp_x = -0x7F
            if tmp_x > 0x7F:
                tmp_x = 0x7F
            x = x + tmp_x

            tmp_y = -(y - go_y)
            if tmp_y < -0x7F:
                tmp_y = -0x7F
            if tmp_y > 0x7F:
                tmp_y = 0x7F
            y = y + tmp_y

            # print(tmp_x, tmp_y)

            self.mouse.move(int(tmp_x), int(tmp_y))

            self.writeCmd(self.mouse.getCmd())

            time.sleep(interval)

    def unit_mouse_move(self):

        self.mouse_move(MkDevice.screenWidth / 2, MkDevice.screenHeight / 2)

        time.sleep(1)

        self.mouse_move(0, 0)

        time.sleep(1)

        self.mouse_move(0, MkDevice.screenHeight)

        time.sleep(1)

        self.mouse_move(MkDevice.screenWidth, MkDevice.screenHeight)

        time.sleep(1)

        self.mouse_move(MkDevice.screenWidth, 0)

        time.sleep(1)

        self.mouse_move(0, 0)

        time.sleep(1)

        self.mouse_move(MkDevice.screenWidth / 2, MkDevice.screenHeight / 2)

        time.sleep(1)

if __name__ == '__main__':
    pass
    MkDevice().unit_mouse_move()