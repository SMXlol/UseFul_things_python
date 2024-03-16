import json


class person:

    def __init__(self, name, last_name, post, salary, func):
        self.name = name
        self.last_name = last_name
        self.post = post
        self.salary = salary
        func(self)

    def new_rab(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            data["workers"].append(
                {
                    "name": self.name,
                    "last_name": self.last_name,
                    "post": self.post,
                    "salary": self.salary
                }
            )
            data[dict][self.last_name].append(self.last_name)

        file.close()

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    def del_rab(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            data["workers"].pop(data["dict"].index(self.last_name))
            data["dict"].pop(data["dict"].index(self.last_name))

        file.close()

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    def output_rab(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            print("\nРаботники ТЕЛЕГРАММА\n")
            for i in range(len(data["workers"])):
                print(f"{data['workers'][i]['last_name']} {data['workers'][i]['name']}")
                print(f"Должность: {data['workers'][i]['post']}\n"
                      f"Зарплата: {data['workers'][i]['salary']}\n")


funcs = {1: person.new_rab, 2: person.del_rab, 3: person.output_rab}
funcs_in = {1: input_part_one, 2: person.del_rab, 3: person.output_rab}

class choice:
    
    def __init__(self):
        
    def input_part_one():
    
def input_choice():
    print("Что вы хотите сделать?\n\n"
          "1 - новый рабботник\n"
          "2 - освободить рабботника\n"
          "3 - вывести всех ваших раббов\n")
    
    choice = int(input("Введите выбранное действие"))
    func = funcs[choice]


while True:
    input_choice()
