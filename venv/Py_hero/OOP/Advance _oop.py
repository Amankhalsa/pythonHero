class Employees:

    def __init__(self,name,email,salary):

        self.name = name

        self.email = email

        self.salary = salary

    def message(self):
        print(f"Name: {self.name} \nEmail id: {self.email}  \nSalary: {self.salary}")

        return f'\t{self.name} is making {self.salary}'

name=input("Enter your name:")
email =input("Enter your email:")
emp_1 = Employees(name,email,100)

name2=input("Enter your name:")
email2 =input("Enter your email:")
emp_2 = Employees(name2,email2,200)


# emp_2 = Employees('sally','sally@gmail.com',200)
# print(emp_2.name,emp_2.email, emp_2.salary, emp_1.name)


print(Employees.message(emp_1))
print(Employees.message(emp_2))

    # print(emp_1.name)

    # print(emp_2.name)

    #

# print(emp_1.message())