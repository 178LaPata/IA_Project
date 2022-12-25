import pygame
from pygame.locals import *

pygame.init()

tamanho = (800,800)
screen = pygame.display.set_mode(tamanho)
pygame.display.set_caption('RaceTracker')

#largura = screen.get_width()
#altura = screen.get_height()

fonte = pygame.font.SysFont('Corbel',35)

textColor = (255, 255, 255)

mouse = pygame.mouse.get_pos()

def escreverTexto(texto, fonte, corTexto, x, y):
    img = fonte.render(texto, True, corTexto)
    screen.blit(img, (x, y))














color_dark = (100,100,100)
pygame.draw.rect(displaysurface, color_dark, [590, 315, 80 , 30])






while True:
    screen.fill((52, 78, 91))
    pygame.display.update()
    escreverTexto("Mostrar Mapa", fonte, textColor, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


        #checks if a mouse is clicked
#        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #if the mouse is clicked on the button the game is terminated
#            if largura/2 <= mouse[0] <= largura/2+140 and altura/2 <= mouse[1] <= altura/2+40:
#                pygame.quit()        



pygame.display.update()