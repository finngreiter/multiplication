from random import *
import os
import time

os.system('clear')

tto = input("What would you like to practice? (2s, 4s, etc...): ")

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
shuffle(list_of_numbers)
# print(list_of_numbers)
# input()
score = 12
num1 = 0
num2 = 0
time_1 = 0
together = 0
answer = ""
cori = "Begin:"
finndex = 0

for i in range(12):
    t0 = time.time()
    os.system("clear")
    print(cori)
    num1 = list_of_numbers[finndex]
    finndex += 1
    num2 = int(tto)
    together = num1 * num2
    answer = input(str(num1) + " X " + str(num2) + " = ")
    t1 = time.time()
    if int(answer) == together:
        cori = "Correct!"
    else:
        cori = "Incorrect, " + str(num1) + " X " + str(num2) + " = " + str(num1 * num2)
        score -= 1
    # print("That took you " + str(round(t1-t0)) + "s")
    time_1 += round(t1-t0)
    # input("press ENTER")

os.system("clear")

print("Score: " + str(score) + "/12")
print("Time: " + str(time_1) + "s")