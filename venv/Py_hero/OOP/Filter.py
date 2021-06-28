# filter function or method
import  random

list_1 = [x for x in range(30)]

test = lambda x:x%2==0

result = list(filter(test,list_1))


print("Odd numbers=",result)


