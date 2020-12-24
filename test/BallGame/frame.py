import pygame
from random import *

###################### 기본 설정(필수)################################
pygame.init() #초기화
# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GameName") # Title

clock = pygame.time.Clock()
####################################################################

# 1. 사용자 게임 초기화 (배경, 게임 이미지)
# background image
background = pygame.image.load("C:/Users/USER/PycharmProjects/untitled/test/BallGame/background.png")
# stage setting
stage = pygame.image.load("C:/Users/USER/PycharmProjects/untitled/test/BallGame/stage.png")
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]
stage_x_pos = 0
stage_y_pos = screen_height - stage_height

weapon = pygame.image.load("C:/Users/USER/PycharmProjects/untitled/test/BallGame/weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = 0
weapon_y_pos = screen_height
weapon_speed = 0.6

# character setting
character = pygame.image.load("C:/Users/USER/PycharmProjects/untitled/test/BallGame/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2  # place mid
character_y_pos = screen_height - character_height
# 이동 좌표
to_x = 0
to_y = 0
# 이동속도
character_speed = 0.6
# enemy setting
ball = pygame.image.load("C:/Users/USER/PycharmProjects/untitled/test/BallGame/ball_1.png")
ball_size = character.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]
ball_x_pos = randrange(0, screen_width-ball_width)  # place mid
ball_y_pos = 0
ball_speed = 0.6

ball2 = pygame.image.load("C:/Users/USER/PycharmProjects/untitled/test/BallGame/ball_2.png")
ball2_size = character.get_rect().size
ball2_width = ball_size[0]
ball2_height = ball_size[1]
ball2_x_pos = 0  # place mid
ball2_y_pos = 0
ball2_speed = 0.6


# font define
game_font = pygame.font.Font(None, 40)
# total time
total_time = 99
# start time
start_ticks = pygame.time.get_ticks()

# Event loop
running = True
while running:
    dt = clock.tick(30)
    # 2. 이벤트처리
    for event in pygame.event.get(): # what event
        if event.type == pygame.QUIT: # End game
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x =0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                to_y =0
    # 3. 캐릭터 위치 정의
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
         character_x_pos =  screen_width -  character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
         character_y_pos =  screen_height -  character_height

    ball_y_pos += ball_speed

    # 4. 충돌처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect =  character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ball_rect = ball.get_rect()
    ball_rect.left = ball_x_pos
    ball_rect.top = ball_y_pos

    weapon_rect = weapon.get_rect()
    weapon_rect.left = weapon_x_pos
    weapon_rect.top = weapon_y_pos



    if character_rect.colliderect(ball_rect):
        print("충돌")
        running = False

    if ball_rect.colliderect(weapon_rect):
        ball = ball2




    # 5. 화면에 적용
    screen.blit(background, (0,0)) #2 background
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(weapon, ())
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ball, (ball_x_pos, ball_y_pos))

    # timer input
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과시간(ms)dmf 1000으로 나눠 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)),True,(0,0,255))
    # time, True, font color

    screen.blit(timer, (10, 10))

    if total_time-elapsed_time <=0:
        print("Time Out")
        running = False


    pygame.display.update()

# 2 sec. delay
pygame.time.delay(2000)

# End game
pygame.quit()