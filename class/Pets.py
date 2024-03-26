class Pets:
    def squeak(self):
        pass


class Dog(Pets):
    def __init__(self, moniker, age, sex, gender, sound):
        self.moniker = moniker
        self.age = age
        self.sex = sex
        self.gender = gender
        self.sound = sound
        self.type = "Собака"

    def squeak(self):
        return [self.moniker, self.age, self.sex, self.gender, self.sound, self.type]


class Cat(Pets):
    def __init__(self, moniker, age, sex, gender, sound):
        self.moniker = moniker
        self.age = age
        self.sex = sex
        self.gender = gender
        self.sound = sound
        self.type = "Кошка"

    def squeak(self):
        return [self.moniker, self.age, self.sex, self.gender, self.sound, self.type]


phrases = []


def create_pet(func):
    moniker = str(input("Ввелите кличку: "))
    age = int(input("Введите возраст: "))
    sex = str(input("Введите пол: "))
    gender = str(input("Введите гендер: "))
    sound = str(input("Введите звук, который оно издаёт: "))
    print()
    phrases.append(func(moniker, age, sex, gender, sound))

    choice()


def choice_pet():
    choice_func = {1: Dog, 2: Cat}
    create_pet(choice_func[int(input("Выберите кого вы хотите (1 - собака, 2 - кот): "))])


def choice():
    choice_func = {1: choice_pet, 2: output}
    choice_func[int(input("Выберите действие (1 - новое животное, 2 - вывести животных): "))]()


def output():
    for phrase in phrases:
        phrase = phrase.squeak()
        moniker_0, age_0, sex_0, gender_0, sound_0, type_0 = phrase[0], phrase[1], phrase[2], phrase[3], phrase[4], \
            phrase[5]
        print(f"\n{type_0} {moniker_0} возрастом {age_0}, пола {sex_0} и гендера {gender_0}, говорит: ", sound_0, "\n")
    choice()


choice()
