'''
#Работа с условными операторами

name1 = 0
name2 = 0

if name1 == name2:
    print('name1 = name2')
    if name2 is True:
        print('True')
elif name1 < name2:
    print ('name1 < name2')
elif name1 != name2:
    pass
else:
    print('name1 = name2')
'''

'''
#Работа с циклам for
for i in 1, 2, 3, 'sorry':
    print(i)

for i in 'sorry':
    print(i)
'''

'''
#Список [], Кортедж ()
n = [1, 2, 3, 'sorry']
print(n[0])
print(len(n))
n.append(7)
print(n)
'''

'''
#Работа с циклом while
m = 0
#while True - бесконечный цикл
while m < 10:
    print(m)
    m += 1
'''