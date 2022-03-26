from itertools import permutations

NUMS = [1,2,6,6,11,20]
OPERATORS = ["+" , "-","/","*"]
TARGET = 690

nums_permed = list(permutations(NUMS))
print(nums_permed)


def operation(opp , a, b):
    if opp == "+":
        return a +b
    if opp == "-":
        return a -b
    if opp == "/":
        return a/b
    if opp == "*":
        return a*b




def pop_append(arr , remove , add):
    arr.remove(remove)
    arr.insert(0,add)



def summle(perms):
    for i in range(len(perms)):


