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

import pygame
import random

num = random.randint(0, 100)
print(num)
W = 480
H = 360
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
numeral = ''
move = 1
block = 0
start = 1
OUISIDE_BG = (0, -100)

pygame.init()
pygame.display.set_caption('угадай число')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 28, True, False)
font_box = pygame.Surface((W - font.get_height(), font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - font.get_height()))
font2 = pygame.font.SysFont('Arial', 14, False, True)

bg = pygame.image.load('image/room.png')
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load('image/cat.png')
cat_rect = cat.get_rect(center=(70, 220))
dog = pygame.image.load('image/dog.png')
dog_rect = dog.get_rect(center=(410, 220))
owl = pygame.image.load('image/owl.png')
owl_rect = owl.get_rect(center=(210, 120))
dialog = pygame.image.load('image/dialog.png')
dialog_rect = dialog.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w // 2, dog_rect.y - dialog_rect.h)
dialog_owl_pos = (owl_rect.x, owl_rect.y - dialog_rect.h)


def dialogs(text, pos, owl_text):
    screen.blit(dialog, pos)
    screen.blit(font2.render(text, True, BLACK), (pos[0] + 5, pos[1] + 5))
    screen.blit(dialog, dialog_owl_pos)
    screen.blit(font2.render(owl_text, True, BLACK), (dialog_owl_pos[0] + 5, dialog_owl_pos[1] + 5))
    pygame.display.update()
    pygame.time.wait(2000)

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

    if block = 0:
        screen.blit(bg, bg_rect)
        screen.blit(cat, cat_rect)
         screen.blit(dog, dog_rect)
        screen.blit(owl, owl_rect)
         screen.blit(font_box, font_rect)
         font_box.fill(SILVER)
        font_box.blit(
        font.render(numeral, True, BLACK), (10, 0)
     )
    pygame.display.update() 

    if start == 1:
         dialogs("", OUTSIDE_BG, 'лОЛОЛОЛО')
         dialogs("", OUTSIDE_BG, 'ЛЯЛЯЛЯЛЯЛЛ')
        start 0
pygame.quit()