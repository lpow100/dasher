import pygame
pygame.init()
WIDTH = 300
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("dodge")
enemycolor = (0,0,245)
ground = pygame.Rect(10,200,280,10)
class obj:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)
ischanged = "no"
player = obj(125,150,50,50,(0,255,10))
enemy = obj(135,0,30,30,enemycolor)
running = True

def inscreen(thing: obj):  
    thing.x = max(0, min(thing.x, WIDTH - thing.width))
    thing.y = max(0, min(thing.y, HEIGHT - thing.height))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), ground, 2)
    pygame.draw.rect(screen, player.color, player.rect())
    pygame.draw.rect(screen, enemycolor,enemy.rect())
    if pygame.key.get_pressed()[pygame.K_d]:
        player.x += 0.035
    elif pygame.key.get_pressed()[pygame.K_a]:
        player.x -= 0.035
    if pygame.key.get_pressed()[pygame.K_e]:
        if ischanged == "no":
            player.color = tuple(color+enemycolor[i] for i,color in enumerate(player.color))
            ischanged = "yes"
    enemy.y += 0.019
    inscreen(enemy)
    inscreen(player)
    pygame.display.flip()
pygame.quit()