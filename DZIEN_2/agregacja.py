class Department:
    def __init__(self,name,employees):
        self.name = name
        self.employees = employees

class Employee:
    def __init__(self,name,department):
        self.name = name
        self.department = department

depertment = Department("Sales",[])
employee1 = Employee("Janek Kot",depertment)
employee2 = Employee("Olga Nowak",depertment)
depertment.employees.append(employee1)
depertment.employees.append(employee2)

print(depertment.name)
print(len(depertment.employees))
print(depertment.employees[0].name)
print(depertment.employees[1].name)
