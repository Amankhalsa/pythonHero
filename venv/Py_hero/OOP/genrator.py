# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
# return delete local variable,Generator(yield) holds or Pause the Variable value


print("2nd example "*5)
def a(x):

    return x+10
def d():
    x = 5
    print(x)
    yield x
    x += 1
    print(x)
    yield x
    x += 1
    print(x)
    yield x
gen = d()
next(gen)
next(gen)
next(gen)


# x="hello"[0]
x={1,2,3,4,2,3,1,3,4,}
print(x)