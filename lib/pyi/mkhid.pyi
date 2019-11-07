
class Mouse:

    def __init__(self):
        """
        初始化
        """

    def move(self, x, y, init=True):
        """
        以屏幕左上角（0，0）为起点的坐标系，将鼠标移动到指定位置。
        :param x: 指定坐标 X 值
        :param y: 指定坐标 Y 值
        :param init: 是否初始化当前指令值，否表示可以叠加设备状态。
        :return:None
        """

    def press(self, pos, init=True):
        """
        按下鼠标状态值。
        :param pos: 0 1 2 对应 左键 右键 中键
        :param init: 是否初始化当前指令值，否表示可以叠加设备状态。
        :return:None
        """

    def release(self, pos, init=True):
        """
        释放鼠标状态值。
        :param pos: 0 1 2 对应 左键 右键 中键
        :param init: 是否初始化当前指令值，否表示可以叠加设备状态。
        :return:None
        """

    def scroll(self, pos, init=True):
        """
        滚动鼠标状态值。
        :param pos: -1 0 +1 -1 ， 0 表示停止，1 可以是 0 - 7F
        :param init: 是否初始化当前指令值，否表示可以叠加设备状态。
        :return:None
        """

    def getCmd(self):
        """
        返回当前软设备的状态值
        :return:硬设备协议数据
        """

class Keyboard:

    def __init__(self):
        """
        初始化
        """

    def press(self, pos, init=True):
        """
        （特殊按键）按下键盘状态值。
        :param pos:  Control 0 Shift 1 Alt 2 GUI 3
        :param init: 是否初始化当前指令值，否表示可以叠加设备状态。
        :return:None
        """

    def release(self, pos, init=True):
        """
        （特殊按键）释放键盘状态值。
        :param pos:  Control 0 Shift 1 Alt 2 GUI 3
        :param init: 是否初始化当前指令值，否表示可以叠加设备状态。
        :return:None
        """

    def quick_key(ascii_key):
        """
        本来想实现快速调用接口，结果没实现，以后有需要再实现。
        """

    def press_key(self, keys, init=True):
        """
        释放键盘状态值。
        :param pos: 查阅资料 keyboard hid to ps2.pdf 参考 HID Usage ID 一列值。
        :param init: 是否初始化当前指令值，否表示可以叠加设备状态。
        :return:None
        """

    def clean_key(self, init=True):
        """
        清除键盘状态值。
        :param pos: 查阅资料 keyboard hid to ps2.pdf 参考 HID Usage ID 一列值。
        :param init: 是否初始化当前指令值，否表示可以叠加设备状态。
        :return:None
        """

    def getCmd(self):
        """
        返回当前软设备的状态值
        :return:硬设备协议数据
        """

class MKHID:

    def __init__(self):
        """
        初始化。
        """
        self.mouse = Mouse()
        self.keyboard = Keyboard()

    def getState(self):
        """
        读取硬件状态数据，可以更新键盘数据或读取硬件版本号。
        """

    def isCaps(self):
        """
        执行 getState 后有效，判断大小写是否开启。
        """

    def isNumLock(self):
        """
        执行 getState 后有效，判断小键盘数字锁定写是否开启。
        """

    def writeCmd(self, data):
        """
        任何 getCmd 的数据都可以导入 writeCmd 后交由硬件执行，核心接口，如果需要也可以直接调用。
        """

