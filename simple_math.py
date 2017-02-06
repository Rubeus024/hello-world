import sys, pygame

pygame.init()

size=width,height=320,240 # utworzylem dwie
#zmienne licznowe width height oraz krotkę size
speed=[2,2]
black = 255,255,255 #utworzenie krotki z 3 elementami
screen = pygame.display.set_mode(size)
print("Pygame display",type(pygame.display.set_mode()))
ball=pygame.image.load("ball.jpg")
print(type(ball))

ballrect=ball.get_rect()
print(type(ballrect))
print()
print(pygame.event.get())
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ballrect=ballrect.move(speed)
    if ballrect.left <0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top < 0 or ballrect.bottom>height:
        speed[1]=-speed[1]
    screen.fill(black)
    screen.blit(ball,ballrect)
    pygame.display.flip()
