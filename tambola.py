import random
import os
from termcolor import colored

nums = [i for i in range(1,91)]
cond = 0
lang = 1
print("Start")
print("Enter 4 for manual")
while nums:
    ans = "say "
    instr = input("Next:")
    if instr == '1':
        for i in range(0,90,10):
            for j in range(1,11):
                if i+j<10:
                    print("",end=' ')
                if i + j in nums:
                    print(i+j,end=' ')
                else:
                    print(colored(str(i+j),'red'),end=' ')
            print('')

        continue
        
    if instr == '2':
        if cond == 0:
            cond = 1 
        else:
            cond = 0
        continue

    if instr == '3':
        print("Select Language:")
        print("1. English")
        print("2. Hindi")
        print("3. French")
        print("Enter number(1:3):")
        lang = int(input())
        continue


    if instr == '4':
        print("------------Manual------------")
        print("' ' : Ask for next number")
        print("'1' : Show board (Red represents numbers which have been taken out)")
        print("'2' : To switch between speaking modes")
        print("'3' : To select language")
        print("'4' : Open manual")
        continue


    print(a:=random.choice(nums))
    if cond == 0:
        if a < 10:
            if lang == 1:
                os.system("say single number")
            elif lang == 2:
                os.system("say -v Lekha ekal sankhya")
            elif lang == 3:
                os.system("say -v Thomas Numero unique")
        else:
            temp = str(a)
            dig1 = "say " 
            dig2 = "say "
            if lang == 2:
                dig1 += "-v Lekha "
                dig2 += "-v Lekha "

            if lang == 3:
                dig1 += "-v Thomas "
                dig2 += "-v Thomas "

            dig1 += str(temp[0])
            dig2 += str(temp[1])
            os.system(dig1)
            os.system(dig2)

    if lang == 2:
        ans += "-v Lekha "

    if lang == 3:
        ans += "-v Thomas "

    ans += str(a)
    os.system(ans)
    nums.remove(a)

