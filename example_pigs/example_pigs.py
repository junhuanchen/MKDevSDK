from lib.mkcv import *
from lib.mkdev import MkDevice

if __name__ == '__main__':
    try:
        # 设置一个监控范围
        setup_region(0, 0, 800, 1000)
        imgs = read_images('pigs')
        for img in imgs:
            cv.imshow(str(np.random.random()), img)

        dev = MkDevice()
        while True:
            res = screen_search(imgs, 0.8, True)
            if len(res):
                print(res)
                dev.mouse_move(res[0][0], res[0][1])
            if (cv.waitKey(100) == 27):
                break
    finally:
        cv.destroyAllWindows()
