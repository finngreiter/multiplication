from random import *
import os
import time

os.system('clear')

loops = input("How many problems would you like to solve?: ")
tto = input("What would you like to practice?: ")

score = int(loops)
num1 = 0
num2 = 0
time_1 = 0
together = 0
answer = ""

for i in range(int(loops)):
    t0 = time.time()
    os.system("clear")
    num1 = randint(1, 12)
    num2 = int(tto)
    together = num1 * num2
    answer = input(str(num1) + " X " + str(num2) + " = ")
    t1 = time.time()
    if int(answer) == together:
        print("Correct!")
    else:
        print("Incorrect, " + str(num1) + " X " + str(num2) + " = " + str(num1 * num2))
        score -= 1
    print("That took you " + str(round(t1-t0)) + "s")
    time_1 += round(t1-t0)
    input("press ENTER")

os.system("clear")

print("Score: " + str(score) + "/" + str(loops))
print("Time: " + str(time_1) + "s")