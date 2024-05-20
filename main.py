import pygame
pygame.init()

pygame.display.set_caption("New Game")
screen = pygame.display.set_mode((500, 500),pygame.RESIZABLE)
logo = pygame.image.load("Images/logo.png").convert()
pygame.display.set_caption("Emailing")
pygame.display.set_icon(logo)

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running = False
          pygame.quit()
          print("Fermeture du jeu")

    clock.tick(30)
    screen.fill("Black")
    pygame.display.flip()