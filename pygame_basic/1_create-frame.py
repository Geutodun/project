import pygame

pygame.init()

#화면 크기
screen_width = 480  #가로
screen_height = 640  #세로
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Geutodun game") #게임이름   

#이벤트 루프
running = True #게임이 진행중?
while running:
    for event in pygame.event.get():  #어떤 사건 발생?
        if event.type == pygame.Quit: #게임을 나가는 사건 발생?
            running = False   #게임 진행X

#게임 종료
pygame.quit()