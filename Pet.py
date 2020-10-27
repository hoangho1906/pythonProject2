class Pet:
    def __init__(self, name = "", animal_type = "", age = 0 ):

        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, x):
        self.__name = x
    def get_name(self):
        return self.__name

    def set_animal_type(self, x):
        self.__animal_type = x
    def get_animal_type(self):
        return self.__animal_type

    def set_age(self, x):
        self.__age = x
    def get_age(self):
        return self.__age

newPet = Pet()
print("Type in your pet type: ")
newPet.name = input()
print("Type in your pet name: ")
newPet.animal_type = input()
print("Type in your pet age: ")
newPet.age = int(input())
print(f"your pet:{newPet.name} type:{newPet.animal_type} age:{newPet.age}")