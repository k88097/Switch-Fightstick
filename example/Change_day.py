from NXController import Controller
import time


# 過日
def change_day(isSaved):
    c = 0

    if isSaved:
        c += 1
        # 第一次過日
        # 過日，點選時間
        ctr.A()

        #跳到 "日"，並且加一天
        ctr.r(0.05)
        ctr.r(0.05)
        ctr.u(0.05)
        ctr.A(0.05)
        ctr.A(0.05)
        ctr.A(0.05)
        ctr.A()

        isSaved = False
        # time.sleep(0.3)

    while c < 31:
        c += 1
        # 快速過日
        ctr.A()
        # time.sleep(0.1)
        ctr.l(0.05)
        ctr.l(0.05)
        ctr.l(0.05)
        ctr.u(0.05)
        ctr.A(0.05)
        ctr.A(0.05)
        ctr.A(0.05)
        ctr.A()
        # time.sleep(0.3)
    return isSaved


# 自動存檔
def save(isSaved):
    # 回主畫面與遊戲
    ctr.h()
    time.sleep(1)
    ctr.h()
    time.sleep(1.6)

    # 存檔，並且回到主畫面
    print("存檔中...")
    ctr.X()
    time.sleep(0.6)
    ctr.R()
    time.sleep(1)
    ctr.A()
    time.sleep(3.2)
    print("存檔完畢")
    ctr.h()
    time.sleep(0.3)

    # 到設定畫面
    ctr.d()
    ctr.r()
    ctr.r()
    ctr.r()
    ctr.r()
    ctr.A()
    time.sleep(0.3)

    # 到設定時間畫面
    # print("到設定時間畫面")
    ctr.d(1.8)
    ctr.A()
    ctr.d()
    ctr.d()
    ctr.d()
    ctr.d()
    ctr.A()

    #到調整時間選項
    ctr.d(0.6)

    isSaved = True
    return isSaved


if __name__ == "__main__":
    ctr = Controller()

    goal = int(input("輸入天數："))
    count = 0
    isSaved = True

    print("{}搜尋控制器{}".format("=" * 5, "=" * 5))
    ctr.LR()
    time.sleep(2)

    print("{}開始執行程式{}".format("=" * 5, "=" * 5))
    print("[%s] 刷時間中..." % time.strftime("%H:%M:%S", time.localtime()))

    # isSaved = save(isSaved)

    while count < goal:
        count += 30

        isSaved = change_day(isSaved)
        if not count == goal:
            print("[%s] 還剩下 %d 天。" %
                  (time.strftime("%H:%M:%S", time.localtime()),
                   (goal - count)))

        # 每300天回去存檔一次
        if count % 300 == 0:
            time.sleep(1.5)
            isSaved = save(isSaved)

    print("[%s] 已達目標天數。" % time.strftime("%H:%M:%S", time.localtime()))

    ctr.close()
