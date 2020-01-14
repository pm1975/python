import pygame
import os

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

copokazuje = "menu"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if copokazuje == "menu":
        napisz("Naciśnij spację, aby zacząć",80,150,20)
        grafika = pygame.image.load(os.path.join('logo.png'))
        screen.blit(grafika, (80,110))

    pygame.display.update()
