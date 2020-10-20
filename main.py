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


# Цикл while в игре
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.quit:
            run = False
        # Выход из игры с помощью escape
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
            # Печатает только цифры
            elif e.unicode.isdecimal() and block == 0:
                numeral += e.unicode
            # Удаляет последний элемент
            elif e.key == pygame.K_BACKSPACE:
                numeral = numeral [:-1]
            elif e.key == pygame.K_RETURN and numeral:
                if int(numeral) > 100:
                    dialogs('', OUTSIDE_BG, 'Вы ошиблись')
                elif int(numeral) > num:
                    dialogs('', OUTSIDE_BG, 'Число меньше')
                elif int(numeral) < num:
                    dialogs('', OUTSIDE_BG, 'Число больше')
                if move == 1:
                    if int(numeral) == num:
                        dialogs (f'Это число {numeral}', dialog_cat_pos, 'Кот ты выиграл')
                        block = 1
                    else:
                        dialogs('Дог, твой ход', dialog_dog_pos, 'Продолжаем')
                elif move == 2:
                    if int(numeral) == num:
                        dialogs (f'Это число {numeral}', dialog_cat_pos, 'Дог ты выиграл')
                        block = 1
                    else:
                        dialogs('Кот, твой ход', dialog_dog_pos, 'Продолжаем')
                numeral = ''
                move += 1
                if move > 2:
                    move = 1
