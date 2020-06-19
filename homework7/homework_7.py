# 1
"""
class matrix:
    def __init__(self):
        try:
            self.l1 = []
            l2 = []
            self.m = int(input("input row quantity: "))
            self.n = int(input("input column quantity: "))
            s = input(f"input {self.m * self.n} numbers via space: ")
            while len(s.split()) != self.m * self.n:
                s = input(f"input {self.m * self.n} numbers via space: ")
            k = 0
            for i in range(1, self.m + 1, 1):
                for j in range(1, self.n + 1, 1):
                    l2.append(int(s.split()[k]))
                    k += 1
                self.l1.append(l2)
                l2 = []
                print(self.l1[i - 1])
        except ValueError:
            print("this is not a number")

    def __str__(self):
        print("this is how your matrix looks like:")
        for i in range(0, self.m, 1):
            for j in range(0, self.n, 1):
                print(f"{self.l1[i][j]:4}", end='') #можно использовать \t - табуляция
            print()
        return ''

    def __add__(self, other):
        if (self.m == other.m)and(self.n == other.n):
            l2 = self.l1
            print("this is a new matrix: ")
            for i in range(0, self.m, 1):
                for j in range(0, self.n, 1):
                    l2[i][j] = self.l1[i][j] + other.l1[i][j]
                    print(f"{l2[i][j]:4}", end='')
                print()
            return ''
        else:
            return "matrix are not equal"

a = matrix()
b = matrix()
print(a + b)
"""
# 2
from abc import ABC, abstractmethod


class clothes(ABC):
    @abstractmethod
    def __init__(self, param):
        pass


class coat(clothes):
    def __init__(self, v):
        self.v = float(v)
        self.s1 = self.v / 6.5 + 0.5
        print(f"tissue consumption on coat = {self.s1:.2f}")

    @property
    def meth2(self):
        return 'something happens'


class suit(clothes):
    def __init__(self, h):
        self.h = float(h)
        self.s2 = 2 * self.h + 0.3
        print(f"tissue consumption on suit = {self.s2:.2f}")


a = coat(10)
b = suit(1)
print(a.meth2)
print(f" this is a summ: {a.s1 + b.s2:.2f}")


# 3
class cell:
    def __init__(self, k):
        self.k = k

    def __add__(self, other):
        return cell(self.k + other.k)

    def __sub__(self, other):
        if self.k >= other.k:
            return cell(self.k - other.k)
        else:
            return "can't sub this cells"

    def __mul__(self, other):
        return cell(self.k * other.k)

    def __truediv__(self, other):
        return cell(self.k // other.k)

    def __str__(self):
        return str(self.k)

    def make_order(self, kk):
        i = 1
        while i <= self.k:
            for j in range(0, kk, 1):
                print("*", end='')
                i += 1
                if i > self.k:
                    break
            print()


a = cell(8)
b = cell(2)
print(f"a+b= {a + b}; a-b= {a - b}; a*b= {a * b}; a / b = {a / b}")
a.make_order(3)
