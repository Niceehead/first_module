def ch1(a, b):
    try:
        a = int(a)
        b = int(b)
        a = a / b
    except (ValueError):
        return "it's not an integer number"
    except ZeroDivisionError:
        return "you divide on zero"
    return a


def ch2(**kwargs):
    return kwargs


def ch4(a, b):
    try:
        a = float(a)
        b = int(b)
        c = a
        if b > 0:
            i = 1
            while i <= (b - 1):
                c = c * a
                i += 1
        elif b < 0:
            i = 1
            while i <= (abs(b) - 1):
                c = c * a
                i += 1
            c = 1 / c
        elif b == 0:
            c = 1
        return c
    except ValueError:
        return "It's not a digit"
    except ZeroDivisionError:
        return "you divide by zero"

def ch5(li):
    #return sum(int(args.split()))
    global s, k
    for ind, el in enumerate(li):
        if el == "#":
            k = 1
        else:
            try:
                s = s + float(el)
            except ValueError:
                print('It"s not a digit')
    return s

def ch6(li):
    for i in range(len(li)):
        li[i] = li[i].capitalize()
    return ' '.join(li)

print("Choose one of the tasks")
print("1 - division")
print("2 - people data")
print("3 - max summa")
print("4 - pow()")
print("5 - infinite summ")
print("6 - products")
choice = input()
if choice == "1":
    print(ch1(input("input first number: "), input("input second number: ")))
elif choice == "2":
    print("input all data about it: name, surname, birthday, city, email, telephone")
    print(ch2(имя=input(), фамилия=input(), год_рождения=input(), город_проживания=input(), email=input(),
              телефон=input()))
elif choice == "3":
    print('input 3 int numbers')
    print((lambda a=int(input()), b=int(input()), c=int(input()): max(a, b) + max(b, c))())
elif choice == "4":
    print(ch4(input("input a number: "), input("input a degree: ")))
elif choice == "5":
    print("enter the digits and you will get their sum. Input # to stop the program")
    s = 0
    k = 0
    while k != 1:
        li = input().split()
        print(ch5(li))
elif choice == "6":
    print(ch6(input("Input a string: ").split()))
    print(input("ещё раз - более простое решение:").title())