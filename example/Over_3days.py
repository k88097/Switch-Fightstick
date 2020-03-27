from NXController import Controller
import time, datetime


def over_3days(ctr, current_date, isFirst):
    # 如果不是第一次執行程式
    if not isFirst:
        Restart_game(ctr)

    for i in range(3):
        tommorrow = current_date + datetime.timedelta(days=1)

        # 極巨戰主頁
        ctr.A()
        time.sleep(2)
        ctr.B()
        time.sleep(0.5)

        # 到主畫面
        ctr.h()
        time.sleep(0.5)

        # 到設定畫面
        ctr.d(0.05)
        ctr.r(0.05)
        ctr.r(0.05)
        ctr.r(0.05)
        ctr.r(0.05)
        ctr.A(0.05)
        time.sleep(0.3)

        # 到設定時間畫面
        ctr.d(1.8)
        ctr.A()
        ctr.d(0.05)
        ctr.d(0.05)
        ctr.d(0.05)
        ctr.d(0.05)
        ctr.A()

        #到調整時間選項
        ctr.d(0.6)
        ctr.A()

        # 調整時間加一天
        ctr.A(0.05)
        ctr.A(0.05)
        ctr.u(0.05)
        if current_date.month == 12 and current_date.day == 31:
            for i in range(2):
                ctr.l(0.05)
                ctr.u(0.05)
            ctr.A(0.05)
            ctr.A(0.05)
        elif not current_date.month == tommorrow.month:
            ctr.l(0.05)
            ctr.u(0.05)
            ctr.A(0.05)
        ctr.A(0.05)
        ctr.A(0.05)
        ctr.A(0.05)
        # 按下確定
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
        time.sleep(0.4)

        current_date = tommorrow

    isFirst = False
    print("目前日期：%s" % current_date.strftime("%Y-%m-%d"))
    return current_date, isFirst


def Restart_game(ctr):
    # 關閉遊戲
    ctr.h()
    time.sleep(1)
    ctr.X()
    time.sleep(1)
    ctr.A()
    time.sleep(3)

    # 打開遊戲
    ctr.A()
    time.sleep(1)
    ctr.A()
    print("進入遊戲畫面")
    time.sleep(16)
    print("點擊A")
    ctr.A()
    time.sleep(9)
    print("進到遊戲")
    ctr.A()
    time.sleep(1)


def isAgain(isAgain):
    isAgain = True
    return isAgain


if __name__ == "__main__":
    ctr = Controller()
    isFirst = True
    isAgain = True

    print("{}搜尋控制器{}".format("=" * 5, "=" * 5))
    ctr.LR()

    year, month, day = [
        int(i) for i in input("輸入目前日期 (YYYY.MM.DD):").split('.')
    ]
    current_date = datetime.datetime(year, month, day)

    print("{}開始執行程式{}".format("=" * 5, "=" * 5))
    print("{}開始刷D點{}".format("=" * 5, "=" * 5))

    current_date, isFirst = over_3days(ctr, current_date, isFirst)

    while isAgain:
        ans = input("是否重刷 [Y/n]：")
        if len(ans) == 0:
            current_date, isFirst = over_3days(ctr, current_date, isFirst)
        else:
            ord_ans = ord(ans[:1])
            if ord_ans == 89 or ord_ans == 121:
                current_date, isFirst = over_3days(ctr, current_date, isFirst)
            else:
                ctr.close()
                isAgain = False
