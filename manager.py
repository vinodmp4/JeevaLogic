import pygame, game_intro, levelselector, level1

class screen:
    def __init__(self,width,height):
        self.width = width
        self.height = height

class room:
    def __init__(self, display):
        self.currentRoom = 'level1'
        self.display = display
        self.roomId = {'intro':0,"levelselector":1,'level1':2}
        self.levelobject = None
        self.roomchanged = True
        self.draw()
        
    def intro(self):
        if self.roomchanged:
            self.levelobject = game_intro.room(self)
        if not(self.levelobject is None):self.levelobject.draw(self.display,self.roomchanged)
        if self.roomchanged:self.roomchanged = False

    def levelselector(self):
        if self.roomchanged:
            self.levelobject = levelselector.room(self)
        if not(self.levelobject is None):self.levelobject.draw(self.display,self.roomchanged)
        if self.roomchanged:self.roomchanged = False

    def level1(self):
        if self.roomchanged:
            self.levelobject = level1.room(self)
        if not(self.levelobject is None):self.levelobject.draw(self.display,self.roomchanged)
        if self.roomchanged:self.roomchanged = False

    def setRoom(self,roomName):
        self.currentRoom = roomName
        self.roomchanged = True
        
    def draw(self):
        Id = self.roomId.setdefault(self.currentRoom,0)
        if Id == 0:self.intro()
        elif Id == 1:self.levelselector()
        elif Id == 2:self.level1()

class gameevents:
    def __init__(self,levelgraphics):
        self.events = []
        self.levelId = {'intro':0,"levelselector":1,'level1':2}
        self.currentKey = "level1"
        self.levelchanged = True
        self.actionobject = None
        self.levelgraphics = levelgraphics

    def intro(self):
        if self.levelchanged:
            self.actionobject = game_intro.action(self,self.levelgraphics)
        if not(self.actionobject is None):self.actionobject.update(self.events)
        if self.levelchanged:self.levelchanged = False

    def levelselector(self):
        if self.levelchanged:
            self.actionobject = levelselector.action(self,self.levelgraphics)
        if not(self.actionobject is None):self.actionobject.update(self.events)
        if self.levelchanged:self.levelchanged = False

    def level1(self):
        if self.levelchanged:
            self.actionobject = level1.action(self,self.levelgraphics)
        if not(self.actionobject is None):self.actionobject.update(self.events)
        if self.levelchanged:self.levelchanged = False

    def setlevel(self,levelname):
        self.currentKey = levelname
        self.levelchanged = True

    def update(self,events):
        self.events = events

    def checkevent(self):
        Id = self.levelId.setdefault(self.currentKey,0)
        if Id == 0:self.intro()
        elif Id == 1:self.levelselector()
        elif Id == 2:self.level1()
