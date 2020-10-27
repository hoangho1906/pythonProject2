class Car:

    def __init__(self, year_model = 0, make = "", speed =0):

        self.__year_model = year_model
        self.__make = make
        self.__speed = speed


    #def get_speed(self, x):
    #    self.__speed = x
    #def set_speed(self):
    #    print(f"Current speed:{self.__speed}")
    #    return self.__speed
    #def accelerate(self):

    @property
    def speed(self):  #getter
        print(f"current speed:".format(self.__speed))
        return self.__speed

    @speed.setter   #setter
    def speed(self, x):
        self.__speed = x

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

newCar = Car(1992,"Ford", 20)
i = 1
while i < 6:
    newCar.accelerate()
    print(newCar.speed)
    i+=1
    break