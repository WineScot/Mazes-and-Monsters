#-*- coding: utf-8 -*-

class Plansza:
    def __init__(self):
        pass
    
class Widok:
    
    def __init__(self):
        self.plansze = [ [], [], [] ]
    
    def generuj(self):
        ''' losuje i ustawia plansze obok siebie '''
        
        # generuje tablicę plansz 3x3
        for i in self.plansze:
            i.extend([None, None, None])
            for j in range(3):
                i[j] = Plansza()
            print(i)