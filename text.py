import pygame
import sys
import Button as bt


# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Scrolling Text in Movable Text Box')

# Set up font
font = pygame.font.Font(None, 30)

# Text to display
text = "This is scrolling text inside a movable box."

# Calculate the text box dimensions slightly bigger than text size
text_width, text_height = font.size(text)
padding_x = 10  # Padding for width
padding_y = 10  # Padding for height
box_width = text_width + padding_x
box_height = text_height + padding_y

# Set the (x, y) coordinates for the text box
# Adjust these coordinates based on your desired position
x = 150
y = 200

class TextBox:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scroll_speed = 2
        self.x_position = x + width

    def scroll_text(self):
        self.x_position -= self.scroll_speed
        if self.x_position < self.x - text_width:
            self.x_position = self.x + self.width

    def draw(self, screen):
        # Draw the box (no border)
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height), 0)

        # Render the text
        text_surface = font.render(text, True, BLACK)

        # Center the text vertically within the box
        y_position = self.y + (self.height - text_height) // 2

        # Blit the text within the box
        screen.blit(text_surface, (self.x_position, y_position))


# Create a movable text box
text_box = TextBox(x, y, box_width, box_height)

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()


# TRY ERROR
# Load images
background_image = pygame.image.load('Image/Background.png')  # Replace with your background image file
button_image1 = pygame.image.load('Image/start_btn.png')  # Replace with your button image file
button_image2 = pygame.image.load('Image/exit_btn.png')  # Replace with your button image file

# Resize images to fit the screen
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
button_image1 = pygame.transform.scale(button_image1, (100, 50))
button_image2 = pygame.transform.scale(button_image2, (100, 50))

# Set the heading font


# Create Button instances
start_button = bt.Button(350, 350, button_image1, 1.5)
exit_button = bt.Button(315, 400, button_image2, 1.5)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Scroll the text within the text box
    text_box.scroll_text()

    # Draw the text box and text
    text_box.draw(screen)

    if start_button.draw(screen):
        print("START")
        text = "START"
        # Scroll the text within the text box
        text_box.scroll_text()

        # Draw the text box and text
        text_box.draw(screen)
        pygame.display.flip()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
