import pygame
import random

# initialisation:
pygame.init()
width = 600
height = 400
blocksize = 10

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snakes by LMc")
pygame.display.update()

# initialise gamestates
game_over = False
game_close = False

# colours:
red = (128, 0, 0)
white = (255, 255, 255)
grey = (150, 150, 150)
orange = (255, 150, 20)
lightblue = (0, 200, 255)

# snake position:
snake_speed = 20
x = int(width / 2)
y = int(height / 2)
x_change = 0
y_change = 0
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("freesans", 25)
lost_img = font_style.render("You died! P to play again or Q to  Quit", True, red)


def the_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orange, (x[0], x[1], snake_block, snake_block))


def thescore(score):
    value = font_style.render("Your Score: " + str(score), True, lightblue)
    dis.blit(value, [0, 0])


def game_loop():
    game_over = False
    game_close = False
    x = 300
    y = 200
    x_change = 0
    y_change = 0
    foodposx = blocksize * random.randint(0, (width // blocksize - 1))
    foodposy = blocksize * random.randint(0, (height // blocksize) - 1)
    snake_list = []
    length_of_snake = 1

    while (game_over == False):
        while (game_close == True):
            dis.fill(white)
            dis.blit(lost_img, [100, 100])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -10

                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 10

                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0

                elif event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x = x + x_change  # set new x pos
        y = y + y_change  # set new y pos
        dis.fill(grey)

        # pygame.draw.rect(dis,orange,(x,y,10,10))#position of snake, rectangle size 10x10
        pygame.draw.rect(dis, lightblue, (foodposx, foodposy, blocksize, blocksize))
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        the_snake(blocksize, snake_list)
        if x == foodposx and y == foodposy:
            length_of_snake += 1
            foodposx = blocksize * random.randint(0, (width // blocksize - 1))
            foodposy = blocksize * random.randint(0, (height // blocksize) - 1)
        thescore(length_of_snake - 1)
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()


game_loop()
