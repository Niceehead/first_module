print("Choose one of the tasks")
print("1 - check the TYPE")
print("2 - make your list")
print("3 - guess the month")
print("4 - type your string")
print("5 - make your list")
print("6 - products")
choice = input()
li = [123, "qwerty", 3.9213, True, [1, 2], {1, 2, 3}, (1, 2, 3,), {123: 1, 234: 2}]
if choice == "1":
    print("li = ", li)
    for ind, el in enumerate(li, 1):
        print(ind, el, type(el))
elif choice == "2":
    print('Input a list via space. Don"t use space in list and other stuff like that')
    li = input().split()
    li2 = list()
    for i in range(len(li)):
        if ('[' in li[i]) and (']' in li[i]):
            li3 = li[i][1:len(li[i]) - 1].split(',')
            li4 = list()
            for j in range(len(li3)):
                if li3[j].isnumeric():
                    li4.append(int(li3[j]))
                elif '.' in li3[j]:
                    print(li3[j])
                    li4.append(float(li3[j]))
                elif 'True' in li3[j]:
                    li4.append(True)
                elif 'False' in li3[j]:
                    li4.append(False)
                else:
                    li4.append(li3[j])
            li2.append(li4)
        elif li[i].isnumeric():
            li2.append(int(li[i]))
        elif '.' in li[i]:
            li2.append(float(li[i]))
        elif 'True' in li[i]:
            li2.append(True)
        elif 'False' in li[i]:
            li2.append(False)
        else:
            li2.append(li[i])
    print('your list is: ', li2)
    for i in range(len(li2) - 1):
        if (i % 2) == 0:
            t = li2[i]
            li2[i] = li2[i + 1]
            li2[i + 1] = t
    print('your changed list is:', li2)
elif choice == '3':
    t = int(input("Enter the month: "))
    li = ["Winter", 'Spring', 'Summer', 'Autumn']
    li2 = {1: "Winter", 2: "Winter", 3: "Winter", 4: "Spring", 5: "Spring", 6: "Spring", 7: "Summer", 8: "Summer",
           9: "Summer", 10: "Autumn", 11: "Autumn", 12: "Autumn"}
    print('it"s :', li[((t - 1) // 3)])
    print("it's :", li2.get(t))
elif choice == '4':
    t = input("Type the string").split()
    for ind, el in enumerate(t, 1):
        print(ind, el[:10])
elif choice == '5':
    li = input("input a list with numbers: ").split()
    li2 = list()
    for i in range(len(li)):
        if li[i].isnumeric():
            li2.append(int(li[i]))
    for i in range(len(li2)):
        t = -1
        ind = -1
        for j in range(len(li2) - i):
            if li2[j + i] > t:
                t = li2[j + i]
                ind = j + i
        if ind != -1:
            li2[ind] = li2[i]
            li2[i] = t
    print("your list is: ", li2)
    k = int(input("please enter the number you want to insert: "))
    li2.append(k)
    for i in range(len(li2)):
        t = -1
        ind = -1
        for j in range(len(li2) - i):
            if li2[j + i] > t:
                t = li2[j + i]
                ind = j + i
        if ind != -1:
            li2[ind] = li2[i]
            li2[i] = t
    print("that's your new list: ", li2)
elif choice == "6":
    t = int(input("quantity of products: "))
    tt = int(input("quantity of characteristics: "))
    i = 1
    li = list()
    di2 = {}
    while i <= t:
        di = {}
        j = 1
        print(f'начнём заполнение товара № {i} !')
        while j <= tt:
            dic1 = input("введите название характеристики: ")
            dic2 = input('введите значение характеристики: ')
            dic = {dic1: dic2}
            di.update(dic)
            if di2.get(dic1):
                di2.get(dic1).append(dic2)
            else:
                di2.update({dic1: [dic2]})
            j += 1
        di = (i, di)
        li.append(di)
        i += 1
    print(li)
    di = di2
    for i in range(len(di2)):
        print(di2.popitem())
