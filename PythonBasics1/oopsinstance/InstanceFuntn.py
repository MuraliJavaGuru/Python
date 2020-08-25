def myfun(x):
    print(x)

myfun(20)

#self is a default argument ; and no need to pass value for self
class Person:
    # instance variables
    id = None
    name = None
    age = None

    # instance funtion
    def show(self):
        print(self.id)
        print(self.name)
        print(self.age)

    def show2(self, x):  # instance funtion
        print(self.id + x)


# create obj and set data
p1 = Person()
p1.id = 1000
p1.name = "user2"
p1.age = 45

print("******show p1*********")
p1.show()  # when show() funtn is called using p1 , then the logic inside the show() funtion is applied on the p1's data. self = p1

# create obj and set data
p2 = Person()
p2.id = 2000
p2.name = "user45"
p2.age = 32

print("******show p2*********")
p2.show()  # when show() funtn is called using p2 , then the logic inside the show() funtion is applied on the p2's data. self= p2


p1.show2(10) #self = p1 , x=10
p2.show2(20) # self=p2 , x =20

