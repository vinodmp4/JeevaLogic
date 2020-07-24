import pygame
class room:
    def __init__(self,parent):
        self.parent = parent
        self.imageLocations = ["background.png","icon_A.png","icon_T.png","icon_G.png","icon_C.png","retry.png","hint.png","menu.png","success.png","wrong.png"]
        self.lifeimgs = ["life_0.png","life_1.png","life_2.png","life_3.png"]
        self.colRloc = ["R_A.png","R_T.png","R_G.png","R_C.png"]
        self.colLloc = ["L_A.png","L_T.png","L_G.png","L_C.png"]
        self.greyloc = ["GR_A.png","GR_T.png","GR_G.png","GR_C.png"]
        self.minipositions = [60,100,140,180,220,260,300,340,380,420,460,500]
        self.miniR = []
        self.miniL = []
        self.miniG = []
        self.assets = []
        self.lifeindicator = []
        self.colR = []
        self.colL = []
        self.greyimg = []
        self.selecteditem = ""
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_down = False
        self.life = 3
        self.mouseabovereset = False
        self.currentquestion = ""
        self.panel = ["","","","","","",""]
        self.values = [0,0,0,0,0,0,0]
        self.sequence = "AGCTGTACCTGA"
        self.verifier = {"A":"T","T":"A","G":"C","C":"G"}
        self.index = 0
        self.firsttime = True
        self._pulseindex = 0
        self.pulseindex = 0
        self.pulseup = True
        self.hintactive = True
        self.mouseabovehintbuttons = [False,False]
        self.showstatus = [False, True] # 1. show status, 2. answer right/wrong
        self.statusval = 0
        self.updatevalues()
        
    def loadassets(self):
        self.assets = [pygame.image.load("./images/level1/"+img) for img in self.imageLocations]
        self.lifeindicator = [pygame.transform.scale(pygame.image.load("./images/level1/"+img),(87,25)) for img in self.lifeimgs]
        self.colR = [pygame.image.load("./images/level1/"+img) for img in self.colRloc]
        self.colL = [pygame.image.load("./images/level1/"+img) for img in self.colLloc]
        self.greyimg = [pygame.image.load("./images/level1/"+img) for img in self.greyloc]
        self.miniR = [pygame.transform.scale(pygame.image.load("./images/level1/"+img),(49,38)) for img in self.colRloc]
        self.miniL = [pygame.transform.scale(pygame.image.load("./images/level1/"+img),(49,38)) for img in self.colLloc]
        self.miniG = [pygame.transform.scale(pygame.image.load("./images/level1/"+img),(49,38)) for img in self.greyloc]

    def updatevalues(self):
        for i in range(0,7):
            self.values[i] = self.index + (-3 + i)
            if self.values[i]<0:self.panel[i] = ""
            elif (self.values[i]>=len(self.sequence)):self.panel[i] = ""
            else:self.panel[i] = self.sequence[self.values[i]]
        self.index += 1
        self.currentquestion = self.panel[3]

    def pulse(self):
        if self.pulseup:self._pulseindex += 1
        else:self._pulseindex -= 1
        if self._pulseindex > 0:self.pulseup = False
        if self._pulseindex < -10:self.pulseup = True
        if abs(self._pulseindex)%2==0:self.pulseindex = int(self._pulseindex/2)
        

    def geticon(self,nucl):
        return {"A":1,"T":2,"G":3,"C":4}[nucl]

    def getcol(self,nucl):
        return {"A":0,"T":1,"G":2,"C":3}[nucl]
        
    def crosscheck(self):
        if not(self.selecteditem == self.verifier[self.currentquestion]):
            self.life -= 1
            self.showstatus[1] = False
        else:
            self.updatevalues()
            self.showstatus[1] = True

    def resetroom(self):
        self.life = 3
        self.index = 0
        self.updatevalues()
        self.firsttime = False
        

    def draw(self,display,refreshroom):
        if refreshroom:
            self.loadassets()
        font = pygame.font.SysFont("comicsansms",25)
        display.blit(self.assets[0],(0,0))
        display.blit(pygame.transform.scale(self.assets[1],(83+(2*self.pulseindex),72+(2*self.pulseindex))),(675-self.pulseindex,109-self.pulseindex))
        display.blit(pygame.transform.scale(self.assets[2],(83+(2*self.pulseindex),72+(2*self.pulseindex))),(675-self.pulseindex,209-self.pulseindex))
        display.blit(pygame.transform.scale(self.assets[3],(83+(2*self.pulseindex),72+(2*self.pulseindex))),(675-self.pulseindex,309-self.pulseindex))
        display.blit(pygame.transform.scale(self.assets[4],(83+(2*self.pulseindex),72+(2*self.pulseindex))),(675-self.pulseindex,409-self.pulseindex))
        for i in range(0, 12):
            selectedleft = self.miniL
            if i >= self.index:selectedleft = self.miniG
            display.blit(selectedleft[self.getcol(self.sequence[i])],(30,self.minipositions[i]))
            if i+1 < self.index:display.blit(self.miniR[self.getcol(self.verifier[self.sequence[i]])],(79,self.minipositions[i]))
            
        if not(self.panel[0]==""):
            display.blit(self.colL[self.getcol(self.panel[0])],(308,-60))
            display.blit(self.colR[self.getcol(self.verifier[self.panel[0]])],(406,-60))
        if not(self.panel[1]==""):
            display.blit(self.colL[self.getcol(self.panel[1])],(308,39))
            display.blit(self.colR[self.getcol(self.verifier[self.panel[1]])],(406,39))
        if not(self.panel[2]==""):
            display.blit(self.colL[self.getcol(self.panel[2])],(308,139))
            display.blit(self.colR[self.getcol(self.verifier[self.panel[2]])],(406,139))
        if not(self.panel[4]==""):display.blit(self.greyimg[self.getcol(self.panel[4])],(308,339))
        if not(self.panel[5]==""):display.blit(self.greyimg[self.getcol(self.panel[5])],(308,439))
        if not(self.panel[6]==""):display.blit(self.greyimg[self.getcol(self.panel[6])],(308,539))
        pygame.draw.rect(display,(255,255,255),(188-self.pulseindex,219-self.pulseindex,429+(2*self.pulseindex),113+(2*self.pulseindex)))
        display.blit(self.lifeindicator[self.life],(694,33))
        if not(self.currentquestion == ""):
            display.blit(self.assets[self.geticon(self.currentquestion.upper())],(208,239))
            display.blit(font.render("Drag and Drop Here",True,(0,0,0)),(349,267))
        else:
            display.blit(font.render("Congratulation !",True,(0,128,0)),(325,247))
            display.blit(font.render("You just build a double stranded DNA",True,(0,0,0)),(249,277))
        if self.life > 0:
            if self.selecteditem in ["A","T","G","C"]:
                display.blit(self.assets[self.geticon(self.selecteditem.upper())],(self.mouse_x-42,self.mouse_y-36))
        else:
            pygame.draw.rect(display,(255,255,255),(200,200,400,200))
            pygame.draw.rect(display,(128,0,0),(200,200,400,200),3)
            font2 = pygame.font.SysFont("comicsansms",50)
            text = font2.render("Level Failed!",True,(128,0,0))
            display.blit(text,(400-text.get_width()//2,300-text.get_height()//2))
            if self.mouseabovereset:pygame.draw.rect(display,(0,128,0),(350,340,110,40),1)
            display.blit(self.assets[5],(357,350))
        if self.hintactive:
            pygame.draw.rect(display,(255,255,255),(100,100,600,400))
            pygame.draw.rect(display,(0,0,128),(100,100,600,400),2)
            # hint contents ------------
            font3 = pygame.font.SysFont("comicsansms",40)
            font4 = pygame.font.SysFont("comicsansms",20)
            doub = font3.render("Double Strand",True,(0,0,128))
            introtext1 = font.render("In this game, player need to create a double",True,(0,0,0))
            introtext2 = font.render("stranded DNA from given single stranded input.",True,(0,0,0))
            hinttext = font.render("Hint",True,(0,0,128))
            ruletext = font.render("Rule",True,(0,0,128))
            hintsarray = [font4.render("Adenine",True,(0,0,0)),
                          font4.render("Thymine",True,(0,0,0)),
                          font4.render("Guanine",True,(0,0,0)),
                          font4.render("Cytosine",True,(0,0,0))]
            hintsarray2 = [font4.render("Adenine only pair with Thymine",True,(0,0,0)),
                          font4.render("Thymine only pair with Adenine",True,(0,0,0)),
                          font4.render("Guanine only pair with Cytosine",True,(0,0,0)),
                          font4.render("Cytosine only pair with Guanine",True,(0,0,0))]
            display.blit(doub,(400-doub.get_width()//2,120))
            display.blit(introtext1,(400-introtext1.get_width()//2,160))
            display.blit(introtext2,(400-introtext2.get_width()//2,180))
            display.blit(hinttext,(140,220))
            display.blit(ruletext,(330,220))
            display.blit(pygame.transform.scale(self.assets[1],(42,36)),(140,250))
            display.blit(pygame.transform.scale(self.assets[2],(42,36)),(140,300))
            display.blit(pygame.transform.scale(self.assets[3],(42,36)),(140,350))
            display.blit(pygame.transform.scale(self.assets[4],(42,36)),(140,400))
            display.blit(pygame.transform.scale(self.colL[0],(47,36)),(330,250))
            display.blit(pygame.transform.scale(self.colL[1],(47,36)),(330,300))
            display.blit(pygame.transform.scale(self.colL[2],(47,36)),(330,350))
            display.blit(pygame.transform.scale(self.colL[3],(47,36)),(330,400))
            display.blit(pygame.transform.scale(self.colR[1],(47,36)),(377,250))
            display.blit(pygame.transform.scale(self.colR[0],(47,36)),(377,300))
            display.blit(pygame.transform.scale(self.colR[3],(47,36)),(377,350))
            display.blit(pygame.transform.scale(self.colR[2],(47,36)),(377,400))
            display.blit(hintsarray[0],(190, 260))
            display.blit(hintsarray[1],(190, 310))
            display.blit(hintsarray[2],(190, 360))
            display.blit(hintsarray[3],(190, 410))
            display.blit(hintsarray2[0],(440, 260))
            display.blit(hintsarray2[1],(440, 310))
            display.blit(hintsarray2[2],(440, 360))
            display.blit(hintsarray2[3],(440, 410))
            # --------------------------
            if self.mouseabovehintbuttons[0]:pygame.draw.rect(display,(128,128,128),(480,460,100,30))
            if self.mouseabovehintbuttons[1]:pygame.draw.rect(display,(128,128,128),(590,460,100,30))
            pygame.draw.rect(display,(0,0,128),(480,460,100,30),2)
            pygame.draw.rect(display,(0,0,128),(590,460,100,30),2)
            if not(self.firsttime):
                rtext = font.render("Reload",True,(0,0,128))
                display.blit(rtext,(500,468))
            else:
                rtext = font.render("Start",True,(0,0,128))
                display.blit(rtext,(510,468))
            ctext = font.render("Close",True,(0,0,128))
            
            display.blit(ctext,(615,468))
        if self.showstatus[0]:
            if self.showstatus[1]:
                display.blit(self.assets[8],(430,450))
            else:
                display.blit(self.assets[9],(430,450))
        display.blit(pygame.transform.scale(self.assets[6],(50,50)),(670,530)) # hint
        display.blit(pygame.transform.scale(self.assets[7],(50,50)),(730,530)) # menu

class action:
    def __init__(self,parent,room):
        self.parent = parent
        self.room = room

    def update(self,events):
        if not(self.room is None):
            if not(self.room.hintactive):
                if ((self.room.life>0)and not(self.room.currentquestion=="")):
                    self.room.pulse()
                    for event in events:
                        if event.type == pygame.MOUSEMOTION:
                            mousepos = pygame.mouse.get_pos()
                            self.room.mouse_x = mousepos[0]
                            self.room.mouse_y = mousepos[1]
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self.room.mouse_down = True
                            mousepos = pygame.mouse.get_pos()
                            if ((mousepos[0]>675)and(mousepos[0]<759)): # for ATGC menu
                                if ((mousepos[1]>109)and(mousepos[1]<182)):self.room.selecteditem = "A"
                                if ((mousepos[1]>209)and(mousepos[1]<282)):self.room.selecteditem = "T"
                                if ((mousepos[1]>309)and(mousepos[1]<382)):self.room.selecteditem = "G"
                                if ((mousepos[1]>409)and(mousepos[1]<482)):self.room.selecteditem = "C"
                            if ((mousepos[1]>530)and(mousepos[1]<581)):
                                if ((mousepos[0]>670)and(mousepos[0]<721)):
                                    self.room.hintactive = True
                                    self.room.firsttime = False
                                if ((mousepos[0]>730)and(mousepos[0]<781)):
                                    self.room.parent.setRoom("levelselector")
                                    self.parent.setlevel("levelselector")
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.room.mouse_down = False
                            mousepos = pygame.mouse.get_pos()
                            if ((mousepos[0]>188)and(mousepos[0]<618)):
                                if ((mousepos[1]>219)and(mousepos[1]<333)):
                                    if not(self.room.selecteditem == ""):
                                        self.room.crosscheck()
                                        self.room.showstatus[0] = True
                                        self.room.statusval = 0
                            self.room.selecteditem = ""
                else:
                    for event in events:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousepos = pygame.mouse.get_pos()
                            if ((mousepos[0]>350)and(mousepos[0]<461)):
                                if ((mousepos[1]>340)and(mousepos[1]<380)):self.room.resetroom()
                            if ((mousepos[1]>530)and(mousepos[1]<581)):
                                if ((mousepos[0]>670)and(mousepos[0]<721)):
                                    self.room.hintactive = True
                                    self.room.firsttime = False
                                if ((mousepos[0]>730)and(mousepos[0]<781)):
                                    self.room.parent.setRoom("levelselector")
                                    self.parent.setlevel("levelselector")
                        if event.type == pygame.MOUSEMOTION:
                            mousepos = pygame.mouse.get_pos()
                            if ((mousepos[0]>350)and(mousepos[0]<461)):
                                if ((mousepos[1]>340)and(mousepos[1]<380)):self.room.mouseabovereset = True
                                else:self.room.mouseabovereset = False
                            else:
                                self.room.mouseabovereset = False
            else:
                for event in events:
                    if event.type == pygame.MOUSEMOTION:
                        mousepos = pygame.mouse.get_pos()
                        if ((mousepos[1]>460)and(mousepos[1]<491)):
                            if ((mousepos[0]>480)and(mousepos[0]<581)):self.room.mouseabovehintbuttons[0] = True
                            else:self.room.mouseabovehintbuttons[0] = False
                            if ((mousepos[0]>590)and(mousepos[0]<691)):self.room.mouseabovehintbuttons[1] = True
                            else:self.room.mouseabovehintbuttons[1] = False
                        else:
                            self.room.mouseabovehintbuttons[0] = False
                            self.room.mouseabovehintbuttons[1] = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousepos = pygame.mouse.get_pos()
                        if ((mousepos[1]>460)and(mousepos[1]<491)):
                            if ((mousepos[0]>480)and(mousepos[0]<581)):
                                self.room.hintactive = False
                                self.room.resetroom()
                            if ((mousepos[0]>590)and(mousepos[0]<691)):
                                self.room.hintactive = False
                                self.room.firsttime = False
                        if ((mousepos[1]>530)and(mousepos[1]<581)):
                            if ((mousepos[0]>670)and(mousepos[0]<721)):
                                self.room.hintactive = False
                                self.room.firsttime = False
                            if ((mousepos[0]>730)and(mousepos[0]<781)):
                                self.room.parent.setRoom("levelselector")
                                self.parent.setlevel("levelselector")
            if self.room.showstatus[0]:
                self.room.statusval += 1
                if self.room.statusval>10:
                    self.room.showstatus[0] = False
                    self.room.statusval = 0
