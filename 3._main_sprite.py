import pygame

pygame.init() #초기화 (반드시 해야한다)

#화면 크기 설정하기
screen_width = 480 # 가로 
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Jin's Game")

# 배경 이미지 불러오기
background = pygame.image.load("/Users/jeongjin/Desktop/Coding/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/jeongjin/Desktop/Coding/pygame_basic/character.png") #70*70
character_size = character.get_rect().size # 이미지 크기 구하기
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #가로 중앙에 위치
character_y_pos = screen_height - character_height #세로 하단에 위치

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos)) 
    pygame.display.update() 
#pygame 종료
pygame.quit()