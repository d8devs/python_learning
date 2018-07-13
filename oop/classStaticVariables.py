
class CarStaticVariable:
    price = "expensive"

auto = CarStaticVariable()
print(auto.price)
# without Class initialization but the variable is setted
print(CarStaticVariable.price)

class NormalCar:
    def __init__(self):
        self.price = "expensive"


anotherAuto = NormalCar()
print(anotherAuto.price)
