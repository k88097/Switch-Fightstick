from NXController import Controller
import time

# 瓦特收集


def WattCollect():
    # 站在洞前
    # ctr.A()
    # time.sleep(0.5)
    ctr.A()
    time.sleep(2)
    ctr.B()
    time.sleep(0.5)

    # 到主畫面
    ctr.h()
    time.sleep(0.5)

    # 到設定畫面
    ctr.d()
    ctr.r()
    ctr.r()
    ctr.r()
    ctr.r()
    ctr.A()
    time.sleep(0.5)

    # 到設定時間畫面
    ctr.d(2.3)
    ctr.A()
    ctr.d()
    ctr.d()
    ctr.d()
    ctr.d()
    ctr.A()

    #到調整時間選項
    ctr.d()
    ctr.d()
    ctr.A()

    #調整時間加一天
    ctr.r()
    ctr.r()
    ctr.u()
    ctr.r(1)
    ctr.A()

    # 回到主畫面並且進入遊戲
    ctr.h(0.3)
    ctr.h(0.3)

    # 退出招募
    ctr.A()
    time.sleep(2)

    # 領取瓦特
    ctr.A()
    ctr.A()
    ctr.A()

    print("成功領取 2000W")


if __name__ == "__main__":
    ctr = Controller()

    ctr.A()
    time.sleep(2)

    WattCollect()