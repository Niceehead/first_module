# 1
"""
from time import sleep


class TrafficLight:
    color = ["red", "yellow", "green"]

    def running(self):
        i = 0
        j = 1
        while True:
            if i % 2 == 0:
                print(self.color[i])
                sleep(7)
                i = i+j
            else:
                print(self.color[i])
                sleep(2)
                i = i+j
            if i <= 0 or i >= (len(self.color) - 1):
                j = j * (-1)


a = TrafficLight()
a.running()
"""

# 2
"""
class road:
    def __init__(self, length, width, consumption=25, thickness=1):
        try:
            self._length = float(length)
            self._width = float(width)
            self._consumption = float(consumption)
            self._thickness = float(thickness)
            # super.__init__(length, width, consumption, thickness)
            self.area()
        except ValueError:
            print("this is not a numbers")

    def area(self):
        return print(f"area = {self._length * self._width * self._consumption * self._thickness / 1000:.2f} ton")


print('input parameters of the road and the concrete:')
road(input("input length: "), input("input width: "), input("input concrete consumption: "),
     input("input road thickness: "))
"""

# 3
"""
class worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class position(worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname} {self.position}")

    def get_total_income(self):
        try:
            self._income = {"wage": float(self.wage), "bonus": float(self.bonus)}
            print(f"income = {self._income}")
        except ValueError:
            print("this is not a numbers!")


print("Give us an information about your worker:")
a = position(input("input name: "), input("input surname: "), input("input position: "), input("input wage: "),
             input("input bonus: "))
b =  position(input("input name: "), input("input surname: "), input("input position: "), input("input wage: "),
             input("input bonus: "))
a.get_full_name()
a.get_total_income()

b.get_full_name()
b.get_total_income()
"""

"""
# 4
class car:
    count = 0
    is_police = False

    def __init__(self, speed, color, name):
        try:
            self.speed = float(speed)
            self.color = color
            self.name = name
        except:
            print("incorrect input")

    def go(self):
        if car.count == 0:
            print(f"Let's go {self.color} {self.name}! Your speed now is {self.speed}.")
            car.count = 1
        else:
            print(f"You are already going! Your speed is increased by 10km/h!")
            self.speed += 10

    def stop(self):
        print("you stopped the car. BUSTED!")

    def turn(self, direction):
        self.direction = direction
        print(f"We turned to the {self.direction}")


class TownCar(car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Your speed {self.speed} is too high!")
        else:
            print(f"your speed is {self.speed}")


class WorkCar(car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Your speed {self.speed} is too high!")
        else:
            print(f"your speed is {self.speed}")


class SportCar(car):
    def show_speed(self):
        print(f"Your speed is {self.speed}!")


class PoliceCar(car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True
    def show_speed(self):
        print(f"Your speed is {self.speed}!")


print("Choose a car!\n1) Town car\n2) Sport car\n3) Work car\n4) Police car")
stp = 0
k = ["Town car", "Sport car", "Work car", "Police car"]
ch = 0
while ch not in range(1, 5, 1):
    try:
        ch = int(input("You need to choose 1-4: "))
    except:
        pass
print(f"Okay. You've chosen {k[ch - 1]}. Now give us a parameters of the car")
if ch == 1:
    a = TownCar(input("input your speed at the start: "), input("input car's color: "), input("input car's name: "))
elif ch == 2:
    a = SportCar(input("input your speed at the start: "), input("input car's color: "),
                 input("input car's name: "))
elif ch == 3:
    a = WorkCar(input("input your speed at the start: "), input("input car's color: "), input("input car's name: "))
else:
    a = PoliceCar(input("input your speed at the start: "), input("input car's color: "),
                  input("input car's name: "))
print("Now it's your turn to rule! Tell me what do you want to do:")
print("'GO' - to start moving or to increase the speed by 10km/h")
print("'STOP' - to stop moving")
print("'TURN LEFT/RIGHT' - to turn the car")
print("'SPEED' - to show actual speed")
while True:
    s = input()
    if 'go' in s.lower():
        a.go()
    elif 'stop' in s.lower():
        a.stop()
        break
    elif ('turn' in s.lower()) and (len(s.split()) == 2) and (s.split()[1].lower() in ['right', 'left']):
        a.turn(s.split()[1])
    elif 'speed' in s.lower():
        a.show_speed()
    else:
        print('incorrect input. Try again')
"""


# 5
class Stationery:
    def __init__(self, title):
        self.title = title
        if self.title.lower() in ['pen', 'pencil', 'handle']:
            self.draw()
            if self.title.lower() in 'pen':
                Pen.draw(self)
            elif self.title.lower() in 'pencil':
                Pencil.draw(self)
            elif self.title.lower() in 'handle':
                Handle.draw(self)
        else:
            print("wrong input")
    def draw(self):
        print("start drawing")


class Pen(Stationery):
    def draw(self):
        print("draw by pen")


class Pencil(Stationery):
    def draw(self):
        print("draw by pencil")


class Handle(Stationery):
    def draw(self):
        print("draw by handle")

Stationery(input("print drawing method: "))