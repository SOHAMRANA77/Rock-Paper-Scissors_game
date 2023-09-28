import pygame
import sys
from main_game_page import RockPaperScissorGame
from Button import Button

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Load images
background_image = pygame.image.load('Image/Background.png')
button_image1 = pygame.image.load('Image/start_btn.png')
button_image2 = pygame.image.load('Image/exit_btn.png')

# Resize images to fit the screen
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
button_image1 = pygame.transform.scale(button_image1, (100, 50))
button_image2 = pygame.transform.scale(button_image2, (100, 50))

# Set the heading font
font = pygame.font.Font(None, 100)

# Create Button instances
start_button = Button(265, 200, button_image1, 1.5)
exit_button = Button(265, 350, button_image2, 1.5)


class ImageButton:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))

        heading_text = font.render('Rock Paper Scissors', True, (0, 0, 0))
        screen.blit(heading_text, (0, 50))

        if start_button.draw(screen):
            print("START")
            if __name__ == "__main__":
                game = RockPaperScissorGame()
                game.run_game()

        elif exit_button.draw(screen):
            running = False
            print("EXIT")

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
