import pygame
import os
import random

pygame.init()

szer = 600
wys = 600
screen = pygame.display.set_mode((szer,wys))

def napisz(tekst, x, y, rozmiar) :
    cz = pygame.font.SysFont("Arial", rozmiar)
    rend = cz.render(tekst, 1, (255,100,100))
    #x = (szer - rend.get_rect().width)/2
    #y = (wys - rend.get_rect().height)/2
    screen.blit(rend, (x,y))

copokazuje = "rozrywka"

class Przeszkoda():
    def __init__(self, x, szerokosc):
        self.x = x
        self.szerokosc = szerokosc
        self.y_gora = 0
        self.wys_gora = random.randint(150,250)
        self.odstep = 200
        self.y_dol = self.wys_gora + self.odstep
        self.wys_dol = wys - self.y_dol
        self.kolor = (160,140,190)
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)
    def rysuj(self):
        pygame.draw.rect(screen, self.kolor, self.ksztalt_gora, 0)
        pygame.draw.rect(screen, self.kolor, self.ksztalt_dol, 0)
    def ruch(self, v):
        self.x = self.x - v
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)

class Helikopter():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wysokosc = 30
        self.szerokosc = 50
        self.ksztalt = pygame.Rect(self.x, self,y, self.szerokosc, self.wysokosc)
        self.grafika = pygame.image.load(os.path.join('helikopter.png'))

przeszkody = []
for i in range(21):
    przeszkody.append(Przeszkoda(i*szer/20,szer/20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0,0,0))
    if copokazuje == "menu":
        napisz("Naciśnij spację, aby zacząć",80,150,20)
        grafika = pygame.image.load(os.path.join('logo.png'))
        screen.blit(grafika, (80,110))
    elif copokazuje == "rozrywka":
        for p in przeszkody:
            p.ruch(1)
            p.rysuj()
        for p in przeszkody:
            if p.x <= -p.szerokosc:
                przeszkody.remove(p)
                przeszkody.append((Przeszkoda(szer, szer/20)))

    pygame.display.update()
