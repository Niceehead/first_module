# first
"""
from sys import argv
source, time, stake, prem = argv
print("ZP = ", (float(time)*float(stake))+float(prem))
"""
# second
li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([li[i + 1] for i in range(len(li) - 1) if li[i + 1] > li[i]])
# third
print([i for i in range(20, 241) if (i % 20 == 0) or (i % 21 == 0)])
# fourth
li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([i for i in li if li.count(i) < 2])


# five
def pro(list):
    s = 1
    for j in list:
        s = s * j
    return s


print(pro([i for i in range(100, 1001) if (i % 2 == 0)]))

# six
from itertools import count, cycle
for i in count(int(input())):
    if i > 100:
        break
    else:
        print(i)
j = 0
for i in cycle('qwerty'):
    if j < 10:
        j += 1
        print(i)
    else:
        break
#seven
def fact(n):
    j = 1
    for i in range(1,n+1):
        j = j*i
        yield j #создали список от 1 до n факториалов последовательно высчитывая конечный

print('input a number: ')
for i in fact(int(input())):
    print(i)
