# def fun_name(x,y):
#  print(x *y)
#  fun_name(x, y)
#
#
#
#
# fun_name(2,3)

#Rec Function by
def table(num, i):
    result = num * i

    print(f'{i} X {num} = {result}')
    i += 1
    while i != 11:
        table(num, i)
        break


table(5, 1)
