# Number
# string
# list
# dict
# tuple
# set

a=2345
b=374.3
print(type (a),a)
print(type (b),b)

name="this is a car can't for flying"
print(type(name),name)
c= 'This is a single qoutes "string" '
d=" double we can use \n for new line "
e="""This 
is also 
multiline for paragraph writing 
"""
f="she is asking me  i \"like you\" "
print(type(c),c)
print(d)
print(e)
print(f)

# List is here list can hold every thing
list=[1,2,3,"A",5.6,{"name:""Aman"}, (),[]   ]
print(type(list),list)
print(type(list[3]))
print(type(list[4]))
print(type(list[5]))
print(type(list[6]))
print(type(list[7]))

# 3- Lists

# test_list = [1,1.1,'string',{},(),[]]
#
# print(test_list[5])


# 4- Dictionaries(Objects)

# dic_test = {'key':'value','key2':2}
# print(dic_test)
# print(dic_test['key2'])



list2=[1,{"key1":"value_1"}]
# in the list we can access object by this method
print(list2[1]["key1"])

my_dic={"key1":"valu1"}
print(my_dic["key1"])