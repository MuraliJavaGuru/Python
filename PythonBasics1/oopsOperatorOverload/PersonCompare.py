class Person:
    def __init__(self,id,name,age): #instance varibales
        self.id=id
        self.name=name
        self.age=age

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.age == other.age


p2 = Person(1000,"user1",67)
p1 =Person(1000,"user1",67)

if p2==p1: # internally calls __eq__
    print("p2 and p1 are duplicates")
else:
    print("p2 and p1 are not duplicates")


p3=p1
if p3==p1:
    print("p3 and p1 are duplicates")
else:
    print("p3 and p1 are not duplicates")






"""
p2 =Person(1000,"user1",68)

print(p1==p2)    
"""


# assignment:
#take multiple person objs and remove duplicates
# use list or set


