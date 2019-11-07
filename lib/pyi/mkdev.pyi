from lib.mkhid import MKHID

class MkDevice(MKHID):
    screenWidth, screenHeight = int, int
    """
    当前屏幕的宽度和高度
    """

    def __init__(self):
        """
        初始化
        """

    def keyboard_click(self, key, interval=0.1):
        """
        控制键盘点击函数，使用方法可以查阅各类 example 示例，例如：self.keyboard.press_key(b"\x04\x05\x06\x07\x08\x09")
        :param key: 查阅资料 keyboard hid to ps2.pdf 参考 HID Usage ID 一列值。
        :param interval: 按下与松开的间隔
        :return:None
        """

    def mouse_click(self, key = 0, interval=0.05):
        """
        控制鼠标点击函数。
        :param key: 0 为左键、1 为右键、2 为中键，可参阅 HID1.11.pdf 文档资料。
        :param interval: 按下与松开的间隔
        :return:None
        """


    def mouse_scroll(self, value, interval=0.1):
        """
        控制鼠标滚动函数
        :param value: 0 为停止，+1 向上滚动，-1 为向下滚动，此值会因系统不同而相反。
        :param interval: 按下与松开的间隔
        :return:None
        """


    def mouse_move_click(self, go_x, go_y, key = 0, lock=False, interval=0.05):
        """
        控制鼠标按下并移动后再松开的函数，常见于 Andorid 模拟器中使用鼠标模拟手指触摸的工作方式。
        :param go_x: 期望移动的位置 X
        :param go_y: 期望移动的位置 Y
        :param key: 0 为左键、1 为右键、2 为中键，可参阅 HID1.11.pdf 文档资料。
        :param lock: 是否锁定鼠标，默认为 False （不锁定）。
        :param interval: 鼠标移动，按下与松开的间隔
        :return:None
        """

    def mouse_move(self, go_x, go_y, lock=False, interval=0.05):
        """
        控制鼠标移动到指定坐标的函数。
        :param go_x: 期望移动的位置 X
        :param go_y: 期望移动的位置 Y
        :param lock: 是否锁定鼠标，默认为 False （不锁定）。
        :param interval: 移动的间隔
        :return:None
        """


