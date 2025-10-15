# یک کلاس به نام Employee طراحی کنید که شامل ویژگی‌های زیر باشد:

# • name: نام کارمند

# • salary: حقوق کارمند

# سپس یک کلاس به نام Department طراحی کنید که شامل متدهای زیر باشد:

# • add_employee(employee): افزودن یک کارمند به دپارتمان.

# • get_total_salary(): محاسبه و برگرداندن مجموع حقوق همه کارمندان.



class Employee :

    def __init__(self , name , salary):

        self.name = name
        self.salary = salary

        

    def info(self):
        print(f'your name is {self.name} and your salary {self.salary} $')

class Department :

    def __init__(self):

        self.employeeList = []
       
    def add_employee(self , employee) :
        self.employeeList.append(employee)

    def get_total_salary(self) :
        return sum(employee.salary for employee in self.employeeList )


employee1 = Employee("A" , 100)
employee2 = Employee("B" , 200)
employee3 = Employee("C" , 300)

Department1 = Department()
Department1.add_employee(employee1)
Department1.add_employee(employee2)
Department1.add_employee(employee3)

x = Department1.get_total_salary()
print(x)