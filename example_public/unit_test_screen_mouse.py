from lib.mkdev import MkDevice

import time


if __name__ == '__main__':

        # 获取硬件控制接口
        self = MkDevice()

        # 控制鼠标移动到屏幕中央
        self.mouse_move(MkDevice.screenWidth / 2, MkDevice.screenHeight / 2)

        time.sleep(1)

        # 控制鼠标移动到屏幕左上角
        self.mouse_move(0, 0)

        time.sleep(1)

        # 控制鼠标移动到屏幕左下角
        self.mouse_move(0, MkDevice.screenHeight)

        time.sleep(1)

        # 控制鼠标移动到屏幕右下角
        self.mouse_move(MkDevice.screenWidth, MkDevice.screenHeight)

        time.sleep(1)

        # 控制鼠标移动到屏幕右上角
        self.mouse_move(MkDevice.screenWidth, 0)

        time.sleep(1)

        # 控制鼠标移动到屏幕左上角
        self.mouse_move(0, 0)

        time.sleep(1)

        # 控制鼠标移动到屏幕中央
        self.mouse_move(MkDevice.screenWidth / 2, MkDevice.screenHeight / 2)

        time.sleep(1)
