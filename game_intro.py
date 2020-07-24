import pygame

class room:
    def __init__(self,parent):
        self.parent = parent
        self.imgloc = ["intro.png"]
        self.assets = []

    def loadassets(self):
        self.assets = [pygame.image.load("./images/intro/"+img) for img in self.imgloc]

    def draw(self,display,refreshroom):
        if refreshroom:self.loadassets()
        display.blit(self.assets[0],(0,0))

class action:
    def __init__(self,parent,room):
        self.parent = parent
        self.room = room

    def update(self,events):
        if not(self.room is None):
            for event in events:
                pass
