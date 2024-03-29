import pygame

pygame.init() #초기화 (반드시 해야한다)

#화면 크기 설정하기
screen_width = 480 # 가로 
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("/Users/jeongjin/Desktop/Coding/pygame_basic/background.png") # 사이즈가 정확히 일치해야 실행됌

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    # screen.fill((0,0,255)) -> rgb로 그냥 배경 채울 수 도있음
    screen.blit(background, (0, 0)) # 배경 그리기 (X좌표, Y좌표)
    pygame.display.update() # 게임화면을 다시 그리기 (꼭 필요)
#pygame 종료
pygame.quit()