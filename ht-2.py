class Employee(object):
    name = ''
    email = ''
    pay_day = 1

    def work(self):
        return "I come to the office."

    def check_salary(self, day):
        money = self.pay_day * day
        return money

class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."
    def __str__(self):
        return "Должность: {} Имя: {}".format(self.__class__.__name__, self.name)

class Programmer(Employee):
    def work(self):
        return "I come to the office and start to coding."
    def __str__(self):
        return "Должность: {} Имя: {}".format(self.__class__.__name__, self.name)


prog = Programmer()
prog.name = 'Alex'
prog.email = 'alex@mail.com'
prog.pay_day = 40

print(prog.check_salary(5))
print(prog.work())
print(prog.__str__())

rcr = Recruiter()
rcr.name = 'Yana'
rcr.email = 'yana@mail.com'
rcr.pay_day = 50

print(rcr.check_salary(3))
print(rcr.work())
print(rcr.__str__())
