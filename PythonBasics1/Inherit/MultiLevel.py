class Person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    def showPersonalInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)


class Employee(Person):
    def __init__(self,id,name,age,pfNo,pan):
        Person.__init__(self, id, name, age)
        self.pfNo = pfNo
        self.pan = pan

    def printEmp(self):
        print(self.pan)
        print(self.pfNo)


class Staff(Employee):
    def __init__(self, id, name, age, pan, pfNo, contactId,contarctPeriod):
        '''invoke parent constructor'''
        Employee.__init__(self, id, name, age,pan,pfNo)
        self.contactId = contactId
        self.contarctPeriod = contarctPeriod

    def displayStaff(self):
        print(self.contactId, self.contarctPeriod)

#create obj for person
print("print person info")
p = Person(2000,"user1", 56)
p.showPersonalInfo()

#create obj for employee
print("print employee info")
emp = Employee(20001, "albert", 54, "testPf", "testPan")
emp.showPersonalInfo()
emp.printEmp()
   

#create obj for staff
print("print staff info")
s1 =Staff(1201, "user2", 28, "proj77777", "IT" ,"c_88888","12 months")
s1.showPersonalInfo()
s1.printEmp()
s1.displayStaff()