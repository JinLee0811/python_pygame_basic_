import pygame

pygame.init() #초기화 (반드시 해야한다)

#화면 크기 설정하기
screen_width = 480 # 가로 
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Jin's Game")

# FPS
clock = pygame.time.Clock() # 시계 생성

# 배경 이미지 불러오기
background = pygame.image.load("/Users/jeongjin/Desktop/Coding/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/jeongjin/Desktop/Coding/pygame_basic/character.png") #70*70
character_size = character.get_rect().size # 이미지 크기 구하기
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #가로 중앙에 위치
character_y_pos = screen_height - character_height #세로 하단에 위치

# 적 enemy 캐릭터
enemy = pygame.image.load("/Users/jeongjin/Desktop/Coding/pygame_basic/enemy.png") #70*70
enemy_size = enemy.get_rect().size # 이미지 크기 구하기
enemy_width = enemy_size[0] #캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #가로 중앙에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) #세로 중앙에 위치


# 이동할 좌표 값 정의
to_x = 0
to_y = 0

# 이동 속도 정의
character_speed = 0.6

# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 정의, 크기 정의

# 총 시간
total_time = 10
# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 시간을 ms단위로 반환


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    # 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN: #키가 눌리는지 확인
            if event.key == pygame.K_LEFT: #캐릭터 왼쪽이동
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터 오른쪽이동
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #만약 방향키에서 손때면 멈추게 하기
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0       

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0 
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False # 게임 종료 처리

    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기


    #타이머 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 타이머 출력
    # 출력할 글자, True, 글자 색상 RGB
    screen.blit(timer, (10, 10)) # 타이머 출력 
    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print('time out')
        running = False # 게임 종료 처리
        
    pygame.display.update()

# 종료 직전 잠시 대기
pygame.time.delay(2000)     
#pygame 종료
pygame.quit()