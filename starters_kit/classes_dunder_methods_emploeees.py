import typing
from math import ceil

class Employee:
    raise_amount = 1.07

    def __init__(self, first=str, last=str, pay=int):
        self.first = first
        self.last = last
        self.email = str(f'{first}.{last}@domain.com')
        self.pay = ceil(pay)

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = ceil(self.pay * self.raise_amount)

    def print_email(self):
        print(f"{self} email: {self.email}")

    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.pay}')"

    def __str__(self):
        return f"{self.first} {self.last}"

class Developer(Employee):
    raise_amount = 1.12

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return f"Developer('{self.first}','{self.last}',{self.pay},'{self.prog_lang}')"

class Manager(Employee):

    def __init__(self, first, last, pay, employees: typing.Optional[list]):
        super().__init__(first, last, pay)
        self.employees = employees if employees is not None else []

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"{emp}")

    def __repr__(self):
        return f"Manager('{self.first}','{self.last}',{self.pay},[{self.employees}])"


emp1 = Employee("Sara", "Connor", 20000)
dev1 = Developer("Will", "Smith", 35000.50, "Python")
mng1 = Manager("Lusi", "Liu", 51000.55, [dev1, emp1])

print(f"{emp1.email}\n{dev1.email}\n{mng1.email}\n")
print(f"{mng1} is manager for:")
print(f"{mng1.print_emps()}")     #where does it get the third item None?!
#print(mng1.employees)             here are only two items!

dev1.apply_raise()
dev1.apply_raise()
print(f"\n{dev1} has ${dev1.pay} each month.")
emp1.apply_raise()
emp1.apply_raise()
emp1.apply_raise()
emp1.apply_raise()
print(f"{emp1} has ${emp1.pay} each month.")
mng1.apply_raise()
print(f"{mng1} has ${mng1.pay} each month.")