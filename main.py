import pygame, sys, manager
from pygame.locals import HWSURFACE, DOUBLEBUF

pygame.init()
pygame.display.set_caption("jeevaLOGIC")
screen = manager.screen(800,600)
display = pygame.display.set_mode((screen.width,screen.height),HWSURFACE|DOUBLEBUF)
clock = pygame.time.Clock()

quitgame = False

room = manager.room(display)
gEvents = manager.gameevents(room.levelobject)

def collided(objectA,objectB):
    if ((objectA.x>(objectB.x+objectB.width))or(objectB.x>(objectA.x+objectA.width))):return False
    if ((objectA.y<(objectB.y+objectB.height))or(objectB.y<(objectA.y+objectA.height))):return False
    return True

def closewindow():
    quitgame = True
    pygame.quit()
    sys.exit(0)
    
while not quitgame:
    clock.tick(27)
    gEvents.update(pygame.event.get())
    gEvents.checkevent()
    for event in gEvents.events:
        if event.type == pygame.QUIT:closewindow()
    room.draw()
    pygame.display.update()
