from NXController import Controller
import time

ctr = Controller()

count = 0
goal = int(input("目標幾隻："))

print("{}開始{}".format("=" * 10, "=" * 10))
while count < goal:
    count += 1
    print("目前第{}隻，剩餘{}隻達到目標。".format(count, goal - count))
    Fossil()
print("已達目標數量，共{}隻。".format(goal))

#復活化石

def Fossil():
    ctr.A(1)
    # print("1. click A")
    ctr.A(1)
    # print("2. click A")
    ctr.A(1)
    # print("3. click A")
    ctr.A(1)
    # print("4. click A")
    ctr.A(1)
    # print("5. click A")
    ctr.A(5)
    # print("6. click A")
    ctr.A(1)
    # print("7. click A")
    ctr.A(1)
    # print("8. click A")
    ctr.A(1)
    # print("9. click A")
    ctr.A(5)
    # print("10. click A")
    ctr.A(2)
    # print("11. click A")
    ctr.A(2)
    # print("12. click A")
