from random import randrange
import pygame
import os


pygame.init()
pygame.font.init()

x=800
y=600
j=0

class Towers:
    def __init__(self, height=100, gap=100, tower_x=x, width=60):
        self.height = height
        self.gap = gap
        self.top = y-height-gap
        self.width = width
        self.tower_x=tower_x
    def show(self, x):
        pygame.draw.rect(screen, (0,128,128), pygame.Rect(x,y-self.height,self.width,self.height))
        pygame.draw.rect(screen, (0,128,128), pygame.Rect(x,0,self.width,self.top))


def get_tower():
    return Towers(randrange(0,500),randrange(100,300),tower_x=x+300*len(towers))
    

birdimg=pygame.image.load(os.path.join('Assets','bird.png'))
def bird(birdx=100,birdy=300):
    screen.blit(birdimg,(birdx,birdy))


pygame.display.set_caption("Flappy Melon")
pygame.display.set_icon(pygame.image.load(os.path.join('Assets','thermometer.png')))
screen = pygame.display.set_mode((x,y))

birdx=100
birdy=300
birdx_change=0
birdy_change=0

running = True
status = 0

c1=(0,255,0)
digital_font = pygame.font.SysFont('Digital-7 Mono', 30)
digital_big = pygame.font.SysFont('Digital-7 Mono', 50)
coolgame = digital_font.render('Cool Game', False, c1)
paused = digital_font.render('Paused', False, c1)


i=0
score=0
towers=[]
while running:
    for event in pygame.event.get():
        if status!=2:
            if event.type==pygame.MOUSEBUTTONDOWN:
                status=1
        if event.type==pygame.QUIT:
                running=False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    while status==1:
        screen.fill((0,0,0))
        screen.blit(coolgame,(x-140,y-30))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                status=0
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status=0
                    running = False
                if event.key == pygame.K_SPACE:
                    birdy_change=-1.5
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    birdy_change=0
            if event.type==pygame.MOUSEBUTTONDOWN:
                status=0     
        
        if birdy_change!=-1:
            birdy_change+=0.006
        birdy+=birdy_change
        
        if i%300==0:
            towers.append(get_tower())

        for tower in towers:
            tower.show(tower.tower_x-i)
            if tower.tower_x-i<birdx<tower.tower_x-i+tower.width/2:
                if birdy>y-tower.height or birdy<tower.top:
                    status=2
            if birdx==tower.tower_x-i:
                score += 1
        scoretext=digital_font.render(str(score),False,(255,255,255))
        screen.blit(scoretext,(770,25))
        birdx=0 if birdx<0 else birdx
        birdx=x-50 if birdx>x-50 else birdx
        birdy=0 if birdy<0 else birdy
        birdy=y-50 if birdy>y-50 else birdy 
        bird(birdx,birdy)
        pygame.display.update()
        i += 0.5
    else:
        if status==0:
            screen.fill((0,0,0))
            bird(birdx,birdy)
            screen.blit(paused,(x-100,y-30))
            for tower in towers:
                tower.show(tower.tower_x-i)
            screen.blit(digital_big.render('Mouse Click To Start/Continue',False,(253, 216, 53)),(70,30))
            pygame.display.update()
        if status==2:
            screen.fill((0,0,0))
            for tower in towers:
                tower.show(tower.tower_x-i)
            bird(birdx,birdy)
            screen.blit(digital_big.render('GAME OVER', False,(255,0,0)),(300,280))
            screen.blit(scoretext,(397,350))
            pygame.display.update()