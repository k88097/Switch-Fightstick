from NXController import Controller
import time


# 瓦特收集
def WattCollect(count):
    # 站在洞前
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
    time.sleep(0.3)

    # 到設定時間畫面
    ctr.d(1.8)
    ctr.A()
    ctr.d()
    ctr.d()
    ctr.d()
    ctr.d()
    ctr.A()

    #到調整時間選項
    ctr.d(0.6)
    ctr.A()

    #調整時間加一天
    ctr.r()
    ctr.r()
    ctr.u()
    ctr.r()
    ctr.r()
    ctr.r()
    ctr.A()

    # 回到主畫面並且進入遊戲
    # print("回到主畫面並且進入遊戲")
    ctr.h()
    time.sleep(1)
    ctr.h()
    time.sleep(1)

    # 退出招募
    # print("退出招募")
    ctr.A()
    time.sleep(4.3)

    # 領取瓦特
    # print("領取瓦特")
    ctr.A()
    time.sleep(0.3)
    ctr.A()
    time.sleep(0.3)
    ctr.A()
    time.sleep(0.3)
    print("[%d] 領取 2000w" % count)

# 存檔
def save():
    print("存檔中...")
    ctr.B()
    time.sleep(1.5)
    ctr.X()
    time.sleep(0.6)
    ctr.R()
    time.sleep(1)
    ctr.A()
    time.sleep(3.2)
    print("存檔完畢")
    ctr.A()


if __name__ == "__main__":
    ctr = Controller()

    goal = int(input("輸入次數："))
    count = 0

    print("{}搜尋控制器{}".format("=" * 5, "=" * 5))
    ctr.LR()
    time.sleep(2)

    print("{}開始執行程式{}".format("=" * 5, "=" * 5))
    while (count < goal):
        count += 1
        WattCollect(count)

    time.sleep(1.8)
    save()

    ctr.close()