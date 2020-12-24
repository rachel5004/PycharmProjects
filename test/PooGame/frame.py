import pygame
from random import *

###################### 기본 설정(필수)################################
pygame.init() #초기화
# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GameName") # Title

clock = pygame.time.Clock()
####################################################################

# 1. 사용자 게임 초기화 (배경, 게임 이미지)
# background image
background = pygame.image.load("C:/Users/USER/PycharmProjects/untitled/test/MyGame/background.png")
# character setting
character = pygame.image.load("C:/Users/USER/PycharmProjects/untitled/test/MyGame/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2  # place mid
character_y_pos = screen_height - character_height
# 이동 좌표
to_x = 0
to_y = 0
# 이동속도
charater_speed = 0.6
# enemy setting
enemy = pygame.image.load("C:/Users/USER/PycharmProjects/untitled/test/MyGame/enemy.png")
enemy_size = character.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randrange(0, screen_width-enemy_width)  # place mid
enemy_y_pos = 0
enemy_speed = 10

score =0

# font define
game_font = pygame.font.Font(None, 40)
# total time
total_time = 500
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
                to_x -= charater_speed
            elif event.key == pygame.K_RIGHT:
                to_x += charater_speed
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

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        score += 1
        enemy_y_pos = 0
        enemy_x_pos = randrange(0, screen_width-enemy_width)
        enemy_speed += 2

    # 4. 충돌처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect =  character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False



    # 5. 화면에 적용
    screen.blit(background, (0,0)) #2 background
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

    # timer input
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과시간(ms)dmf 1000으로 나눠 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)),True,(0,0,255))
    # time, True, font color
    score_cnt = game_font.render(str(int(score)), True, (0,0,255))

    screen.blit(timer, (10, 10))
    screen.blit(score_cnt, (460, 10))

    if total_time-elapsed_time <=0:
        print("Time Out")
        running = False


    pygame.display.update()

# 2 sec. delay
pygame.time.delay(2000)

# End game
pygame.quit()