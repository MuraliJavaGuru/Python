# take name and pass as input ,
#if name == 'admin' and  pass ='admin' login success else login failure
"""
can we write multiple conditions in one if statement??
yes

ways:
-> and
[if multiple conditions are joined by using and then the if block is executed only if all conditions are satisfied]
-> or
[if multiple conditions are joined by using or then the if block is executed  if atleast one  condition is satisfied]
"""
name = input("enter login  name : ")
password = input("enter password : ")


if name ==  "admin"  and password =="admin":
    print("login succes")
else:
    print("login failure")
