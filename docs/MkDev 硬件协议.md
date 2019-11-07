# `MkDev` 硬件协议（2019年11月8日）

摘取局部代码可知，如果看不懂，可以直接问我。

```c
// DebugBytes("tmp.event", tmp.event, sizeof(tmp.event));
switch (tmp.event[1])
{
    case 0x01:
        switch (tmp.event[2])
        {
            case 0x00:
                Enp1IntIn(&tmp.event[3], KEYBOARD_LEN);
                break;
            case 0x01:
                ClickKey(tmp.event[3]);
                break;
            case 0x02:
                ClickCustom(tmp.event[3]);
                break;
        }
        break;
    case 0x02:
        switch (tmp.event[2])
        {
            case 0x00:
                Enp2IntIn(&tmp.event[3], MOUSE_LEN);
                break;
            case 0x01:
                MouseMove(tmp.event[3], tmp.event[4], tmp.event[5]);
                break;
            case 0x02:
                MouseScroll(tmp.event[3]);
                break;
        }
        break;
    case 0x03:
        report(Array, Recv);
        break;
    default:
        break;
}

```

里面的指令就三类，两个转发，一个返回，再补一个返回数据的函数。

```c

void report(QueueArray *Array, UINT8 *Recv)
{
    const UINT8 VERSION = 0x11;

    memset(Recv, 0, MAX_PACKET_SIZE);
    Recv[0] = VERSION;
    Recv[1] = 4;
    Recv[2] = GetKeyboardLedStatus();
    Recv[3] = isNumLock();
    Recv[4] = isCapsLock();
    Recv[5] = QueueArraySize(Array);
    Enp3IntIn(Recv, MAX_PACKET_SIZE);
}
```

想添加更多有用的协议功能，可以提交 issue 来聊聊，本文档写于 2019年11月8日。

