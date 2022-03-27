from itertools import permutations
from itertools import product


NUMS = [4,5,5,7,8,25]
OPERATORS = ["+" , "-","/","*"]
TARGET = 692

opers_permed = list(map(list, product(OPERATORS, repeat=5)))

nums_permed = list(permutations(NUMS))



def operation(opp , a, b):
    return eval(str(a) + opp + str(b))


print(operation(OPERATORS[2],NUMS[0],NUMS[1]))



def pop_append(arr , a,b , add):
    arr.remove(a)
    arr.remove(b)
    arr.insert(0,add)

cnt =0
for oppers in opers_permed:
    temp = NUMS
    cnt = cnt +1
    for i in range(len(oppers)):
        print(oppers)
        print(temp)
        a = temp[0]
        b = temp[1]
        res = operation(oppers[i],a,b)
        pop_append(temp,a,b,res)
        if len(temp) == 1:
            print(str(temp) + " : " + str(cnt))
            print("HUHHUH")
    break




