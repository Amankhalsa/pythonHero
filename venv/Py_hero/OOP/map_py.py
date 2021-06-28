import random
randomlist = []
randomlist2 = []

for i in range(0,10):
    n = random.randint(1,30)
    m=  random.randint(1,40)
    randomlist.append(n)
    randomlist2.append(m)

print(randomlist)
print(randomlist2)
p=  random.randint(1,40)

# list_1 = [1,2,3,4,5,6,7,8]
# list_2 = [9,2,5,59,56,6,8,1]
list_1 =randomlist

list_2 =randomlist2


multi = lambda x:x*2
adder = lambda x,y:x+y
result = list(map(adder,list_1,list_2))
print(result)