class Pet:

    def __init__(self, name, age, value):

        self.__name = name
        self.__age = None
        self.__sound = None
        self.__choice = value

        self.age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < int(age) < 40:
            self.__age = age
        else:
            print("НЕПРАВИЛЬНЫЙ ВВОД ВОЗРАСТА ДОМАШНЕЙ уТВАРИ")


class Type_of_pet(Pet):
    def choice(self):
        dictionary = {1: Cat, 2: Dog, 3: Naked_man}
        choicer = dictionary[self.__choice]


essence = Pet(str(input("Введите имя вашей твари: ")), int(input("Введите возраст тварюжечки: ")),
              int(input("Введите тип вашей твари (1 - Кошка, 2 - Собака, 3 - Голый землекоп): ")))
