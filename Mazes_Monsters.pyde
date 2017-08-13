from widok import Widok, Plansza, load

w = None

def setup():
    size(800,640)
    load()
    global w
    w = Widok()
    w.generuj()

def draw():
    w.rysuj( PVector( mouseX, mouseY ) )
