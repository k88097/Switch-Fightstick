from NXController import Controller
import time


# 瓦特收集
def WattCollect(year, month, day):
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
    ctr.d()
    ctr.d()
    ctr.A()

    if day == max_day[month - 1]:
        if month == 12:
            NextYear()
            year += 1
            month = 1
        else:
            NextMonth()
            month += 1
        day = 1
    else:
        # 一般模式
        NTime()

    # 回到主畫面並且進入遊戲
    print("回到主畫面並且進入遊戲")
    ctr.h()
    time.sleep(1)
    ctr.h()
    time.sleep(1)

    # 退出招募
    print("退出招募")
    ctr.A()
    time.sleep(4.3)

    # 領取瓦特
    print("領取瓦特")
    ctr.A()
    time.sleep(0.3)
    ctr.A()
    time.sleep(0.3)
    ctr.A()
    time.sleep(0.3)
    print("成功領取 2000W")

    def NTime():
        # 一般模式
        #調整時間加一天
        ctr.r()
        ctr.r()
        ctr.u()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.A()

    def NextMonth():
        # 下一個月模式
        #調整時間加一天
        ctr.r()
        ctr.u()
        ctr.r()
        ctr.u()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.A()

    def NextYear():
        # 下一年模式
        #調整時間加一天
        ctr.u()
        NextMonth()


if __name__ == "__main__":
    ctr = Controller()
    global year, month, day
    year, month, day = [
        int(i) for i in input("輸入目前日期\n按照此格式輸入2020.3.17 : ").split(".")
    ]

    print("{}搜尋控制器{}".format("=" * 5, "=" * 5))
    ctr.LR()
    time.sleep(2)

    print("{}開始執行程式{}".format("=" * 5, "=" * 5))
    while (True):
        global max_day
        max_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0:
            max_day[1] = 29
        WattCollect(year, month, day)
    ctr.close()