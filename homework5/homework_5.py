# 1
print("fulfill the file")
with open("user_file.txt", "w", encoding="utf-8") as f:
    s = input()
    while s != "":
        print(s, file=f)
        s = input()
# 2
with open("user_file.txt", "r", encoding="utf-8") as f:
    print(f"Number of strings is: {len(f.readlines())}")
    f.seek(0)
    s = 0
    for i in f:
        s = s + len(i.split())
    print(f"Number of words is: {s}")
# 3
from random import randrange

with open("user_file.txt", "w+", encoding="utf-8") as f:
    for i in range(1, 11):
        print(f"Иванов #{i}  {randrange(5000, 30000, 1000)}", file=f)
        print(i)
    f.seek(0)
    sr = 0
    k = 0
    for i in f:
        s = i.split()
        if float(s[2]) < 20000:
            print(' '.join(s[0:2]))
        sr = sr + float(s[2])
        k += 1
    print(f"Average salary is: {sr / k:.2f}")
# 4
try:
    with open("text_4.txt", "r", encoding="utf-8") as f:
        f2 = open("text_4_new.txt", 'w', encoding="utf-8")
        key1 = ['one', 'two', 'three', 'four']
        key2 = ['1', '2', '3', '4']
        for i in f:
            s = i.split()
            if s[0].lower() in key1:
                s[0] = key2[key1.index(s[0].lower())]
            f2.writelines(" ".join(s) + '\n')
        f2.close()
except IOError:
    print("File not found")

# 5
print("input a string of numbers")
with open("user_file2.txt", 'w+', encoding='utf-8') as f:
    f.writelines(input())
    f.seek(0)
    try:
        s = f.readline().split()
        for i in range(len(s)):
            s[i] = float(s[i])
        print(f'summary = {sum(s)}')
    except TypeError:
        print('This is not a number')
# 6
try:
    with open("text_6.txt", 'r', encoding="utf-8") as f:
        key = {}
        for i in f:
            s = i
            s = s.replace('(л)', ' ')
            s = s.replace('(пр)', ' ')
            s = s.replace('(лаб)', ' ')
            s = s.replace('.', ' ')
            s = s.replace('-', ' ')
            s = s.split()
            for i in range(len(s) - 1):
                s[i + 1] = float(s[i + 1])
            key.update({s[0]: sum(s[1:len(s)])})
        print(key)
except IOError:
    print("File not found")
# 7
import json

try:
    with open("text_7.txt", 'r', encoding="utf-8") as f:
        f2 = open("text_7_new", 'w', encoding="utf-8")
        l = [{}, {}]
        av = 0
        j = 0
        for i in f:
            s = i.split()
            l[0].update({s[0]: (float(s[2]) - float(s[3]))})
            if (float(s[2]) - float(s[3])) > 0:
                av = av + (float(s[2]) - float(s[3]))
                j += 1
        l[1].update({'average profit': (av / j)})
        print(l)
        json.dump(l, f2)
        f2.close()
except IOError:
    print("File not found")
