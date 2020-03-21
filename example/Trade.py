from NXController import Controller
import time


def Trade(goal):
    count = 0
    while count < goal:
        count += 1
        print("第{}隻，傳送中...".format(count))

        ctr.A()
        time.sleep(0.8)
        ctr.A()
        time.sleep(3.6)
        ctr.A()
        time.sleep(40)

        if count % 5 != 0:
            ctr.d()
            time.sleep(0.5)
        elif count % 30 == 0:
            # 一箱交易結束
            ctr.r()
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
        
        print("第 %d 隻傳送完畢。")


def getGoal():
    _range = []
    for i in range(1, 31):
        _range.append(i)

    goal = int(input("傳送幾隻(一次最多30隻)："))
    if not goal in _range:
        print("請再輸入一次。 (範圍 1 ~ 30)")
        getGoal()
    return goal


if __name__ == "__main__":
    ctr = Controller()
    goal = getGoal()

    print("{}搜尋控制器{}".format("=" * 5, "=" * 5))
    ctr.Y()
    time.sleep(2)

    print("{}開始執行程式{}".format("=" * 5, "=" * 5))
    print("開始進行交易，一次以一箱為單位")
    Trade(goal)
    print("交易結束")
    ctr.close()