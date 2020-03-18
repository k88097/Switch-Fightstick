from NXController import Controller
import time


# 過日
def change_day():
    pass

# 自動存檔
def save():
    pass


if __name__ == "__main__":
    ctr = Controller()

    goal = int(input("輸入天數："))
    count = 0

    print("{}搜尋控制器{}".format("=" * 5, "=" * 5))
    ctr.LR()
    time.sleep(2)

    print("{}開始執行程式{}".format("=" * 5, "=" * 5))

    while count < goal:
        count += 1
        change_day()

        # 每300天回去存檔一次
        if count % 300 == 0:
            time.sleep(1.8)
            save()

    ctr.close()