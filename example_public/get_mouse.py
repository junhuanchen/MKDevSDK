# -*- encoding: utf-8 -*-

import time
import pyautogui as pag
import os

try:
    while True:
        print("Press Ctrl-C to end")
        screenWidth, screenHeight = pag.size()  # 获取屏幕的尺寸
        x, y = pag.position()  # 返回鼠标的坐标
        print("Screen size: (%s %s),  Position : (%s, %s)\n" % (screenWidth, screenHeight, x, y))  # 打印坐标

        time.sleep(1)  # 每个1s中打印一次 , 并执行清屏
        os.system('cls')  # 执行系统清屏指令
except KeyboardInterrupt:
    print('end')

