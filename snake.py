
import pygame
import random
pygame.init()

pygame.mixer.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255.255,0)
screenwidth = 1200
screenheight = 800
gameWindow = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snk(gameWindow, color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x,y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("Hii, Welcome To Snake Game!!!",red,260,250)
        text_screen("Press space bar to play", black, 330, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('Blue Eyes .mp3')
                    pygame.mixer.music.play()

                    game_loop()
        pygame.display.update()
        clock.tick(60)

def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10

    fps = 10
    velocity_x = 10
    velocity_y = 10
    init_velocity = 5
    food_x = random.randint(20, screenwidth/2)
    food_y = random.randint(20, screenheight/2)
    score = 0
    snk_list = []
    snk_length = 1
    with open("highscore.txt", "r") as f:
        highscore = f.read()


    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            text_screen("Game Over! Please Enter to continue but you'll not hear music...", red, 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for  event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:

                        velocity_x = 10
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:

                        velocity_x = -10
                        velocity_y = 0
                    if event.key == pygame.K_UP:

                        velocity_y = -10
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:

                        velocity_y = 10
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score +=10



                food_x = random.randint(0, screenwidth)
                food_y = random.randint(0, screenheight)
                snk_length += 5
                if score>int(highscore):
                    highscore = score


            gameWindow.fill(white)
            text_screen("score:" + str(score )+ " High Score :"+str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)> snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x > screenwidth or snake_y < 0 or snake_y >screenheight:
                game_over =True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()

            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snk(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome()