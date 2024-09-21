import random 
import msvcrt

def dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    summ = dice1 + dice2
    return summ

#获取种子
seed = int(input("输入一个无符号整数作为种子："))
random.seed(seed)

#第一轮
sum_ = dice()
print("第一轮和为", sum_, sep = "")
if sum_ == 7 or sum_ == 11:
    print("你赢了！")
    print("按任意键结束游戏...")
    msvcrt.getch()
elif sum_ == 2 or sum_ == 3 or sum_ == 12:
    print("你输了！")
    print("按任意键结束游戏...")
    msvcrt.getch()
else:
    print("按任意键继续游戏...")
    msvcrt.getch()
    point = sum_
    while True:
        sum_ = dice()
        print("和为", sum_, sep="")
        if sum_ == point:
            print("你赢了！")
            print("按任意键结束游戏...")
            msvcrt.getch()
            break
        elif sum_ == 7:
            print("你输了！")
            print("按任意键结束游戏")
            msvcrt.getch()
            break
        print("按任意键继续游戏...")
        msvcrt.getch()

