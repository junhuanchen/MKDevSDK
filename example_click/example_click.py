from lib.mkdev import MkDevice

import keyboard

# http://www.4399.com/flash/193481_1.htm
# 试玩地址

clinck_flag = False

def on_triggered():
    print("Triggered!")
    global clinck_flag
    clinck_flag = not clinck_flag

keyboard.add_hotkey('ctrl', on_triggered)
print("按 ctrl 启动连点器")

import time

if __name__ == '__main__':
    try:
        dev = MkDevice()
        while True:
            if clinck_flag:
                dev.mouse_click(0, 0.001)
            else:
                time.sleep(0.5)
    except Exception as e:
        print(e)
