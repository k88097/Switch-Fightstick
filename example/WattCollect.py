from NXController import Controller
import time
import datetime


# 瓦特收集
def WattCollect(ctr, current_date):
    tommorrow = current_date + datetime.timedelta(days=1)

    # 站在洞前
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
    ctr.d(0.05)
    ctr.d(0.05)
    ctr.A()

    # 調整時間加一天
    if current_date.month == 12 and current_date.day == 31:
        for i in range(3):
            ctr.u(0.05)
            ctr.A(0.05)
    elif not current_date.month == tommorrow.month:
        ctr.A(0.05)
        for i in range(2):
            ctr.u(0.05)
            ctr.A(0.05)
    else:
        ctr.A(0.05)
        ctr.A(0.05)
        ctr.u(0.05)
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
    print("[%d] 領取 2000w" % count)
    return tommorrow


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
    time.sleep(1)


if __name__ == "__main__":
    ctr = Controller()

    print("{}搜尋控制器{}".format("=" * 5, "=" * 5))
    ctr.LR()

    year, month, day = [
        int(i) for i in input("輸入目前日期 (YYYY.MM.DD):").split('.')
    ]
    count, goal = 0, int(input("輸入次數："))
    # 當前日期轉為datetime格式
    current_date = datetime.datetime(year, month, day)
    isSaved = True

    print("{}開始執行程式{}".format("=" * 5, "=" * 5))
    while count < goal:
        count += 1
        current_date = WattCollect(ctr, current_date)

        if count % 100 == 0:
            time.sleep(1.8)
            save()

    if not count % 100 == 0:
        time.sleep(1.8)
        save()

    ctr.close()