from NXController import Controller
import time

ctr = Controller()

count = 0
goal = int(input("目標幾顆蛋："))

print("{}開始{}".format("=" * 10, "=" * 10))
while count < goal:
    count += 1
    print("目前第{}顆，剩餘{}顆達到目標。".format(count, goal - count))
    Egg()
print("已達目標數量，共{}顆蛋。".format(goal))

# 自動取蛋
def Egg():
    c = 0
    while c < 6:
        c += 1
        ctr.ls_u(2)
        ctr.ls_l(2)
        # sendCommand(s, "setStick LEFT -0x8000 0x7FFF")
        # time.sleep(2)
        ctr.ls_u(2)
        ctr.ls_r(2)
        # sendCommand(s, "setStick LEFT 0x7FFF 0x7FFF")
        # time.sleep(2)

    # sendCommand(s, "setStick LEFT 0x0000 0x0000")  #stop
    ctr.A(1)
    ctr.A(3.3)
    ctr.A(2)
    ctr.A(2)
    ctr.A()