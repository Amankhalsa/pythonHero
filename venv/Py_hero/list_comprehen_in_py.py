# list_man = [1,2,3,4,5,6,7,8,9]
# print(list_man)
# print('x'*20)
list_norm = []
for x in range(10):
 list_norm.append(x)
print(list_norm)
# print('x'*20)
print('x' * 20)
list_com = [x*2 for x in range(20) if x % 2 == 0]
print(list_com)
print('x' * 20)
list_com = [x for x in range(30) if x % 2 == 1]
print(list_com)