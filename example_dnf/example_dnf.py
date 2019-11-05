from lib.mkcv import *

from lib.mkdev import MkDevice

import threading
import time

dev = MkDevice()


# right 0x4F left down up
def control_allow(allow=[], interval=0.1):
    dev.keyboard_click(bytes(allow), interval)


def close_to_points(x1, y1, x2, y2, interval=0.25):
    # 距离目标大于 4 时 ，假设未遮挡识别物体的时候。可以靠近
    if euclidean_distance(x1, y1, x2, y2) > 4:
        # 由 终点 2 到 起点 1 提供方位角 上北下南左西右
        tmp = azimuth_angle(x2, y2, x1, y1)
        # print(tmp)  # 方位角象限
        if tmp > 0 and tmp <= 90:  # 左上 西北
            control_allow([0x50, 0x52], interval)
        if tmp > 90 and tmp <= 180:  # 左下 西南
            control_allow([0x50, 0x51], interval)
        if tmp > 180 and tmp <= 270:  # 右下 东南
            control_allow([0x4F, 0x51], interval)
        if tmp > 270 and tmp <= 360:  # 右上 东北
            control_allow([0x4F, 0x52], interval)


try:
    # 非全屏的窗口模式都会建议使用工具去捕获位置
    setup_region(4, 215, 803, 810)

    game_fsm = 0  # 可以指定处于某状态
    self_pos = 0, 0

    while True:

        # print(game_fsm)
        if (cv.waitKey(100) == 27):
            break

        if (game_fsm < 2):
            game_fsm = event_fsm(game_fsm, 0, './dnf/home', 0.8, True, lambda res: {
                print('试图离开家'),
                control_allow([0x4F], 2),
            })
        elif (game_fsm < 4):
            game_fsm = event_fsm(game_fsm, 2, './dnf/risk', 0.8, True, lambda res: {
                print('向冒险图移动'),
                control_allow([0x50, 0x51], 4),
            })
        elif (game_fsm < 6):
            game_fsm = event_fsm(game_fsm, 4, './dnf/select_map', 0.8, True, lambda res: {
                print('按空格选图或用鼠标移动控制'),
                # dev.mouse_move(res[0][0], res[0][1]), dev.mouse_click(0)
                control_allow([0x2C], 0.5),  # space
            })
        elif (game_fsm < 8):
            # 锁定玩家位置
            def lock_self():
                global self_pos
                while True:
                    res = screen_search(read_images('./dnf/self'), 0.8, True)
                    if len(res):
                        self_pos = res[0][0], res[0][1] + 75  # - 50 修正到角色身体位置
                    time.sleep(0.5)


            # 自动输入攻击
            def lock_fight():
                while True:
                    time.sleep(1)

                    # 寻怪 跟踪 靠近
                    res = screen_search(read_images('./dnf/monster'), 0.4, True)
                    if len(res):
                        print('寻怪', res[0])
                        close_to_points(self_pos[0], self_pos[1], res[0][0], res[0][1]),

                        control_allow([0x4F], 0.2)
                        control_allow([0x1B], 0.1), control_allow([0x1B], 0.1), control_allow([0x1B], 0.1)
                        # control_allow([0x50], 0.1)


            threading.Thread(target=lock_self).start()
            threading.Thread(target=lock_fight).start()
            print('定位玩家位置，建立额外的控制角色任务')
            game_fsm += 2
        elif (game_fsm < 10):
            # print('确认定位到玩家', self_pos)
            # if (self_pos[0] != 0 or self_pos[1] != 0):
            game_fsm = event_fsm(game_fsm, 8, './dnf/room_01/01', 0.8, True, lambda res: {
                print('通过键盘移动靠近追踪的目标', self_pos, res[0]),
                close_to_points(self_pos[0], self_pos[1], res[0][0], res[0][1]),
            })
        elif (game_fsm < 12):
            game_fsm = event_fsm(game_fsm, 10, './dnf/room_01/02', 0.8, True, lambda res: {
                print('找到门口，直到离开', self_pos, res[0]),
                close_to_points(self_pos[0], self_pos[1], res[0][0], res[0][1]),
                control_allow([0x4F, 0x52], 2)
            })
        elif (game_fsm < 14):
            print('流程结束')
            break

finally:
    cv.destroyAllWindows()
