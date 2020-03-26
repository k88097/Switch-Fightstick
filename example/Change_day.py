from NXController import Controller
import time, datetime


# 過日
def change_day(ctr, isSaved, current_date):
    tommorrow = current_date + datetime.timedelta(days=1)

    if isSaved:
        # 第一次進入點選時間
        # 過日，點選時間
        ctr.A()

        #跳到 "日"，並且加一天
        ctr.r(0.05)
        ctr.r(0.05)
        ctr.u(0.05)

        # 當年的最後一天
        if current_date.month == 12 and current_date.day == 31:
            #加 年月日
            for i in range(2):
                ctr.l(0.05)
                ctr.u(0.05)
            ctr.A(0.05)
            ctr.A(0.05)
        # 月份最後一天
        elif not current_date.month == tommorrow.month:
            #加 月日
            ctr.l(0.05)
            ctr.u(0.05)
            ctr.A(0.05)

        ctr.A(0.05)
        ctr.A(0.05)
        ctr.A(0.05)
        ctr.A()
        isSaved = False

    else:
        # 點選時間
        ctr.A()

        # 加一天
        for i in range(3):
            ctr.l(0.05)
        ctr.u(0.05)

        # 當年最後一天
        if current_date.month == 12 and current_date.day == 31:
            for i in range(2):
                ctr.l(0.05)
                ctr.u(0.05)
            ctr.A(0.05)
            ctr.A(0.05)
        # 當月最後一天
        elif not current_date.month == tommorrow.month:
            ctr.l(0.05)
            ctr.u(0.05)
            ctr.A(0.05)

        ctr.A(0.05)
        ctr.A(0.05)
        ctr.A(0.05)
        ctr.A()

    return isSaved, tommorrow


# 自動存檔
def save(isSaved):
    # 回主畫面與遊戲
    ctr.h()
    time.sleep(1)
    ctr.h()
    time.sleep(1.6)

    # 存檔，並且回到主畫面
    print("[*] 存檔中...")
    ctr.X()
    time.sleep(0.6)
    ctr.R()
    time.sleep(1)
    ctr.A()
    time.sleep(3.2)
    print("[*] 存檔完畢。")
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

    print("{}搜尋控制器{}".format("=" * 5, "=" * 5))
    ctr.LR()

    year, month, day = [
        int(i) for i in input("輸入目前日期 (YYYY.MM.DD):").split('.')
    ]
    count, goal = 0, int(input("輸入天數："))
    # 當前日期轉為datetime格式
    current_date = datetime.datetime(year, month, day)
    isSaved = True

    print("{}開始執行程式{}".format("=" * 5, "=" * 5))
    print("[%s] 刷時間中..." % time.strftime("%H:%M:%S", time.localtime()))

    # isSaved = save(isSaved)

    while count < goal:
        count += 1

        isSaved, current_date = change_day(ctr, isSaved, current_date)
        if count % 30 == 0 and not count == goal:
            print("[%s] 還剩下 %d 天。" %
                  (time.strftime("%H:%M:%S", time.localtime()),
                   (goal - count)))

        # 每300天回去存檔一次
        if count % 300 == 0:
            time.sleep(1)
            isSaved = save(isSaved)

    print("[%s] 已達目標天數。" % time.strftime("%H:%M:%S", time.localtime()))

    ctr.close()
