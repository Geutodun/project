import pygame

pygame.init()

#화면 크기
screen_width = 480  #가로
screen_height = 640  #세로
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Geutodun game") #게임이름   

#FPS
clock = pygame.time.Clock()


#배경 이미지 불러오기
background = pygame.image.load("E:\\파이썬\pygame_basic\\background.png")

#스프라이트(캐릭터) 불러오기
character = pygame.image.load("E:\\파이썬\pygame_basic\\character.png")
character_size = character.get_rect().size   #이미지 크기 구함
character_width = character_size[0]  #캐릭터의 가로 크기
character_height = character_size[1]  #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  #화면 가로 크기 절반에 위치 (가로)
character_y_pos = screen_height - character_height#화면 세로크기 가장 아래에 위치 (세로)


#이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 0.5


#이벤트 루프
running = True #게임이 진행중?
while running:
    dt = clock.tick(60)  #게임의 프레임 정하기

    #이동속도를 프레임마다 같게 하기 위해 이동속도르르 프레임마다 조정
    
    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():  #어떤 사건 발생?
        if event.type == pygame.QUIT: #게임을 나가는 사건 발생?
            running = False   #게임 진행X
         
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로 이동
                to_x -= character_speed  
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로 이동
                to_x += character_speed
            elif event.key == pygame.K_UP: #캐릭터를 위로 이동
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로 이동
                to_y += character_speed
        
        if event.type == pygame.KEYUP: #방향키를 떄면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0     
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

 
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

       #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:    
        character_x_pos = screen_width - character_width 

       #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:    
        character_y_pos = screen_height - character_height   


    #screen.fill((0, 0, 255))     #R,G,B설정으로 스크린 채우기(fill:채우다)
    screen.blit(background, (0, 0))   #배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    pygame.display.update()  #게임화면 다시 그리기



#게임 종료
pygame.quit()