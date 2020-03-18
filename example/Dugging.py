from NXController import Controller
import time


# 挖礦
def Dugging():
    ctr.A()


if __name__ == "__main__":
    ctr = Controller()

    print("{}搜尋控制器{}".format("=" * 5, "=" * 5))
    ctr.LR()
    time.sleep(2)

    print("{}開始執行程式{}".format("=" * 5, "=" * 5))
    print("挖礦中")
    while True:
        Dugging()

    ctr.close()