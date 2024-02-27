from random import randint
import time

def handle(player, money, computer):
    if (computer >= 3) and (computer <= 10):
        print(str(computer) + " - Xiu")
        if player == 2:
            money *= 0.9
            print("+" + str(int(money)))
            return money
        else:
            print("-" + str(int(money)))
            return -money
    else:
        print(str(computer) + " - Tai")
        if player == 1:
            money *= 0.9
            print("+" + str(int(money)))
            return money
        else:
            print("-" + str(int(money)))
            return -money

def player_input(money):
    print("Chon so tien cuoc:")
    print("-------------------------")
    print("|  1: 10.000            |")
    print("|  2: 20.000            |")
    print("|  3: 50.000            |")
    print("|  4: 100.000           |")
    print("|  5: 200.000           |")
    print("|  6: 500.000           |")
    print("|  7: 1.000.000         |")
    print("|  8: All in            |")
    print("|  9: Tu chon           |")
    print("-------------------------")
    while True:
        variable = int(input())
        if variable == 1:
            return 10000
        elif variable == 2:
            return 20000
        elif variable == 3:
            return 50000
        elif variable == 4:
            return 100000
        elif variable == 5:
            return 200000
        elif variable == 6:
            return 500000
        elif variable == 7:
            return 1000000
        elif variable == 8:
            return money
        elif variable == 9:
            while True:
                betting_money = int(input("Nhap so tien cuoc: "))
                if (betting_money <= money) and (betting_money > 0):
                    return betting_money
                else:
                    print("So tien cuoc khong hop le!")
        else:
            print("So tien cuoc khong hop le!")

def main():
    money = 500000
    print("So tien ban co: " + str(int(money)))
    while True:
        print("-------------------")
        print("|  1: Play        |")
        print("|  2: Out         |")
        print("-------------------")
        select = int(input())
        if select == 2:
            break
        elif select == 1:
            print("--------------------------")
            print("|  |1: Tai| - |2: Xiu |  |")
            print("--------------------------")
            variable = int(input())
            betting_money = player_input(money)
            print("Dang quay so!")
            time.sleep(4)
            computer = randint(3, 18)
            money += handle(variable, betting_money, computer)
            print("----------------")
            print("So tien ban co: " + str(int(money)))
            if money == 0:
                print("Ban da het tien!")
                break
        else:
            continue
main()