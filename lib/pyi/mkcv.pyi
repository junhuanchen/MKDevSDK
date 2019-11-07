import cv2 as cv
import numpy as np

def setup_region(left, top, right, down):
    """
    以屏幕左上角（0，0）为起点的坐标系，为本模块的 screen_search 函数设定监控范围，参数对应监控的（左，上）和（右，下）两坐标，默认为监控全屏。
    :param left: 左上角起始点的坐标 X 值
    :param top: 左上角起始点的坐标 Y 值
    :param right: 右下角终止点的坐标 X 值
    :param down: 右下角终止点的坐标 Y 值
    :return:None
    """

def clear_region():
    """
    该函数用于清除 setup_region 的结果，恢复默认值。
    :return:None
    """

def center_region():
    """
    获取此时 setup_region 的监控画面的中点位置，用于定位相对位置。
    :return:None
    """

def screen_search(images, threshold=0.8, debug=False):
    """
    在捕获的屏幕范围中，识别找出导入的 image 集中相似度符合的图像。
    :param images: 传入 image 集， read_images 函数的返回值。
    :param threshold: 图像相似度阈值，默认值为 0.8 。
    :param debug: 调试开关，开启将会弹出图像匹配结果和对应的调试值，默认为 False 。
    :return:图像匹配的点（x，y）集。
    """

def read_images(dir_name):
    """
    读取指定目录下的所有图像文件，注意不要放入无关文件，会一起读取。
    :param dir_name: 设定读取图像样本集的目录。
    :return:images
    """

def event_fsm(state, expect, imgs_path, threshold, debug = False, event=lambda x:{print(x+1), print(x+2)}):
    """
    状态机函数事件函数，请根据案例的方式去使用，这只是为了减少代码写的框架接口，可以不使用。
    这是一个异步状态机事件，先是期望等待图像出现（状态转移 + 1），再直到到图像消失，（状态转移 + 2）。
    :param state: 传入的原始状态值
    :param expect: 固定的期望状态值（state + 1）或（state + 2）
    :param imgs_path: 图像集路径
    :param threshold: 图像相似度
    :param debug: debug 开关
    :param event: debug 开关
    :return:返回本次转移的状态值，返回值可能在 [state, state + 2] 范围。
    """

def azimuth_angle(x1, y1, x2, y2):
    """
    以北为 0 度基点的方位角计算函数，计算起始点 P1(x, y) 到 终止点 P2(x, y) 的向量角度值，表现为 P1 到 P2 的两点，。
    由于坐标系不好理解，可以参考 example_dnf 示例，可以打印方位角来感受一下方向值。
    :param x1: 起始点 X1
    :param y1: 起始点 Y1
    :param x2: 目标点 X2
    :param y2: 目标点 Y2
    :return:返回方位角度值。
    """

def euclidean_distance(x1, y1, x2, y2):
    """
    计算两点模，即为两点之间的欧拉距离，无关方向。
    :param x1: 起始点 X1
    :param y1: 起始点 Y1
    :param x2: 目标点 X2
    :param y2: 目标点 Y2
    :return:返回距离值（int）
    """

def enter_point(x1, y1, x2, y2):
    """
    计算两点之间的中点，自带方向。
    :param x1: 起始点 X1
    :param y1: 起始点 Y1
    :param x2: 目标点 X2
    :param y2: 目标点 Y2
    :return:返回（x，y）坐标。
    """
