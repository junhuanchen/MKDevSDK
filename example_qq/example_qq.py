from lib.mkcv import *
from lib.mkdev import MkDevice

import time
import keyboard


def on_triggered():
    print("Triggered!")
    import os
    os._exit(0)

keyboard.add_hotkey("esc", on_triggered)
print("编辑器激活的时候，按左上角的 ESC 键即可退出程序")

if __name__ == '__main__':
    try:
        print(__file__)

        # 利用工具去定位框，方法查阅用户手册
        setup_region(55, 103, 562, 926)

        dev = MkDevice()

        game_fsm = 0  # 可以指定处于某状态，边写边叠加

        while True:

            print('game_fsm', game_fsm)
            if (cv.waitKey(100) == 27):
                break

            if (game_fsm < 2):  # 回到首页
                game_fsm = event_fsm(game_fsm, 0, './qq/index', 0.8, True, lambda res: {
                    dev.mouse_move(res[0][0], res[0][1], True),
                    dev.mouse_click(0)
                })
            elif (game_fsm < 4):  # 离开文件夹，找到软件列表
                game_fsm = event_fsm(game_fsm, 2, './qq/back', 0.8, True, lambda res: {
                    dev.mouse_move(res[0][0], res[0][1], True),
                    dev.mouse_click(0),
                    dev.mouse_click(0),
                    dev.mouse_click(0),
                })
            elif (game_fsm < 6):  # 找到 QQ 软件，点击进入 QQ 软件
                game_fsm = event_fsm(game_fsm, 4, './qq/open', 0.8, True, lambda res: {
                    dev.mouse_move(res[0][0], res[0][1], True),
                    dev.mouse_click(0)
                })
            elif (game_fsm < 8):  # 发现处于首页，持续向左滑动，然后进入名片列表

                # 进入了不想进入的页面，查找并点击取消，可以直接点击后退键
                res = screen_search(read_images('./qq/error'), 0.8, True)
                if len(res):
                    dev.mouse_move(res[0][0], res[0][1], True)
                    dev.mouse_click(0)

                def touch_left_swipe():
                    tmp = center_region()
                    dev.mouse_move(tmp[0] - 100, tmp[1], True)
                    dev.mouse_move_click(tmp[0] + 250, tmp[1], 0, True, 0.25)

                game_fsm = event_fsm(game_fsm, 6, './qq/into', 0.8, True, lambda res: {
                    touch_left_swipe()
                })

            elif (game_fsm < 10):  # 进入名片页面，根据这次的定位结果，点击的位置在 Y 轴相对的 中间 二分之一 。
                def touch_left_swipe():
                    tmp = center_region()
                    dev.mouse_move(tmp[0], tmp[1] / 2)
                    dev.mouse_click(0) # 不要在没有定位好位置的时候去点击

                game_fsm = event_fsm(game_fsm, 8, './qq/mp', 0.8, True, lambda res: {
                    touch_left_swipe()
                })
            elif (game_fsm < 12):  # 找到大拇指，点击进入点赞页面 。
                game_fsm = event_fsm(game_fsm, 10, './qq/dz', 0.8, True, lambda res: {
                    dev.mouse_move(res[0][0], res[0][1]),
                    dev.mouse_click(0, 0.5),
                })
            elif (game_fsm < 14): # 在点赞列表，将所有找到的大拇指都点赞
                def all_dianzhan(all_object):
                    # print('all_object', all_object)
                    for point in all_object:
                        # print('point', point)
                        dev.mouse_move(point[0], point[1])
                        # 选中后重复点击 20 次
                        for i in range(0, 10):
                            dev.mouse_click(0)

                    # 进入到了广告界面，关掉
                    res = screen_search(read_images('./qq/adv'), 0.8, True)
                    if len(res):
                        dev.mouse_move(res[0][0], res[0][1], True)
                        dev.mouse_click(0)

                    # 翻下一页
                    tmp = center_region()
                    dev.mouse_move(tmp[0], tmp[1] + 200)
                    dev.mouse_move_click(tmp[0], tmp[1] - 200, 0, True, 0.25)

                game_fsm = event_fsm(game_fsm, 12, './qq/dz20', 0.8, True, lambda res: {
                    all_dianzhan(res)
                })

                # 翻下一页
                tmp = center_region()
                dev.mouse_move(tmp[0], tmp[1] + 50)
                dev.mouse_move_click(tmp[0], tmp[1] - 50, 0, True, 0.25)

            else:
                pass  # break

    except Exception as e:
        print(e)
    finally:
        cv.destroyAllWindows()
