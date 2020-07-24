import pygame

class room:
    def __init__(self,parent):
        self.parent = parent
        self.imgloc = []
        self.assets = []

    def loadassets(self):
        pass

    def draw(self,display,refreshroom):
        if refreshroom:self.loadassets()
        display.fill((0,255,0))

class action:
    def __init__(self,parent,room):
        self.parent = parent
        self.room = room

    def update(self,events):
        if not(self.room is None):
            for event in events:
                pass
