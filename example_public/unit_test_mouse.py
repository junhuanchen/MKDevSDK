from msvcrt import kbhit
from lib.mkhid import MKHID
import time
try:
    self = MKHID()
    while not kbhit() and self.device.is_plugged():

        time.sleep(1)

        # 测试鼠标左右中键（0，1，2）
        self.mouse.press(1), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)
        self.mouse.release(1), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)

        self.mouse.press(0), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)
        self.mouse.release(0), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)

        self.mouse.press(2), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)
        self.mouse.release(2), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)

        time.sleep(1)

        # 测试鼠标上下滚动
        self.mouse.scroll(1), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)
        self.mouse.scroll(0), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)
        self.mouse.scroll(-1), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)

        time.sleep(1)

        # 测试鼠标上右下左移动
        self.mouse.move(-128, -128), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)
        self.mouse.move(128, -128), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)
        self.mouse.move(128, 128), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)
        self.mouse.move(-128, 128), self.writeCmd(self.mouse.getCmd()), time.sleep(0.5)

except Exception as e:
    print(e)