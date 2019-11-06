from lib.mkcv import *
from lib.mkdev import MkDevice

import time
import keyboard


def on_triggered():
    print("Triggered!")
    import os
    os._exit(0)


keyboard.add_hotkey("esc", on_triggered)
print("按左上角的 ESC 键即可退出程序")

# 刷课示范，东莞理工学院内部刷课网站。

if __name__ == '__main__':
    try:
        print(__file__)

        # 利用工具去定位框，方法查阅用户手册
        setup_region(0, 78, 940, 1048)

        dev = MkDevice()
        game_fsm = 0  # 可以指定处于某状态，边写边叠加
        while True:
            # print('game_fsm', game_fsm)

            if (cv.waitKey(100) == 27):
                break

            if game_fsm < 1:
                res = screen_search(read_images('./goal'), 0.8, True)
                if len(res):  # 找到可以观看的视频，点击进入
                    time.sleep(1)  # 延时展示效果，debug 标记物是否稳定
                    dev.mouse_move(res[0][0], res[0][1], True)
                    dev.mouse_click(0)
                    game_fsm = 1
                    time.sleep(1) # 等待进入视频页面，避免误判
                else:
                    res = screen_search(read_images('./extend'), 0.8, True)
                    if len(res):  # 没有视频可以观看，点击展开
                        print("找不到所以点击展开列表和滚动列表")
                        dev.mouse_move(res[0][0], res[0][1], True)
                        dev.mouse_click(0)
                    dev.mouse_scroll(-1)  # 向下滚动找目标

            elif game_fsm < 2:  # 视频启动后会自动播放，等待它停止播放
                res = screen_search(read_images('./end'), 0.8, True)
                if len(res):  # 直到找到停止播放的标记物
                    print("视频已停止播放")
                    res = screen_search(read_images('./back'), 0.8, True)
                    if len(res):  # 确认视频结束，此时可以找一下返回按钮退回上级
                        time.sleep(1)  # 延时展示效果，debug 标记物是否稳定
                        dev.mouse_move(res[0][0], res[0][1], True)
                        dev.mouse_click(0)
                        game_fsm = 2
            elif game_fsm < 3:
                game_fsm = 0  # 状态机回归，重新开始
            else:
                pass  # break
    except Exception as e:
        print(e)
    finally:
        cv.destroyAllWindows()
