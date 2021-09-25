import pygame
from random import randrange

RES = 800  # размер нашего окна
SIZE = 20  # размер танка

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)  # начальное положение
alien = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)  # начальное положение цели
length = 1  # длинна танка
spaceship = [(x, y)]  # танк список координат
dx, dy = 0, 0   # направление движения
fps = 10  # скорость
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0   # очки
speed_count, spaceship_speed = 0, 10

pygame.init()  # инициализируем pygame
surface = pygame.display.set_mode([RES, RES])  # иницилизируем рабочее окно
clock = pygame.time.Clock()                    # объект регулирует скорость танка
font_score = pygame.font.SysFont('Arial', 26, bold=True)  #  шрифт для очков
font_end = pygame.font.SysFont('Arial', 66, bold=True)    #  шрифт для  конца игры
img = pygame.image.load('1.jpg').convert()                #  фон рисунок

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

while True:
    surface.blit(img, (0, 0))

    [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in spaceship]  # рисуем танк с разделением -1
    pygame.draw.rect(surface, pygame.Color('red'), (*alien, SIZE, SIZE))   # рисуем цель

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))  # надпись подсчет очков
    surface.blit(render_score, (5, 5))

    speed_count += 1     # рост скорости нашего танка
    if not speed_count % spaceship_speed:
        x += dx * SIZE    # рост скорости нашего танка
        y += dy * SIZE    # рост скорости нашего танка
        spaceship.append((x, y))
        spaceship = spaceship[-length:]  # срез координат в соответствии со значением длинны танка

    if spaceship[-1] == alien:            # поражение цели
        alien = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)  # размещение цели
        length += 1  # увеличиваем длинну танка
        score += 1  #  увеличиваем скорость
        spaceship_speed -= 1
        spaceship_speed = max(spaceship_speed, 4)

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(spaceship) != len(set(spaceship)):  # случай пройгрыша выход за поле
        while True:                                                                                  #  или
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()

    pygame.display.flip()
    clock.tick(fps)
    close_game()

    key = pygame.key.get_pressed()   # управление танком
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }





