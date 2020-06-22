# 1
class date:
    def __init__(self, s):
        self.s = s
        self.check(self.change(self.s))

    @classmethod
    def change(cls, s):
        try:
            s2 = list(map(int, s.split('-')))
        except ValueError:
            print('this is not a numbers')
            return [0, 0, 0]
        else:
            return s2

    @staticmethod
    def check(s):
        if s[0] in range(1, 32, 1):
            if s[1] in range(1, 13, 1):
                if s[2] in range(2000, 2100, 1):
                    print(f"day: {s[0]}, month: {s[1]}, year: {s[2]}")
                else:
                    print("wrong year")
            else:
                print("wrong month")
        else:
            print("wrong day")


a = date(input("input a date: "))


# 2
class del0(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    if b == 0:
        raise del0("do not delete on zero")
except ValueError:
    print('this is not a number')
except del0 as err:
    print(err)
else:
    print(a / b)


# 3
class err2(Exception):
    def __init__(self, txt):
        self.txt = txt


l = []
while True:
    try:
        s = input("input a number: ")
        if s != "stop":
            if not s.isnumeric():
                raise err2("this is not a correct number!")
        else:
            break
    except err2 as er:
        print(er)
    else:
        l.append(int(s))
print(f"this is your list of numbers: {l}")


# 4 - 6
class warehouse:
    stock = {"printer": 0, "scanner": 0, "xerox": 0}
    stock_assets = {"printer": 0, "scanner": 0, "xerox": 0}
    menuu = ['printer', 'scanner', 'xerox']

    @staticmethod
    def navi():
        while True:
            print("type the number according to the menu below: ")
            print("1 - add a tech")
            print("2 - move to warehouse")
            print("3 - move to store")
            print("4 - stop the program")
            print("5 - show the quantity")
            ch1 = input()
            while ch1 not in ['1', '2', '3', '4', '5']:
                print("wrong input")
                ch1 = input()
            if ch1 == '1':
                print("what tech you want to add?")
                print("1 - printer")
                print("2 - scanner")
                print("3 - xerox")
                print("4 - go back to the menu")
                ch2 = input()
                while ch2 not in ['1', '2', '3', '4']:
                    print("wrong input")
                    ch2 = input()
                if ch2 != '4':
                    print(f"input the quantity of {warehouse.menuu[int(ch2) - 1]} you want to add: ")
                    ch3 = input()
                    while not ch3.isnumeric():
                        print("wrong input")
                        ch3 = input()
                    if ch2 == '1':
                        printer(int(ch3))
                    elif ch2 == '2':
                        scanner(int(ch3))
                    elif ch2 == '3':
                        xerox(int(ch3))
                else:
                    continue
            elif ch1 == '2':
                warehouse.to_stock()
            elif ch1 == '3':
                warehouse.from_stock()
            elif ch1 == '4':
                break
            elif ch1 == '5':
                print(f"warehouse quantity: {warehouse.stock.items()}")
                print(f"warehouse assets: {warehouse.stock_assets.items()}")
                print(f"stock quantity: {tech.quan.items()}")
                print(f"stock assets: {tech.assets.items()}")

    @staticmethod
    def to_stock():
        for i in tech.quan.keys():
            warehouse.stock[i] += tech.quan[i]
            warehouse.stock_assets[i] += tech.assets[i]
            tech.quan[i] = 0
            tech.assets[i] = 0

    @staticmethod
    def from_stock():
        for i in tech.quan.keys():
            tech.quan[i] += warehouse.stock[i]
            tech.assets[i] += warehouse.stock_assets[i]
            warehouse.stock_assets[i] = 0
            warehouse.stock[i] = 0


class tech:
    quan = {"printer": 0, "scanner": 0, "xerox": 0}
    assets = {"printer": 0, "scanner": 0, "xerox": 0}

    @staticmethod
    def quantity(s):
        tech.quan[s[0]] += s[1]
        tech.assets[s[0]] += s[2] * s[1]


class printer(tech):
    def __init__(self, kol, price=1000):
        self.kol = kol
        self.price = price
        tech.quantity(['printer', self.kol, self.price])


class scanner(tech):
    def __init__(self, kol, price=1500):
        self.kol = kol
        self.price = price
        tech.quantity(['scanner', self.kol, self.price])


class xerox(tech):
    def __init__(self, kol, price=900):
        self.kol = kol
        self.price = price
        tech.quantity(['xerox', self.kol, self.price])


warehouse.navi()


# 7
class compl:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return compl(self.a + other.a)

    def __mul__(self, other):
        return compl(self.a * other.a)

    def __str__(self):
        return str(self.a)


k1 = compl(complex(float(input("input first real part:")), float(input("input first imaginary part:"))))
k2 = compl(complex(float(input("input second real part:")), float(input("input second imaginary part:"))))
print(f"k1 = {k1} ; k2 = {k2}")
print(f"k1 + k2 = {k1 + k2}")
print(f"k1 * k2 = {k1 * k2}")
