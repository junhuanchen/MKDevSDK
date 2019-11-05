import cv2 as cv
import numpy as np
import pyautogui

region = None # left, top, right, down

def setup_region(left, top, right, down): # size_x, size_y
    global region
    region = (left, top, right - left, down - top)
    # region = (left, top, left + size_x, top + size_y)

def clear_region():
    global region
    region = None

def center_region():
    global region
    return ((region[0] + region[2]) / 2, (region[1] + region[3]) / 2)

def screen_search(images, threshold=0.8, debug=False):
    global region
    screen = pyautogui.screenshot(region=region)
    target = cv.cvtColor(np.asarray(screen), cv.COLOR_RGB2BGR)

    points = []
    for template in images:
        th, tw = template.shape[:2]
        res = cv.matchTemplate(target, template, cv.TM_CCOEFF_NORMED)
        # if debug:
        #     print('screen_search ', res)
        loc = np.where(res >= threshold)  # 默认匹配程度大于 80% 的坐标 y,x
        for lt in zip(*loc[::-1]):  # *号表示可选参数
            point = list((lt[0] + (tw / 2), lt[1] + (th / 2)))
            if region:
                # print(point, region)
                point[0], point[1] = point[0] + region[0], point[1] + region[1]
            points.append(point)  # center point
            if debug:
                rb = (lt[0] + tw, lt[1] + th)
                cv.rectangle(target, lt, rb, (0, 0, 255), 2)
                print('screen_point ', (lt[0] + rb[0]) / 2, (lt[1] + rb[1]) / 2)
    if debug:
        cv.namedWindow("screen_search", cv.WINDOW_NORMAL)
        if region:
            cv.resizeWindow("screen_search", region[2], region[3])
        cv.imshow("screen_search", target)
    return points

def read_images(dir_name):
    import os
    arr_of_img = []
    for filename in os.listdir(r"./" + dir_name):
        # print(dir_name + "/" + filename)
        img = cv.imread(dir_name + "/" + filename)
        if img.any():
            arr_of_img.append(img)
    return arr_of_img

def event_fsm(state, expect, imgs_path, threshold, debug = False, event=lambda x:{print(x+1), print(x+2)}):
    if (state == expect):
        res = screen_search(read_images(imgs_path), threshold, debug)
        if len(res):
            state = expect + 1
    elif (state == expect + 1):
        res = screen_search(read_images(imgs_path), threshold, debug)
        if len(res):
            event(res)
        else:
            state = expect + 2
    return state

import math

# 获得 方位角
def azimuth_angle(x1, y1, x2, y2):
    angle = 0.0
    dx = x2 - x1
    dy = y2 - y1
    if x2 == x1:
        angle = math.pi / 2.0
        if y2 == y1:
            angle = 0.0
        elif y2 < y1:
            angle = 3.0 * math.pi / 2.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dx / dy)
    elif x2 > x1 and y2 < y1:
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif x2 < x1 and y2 < y1:
        angle = math.pi + math.atan(dx / dy)
    elif x2 < x1 and y2 > y1:
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    return (angle * 180 / math.pi)

import numpy as np
# 欧几里德范数
def euclidean_distance(x1, y1, x2, y2):
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])
    p3 = p2 - p1
    return math.hypot(p3[0], p3[1])

def enter_point(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

if __name__ == '__main__':
    x1, y1, x2, y2 = 20, 20, 40, 30
    tmp = euclidean_distance(x1, y1, x2, y2)
    print(tmp)
    if tmp > 0:
        print(enter_point(x1, y1, x2, y2))
        print(azimuth_angle(x1, y1, x2, y2))

    # print(euclidean_distance(x1, y1, x2, y2))
