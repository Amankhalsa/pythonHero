# if statement
# continue
# break

list_pl = ['java', 'python', 'c++', 'HTML', 'css']

for pl in list_pl:
    if pl == 'c++':
        print('I am before break statemt')
        break
        print('I am after continue statemt')
    else:
        print(pl)