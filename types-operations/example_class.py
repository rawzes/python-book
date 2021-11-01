class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def get_lastname(self):
        return self.name.split()[-1]
    def give_percent(self, percent):
        self.pay = self.pay + self.pay * percent / 100

emp1 = Worker('Roma Test', 1000)
emp2 = Worker('Ivan Ivanov', 500)

print(emp1.get_lastname(), emp1.pay)
emp1.give_percent(5)
print(emp1.get_lastname(), emp1.pay)
