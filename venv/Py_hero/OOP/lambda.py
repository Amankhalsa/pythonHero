def adder(x):
    return x +10
add_lam = lambda x:x +10
text_lam = lambda name:f'Hi {name} How are you'
print(adder(2))
print(add_lam(2))
user=input("Enter name:")
print(text_lam(user))

"""
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
#============================
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
"""