import pygame
import sys

class RectangleObject:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []

    def update_dimensions(self):
        width, height = self.screen.get_size()
        button_width = width // 5
        button_height = height // 15
        for i, rect in enumerate(self.buttons):
            button_x = 0  # Position de base à (0, 0)
            button_y = i * (button_height + 10)  # Espacement vertical entre les boutons
            self.buttons[i] = pygame.Rect(button_x, button_y, button_width, button_height)

    def add_button(self):
        width, height = self.screen.get_size()
        button_width = width // 5
        button_height = height // 15
        button_x = 0  # Position de base à (0, 0)
        if self.buttons:
            last_button = self.buttons[-1]
            button_y = last_button.y + button_height + 10  # 10 pixels d'espacement entre les boutons
        else:
            button_y = 20  # Position verticale de base pour le premier bouton
        new_button = pygame.Rect(button_x, button_y, button_width, button_height)
        self.buttons.append(new_button)

    def clear_buttons(self):
        self.buttons = []

    def draw(self):
        for rect in self.buttons:
            # Dessiner l'intérieur du bouton en gris clair
            pygame.draw.rect(self.screen, (211, 211, 211), rect)  # Gris clair
            # Dessiner les bords du bouton en noir
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 3)  # Noir avec épaisseur 3

def main():
    # Initialiser Pygame
    pygame.init()

    # Définir les dimensions initiales de la fenêtre
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
    pygame.display.set_caption("Rectangle Creux Redimensionnable")

    # Créer un objet RectangleObject
    rectangle_object = RectangleObject(screen)

    # Appeler la fonction pour dessiner un bouton initial
    rectangle_object.add_button()

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                rectangle_object.update_dimensions()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Ajouter un nouveau bouton lors du clic
                rectangle_object.add_button()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    # Supprimer tous les boutons lorsque la touche 'C' est pressée
                    rectangle_object.clear_buttons()

        # Effacer l'écran avec une couleur gris foncé
        screen.fill((169, 169, 169))

        # Dessiner tous les boutons
        rectangle_object.draw()

        # Mettre à jour l'affichage
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
