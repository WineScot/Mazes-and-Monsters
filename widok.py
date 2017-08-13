#-*- coding: utf-8 -*-

def load():
    Plansza.images.append(loadImage("plansza0.png"))

class Plansza:

    images = []

    def __init__(self,i,pos):
        self.img = Plansza.images[i]
        self.pos = pos

    def rysuj(self):
        image( self.img, self.pos.x, self.pos.y )

    '''def setPos(p):
        self.pos = p'''

class Widok:

    def __init__(self):
        self.plansze = [ [], [], [] ]

    def generuj(self):
        ''' losuje i ustawia plansze obok siebie '''

        # generuje tablicę plansz 3x3
        for i in range(3):
            self.plansze[i].extend([None, None, None])
            for j in range(3):
                self.plansze[i][j] = Plansza( 0, PVector( 550*i, 550*j ) )
                #self.plansze[i][j].rysuj()

    def rysuj(self,pos):
        pushMatrix()
        translate( -pos.x, -pos.y )
        for i in range(3):
            for j in range(3):
                self.plansze[i][j].rysuj()
        popMatrix()