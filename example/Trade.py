from NXController import Controller
import time


def Trade(ctr, count, goal):
    print("[{}] 第{}隻，準備傳送。".format(time.strftime("%H:%M:%S", time.localtime()),
                                   count))

    ctr.A()
    time.sleep(0.8)
    ctr.A()
    time.sleep(3.6)
    print("[{}] 開始傳送...".format(time.strftime("%H:%M:%S", time.localtime())))
    ctr.A()
    time.sleep(45)

    if count % 5 != 0 and not count == goal:
        ctr.d()
        time.sleep(0.5)
    elif count % 30 == 0:
        # 一箱交易結束
        ctr.R()
        for i in range(4):
            ctr.u()
        for i in range(5):
            ctr.l()
    else:
        for i in range(4):
            ctr.u()
            # time.sleep(0.4)
        ctr.r()
        time.sleep(0.5)

    print("[{}] 第 {} 隻傳送完畢。".format(
        time.strftime("%H:%M:%S", time.localtime()), count))


def getGoal():
    goal = int(input("傳送幾隻："))

    if goal <= 0:
        print("請再輸入一次。")
        getGoal()

    return goal


if __name__ == "__main__":
    ctr = Controller()

    print("{}搜尋控制器{}".format('=' * 5, '=' * 5))
    ctr.Y()

    count, goal = 0, getGoal()

    print("{}開始執行程式{}".format('=' * 5, '=' * 5))
    print("{}開始進行交易{}".format('=' * 5, '=' * 5))
    while count < goal:
        count += 1
        Trade(ctr, count, goal)
    print("交易結束")
    ctr.close()