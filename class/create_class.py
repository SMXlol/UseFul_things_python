


class create_machine:
    def __init__(self):
        self.__tittle = None
        self.__age = None
        self.__model = None
        self.__body_type = None
        self.__mark = None

    # сеттер для установки возраста
    def set_all(self, tittle_, age_, model_, bode_type_, mark_):
        if 2003 < age_ < 2025:
            self.__age = age_
        else:
            print("\nНедопустимый год создания")
            retry_input(tittle_, model_, bode_type_, mark_)
        self.__mark = mark_
        self.__body_type = bode_type_
        self.__model = model_
        self.__tittle = tittle_

    def get_age(self):
        return self.__age

    def get_tittle(self):
        return self.__tittle

    def get_model(self):
        return self.__model

    def get_body_type(self):
        return self.__body_type

    def get_mark(self):
        return self.__mark

    def print_car(self):
        print(f"\nНазвание: {self.__tittle}\nГод создания: {self.__age}\nМарка: {self.__mark}\nМодель: {self.__model}\n"
              f"Тип кузова: {self.__body_type}")


def retry_input(tittle_, model_, bode_type_, mark_):
    age_ = int(input("\nЗаново введите год создания: "))
    car.set_all(tittle_, age_, model_, bode_type_, mark_)


car = create_machine()

tittle, age, model, bode_type, mark = map(str,
                                          input("Введите Название машины, её год создания, модель, тип кузова и её "
                                                "марку,"
                                                "в точно таком же порядке: ").split())

car.set_all(tittle, int(age), model, bode_type, mark)

car.print_car()
