def myGen():
    x = 1
    yield x

    x = 10
    yield x

    x = 50
    yield x


genObj = myGen()
print(next(genObj))
print(next(genObj))
print(next(genObj))


# Using for loop
for item in myGen():
    print(item) 
