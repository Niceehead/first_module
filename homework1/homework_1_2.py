print("Choose a game you want to play")
print("1 - my own game")
print("2 - how much time?")
print("3 - n+nn+nnn")
print("4 - cut the numbers")
print("5 - profit and losses")
print("6 - how tough do you want to be?")
choice = input()
if choice == "1":
    name = input("Give me your name, stranger\n")
    print("Guess my number from 0 to 10")
    i = 1
    while input() != "3.0":
        print("Wrong, you silly")
        if i >= 5:
            print('Maybe, 3?')
        else:
            i += 1
    print(f"Congrats, {name:<20}. You've won {3 / 9:.5f} cents!")  # форматирование2 с f-строками
elif choice == "2":
    hours = 0
    min = 0
    print("how long did you need to understand my code")
    a = int(input())
    hours = a // 3600
    min = (a - hours * 3600) // 60
    sec = (a - hours * 3600 - min * 60)
    print(f"So... You needed {hours}:{min}:{sec} ... Kinda long, don't you think?")
elif choice == "3":
    a = input("Give me a number\n")
    print("n+nn+nn=", int(a) + int(a * 2) + int(a * 3))
elif choice == "4":
    a = int(input("Let's cut your numbers!\n"))
    b = 0
    while a != 0:
        if b < (a % 10):
            b = a % 10
        a = a // 10
    print("that's the greatest number of yours: ", b)
elif choice == "5":
    a = int(input('Give me your revenue: '))
    b = int(input("Give me your looses: "))
    if a > b:
        c = (a-b) / b * 100
        print(f"Good for you :) ROI: {c:.2f} %")
        c = int(input("how much workers do you have?\n"))
        print(f"Your gift for every worker is: {(a-b) / c:.2f}")
    else:
        print("Too bad for ya")
elif choice == "6":
    a = float(input("give me your best day record, baby!"))
    b = float(input("what about your future results?"))
    i = 1
    while a < b:
        a = a * 1.1
        i += 1
    print(f"days: {i}")
else:
     print("ok. Just quit then")
