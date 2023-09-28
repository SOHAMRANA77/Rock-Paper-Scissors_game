import pygame
import sys
from Button import Button
from game_logic import logic


class RockPaperScissorGame:
    def __init__(self):
        # Initialize Pygame
        self.Losser = None
        self.Winner = None
        self.game_logic = None
        self.c_choice = None
        self.winner = None
        self.scissors_button = None
        self.rock_button = None
        self.paper_button = None
        self.scissors = None
        self.paper = None
        self.rock = None
        self.tv_image_s = None
        self.tv_image_p = None
        self.tv_image_r = None
        self.background_image = None
        self.U_point = 0
        self.C_point = 0
        self.user_score_updated = False
        self.comp_score_updated = False
        pygame.init()

        # Create game window
        self.SCREEN_WIDTH = 700
        self.SCREEN_HEIGHT = 500

        # Load images
        self.load_images()

        # Resize images to fit the screen
        self.background_1st_image = pygame.transform.scale(self.background_image,
                                                           (self.SCREEN_WIDTH, self.SCREEN_HEIGHT - 100))
        self.tv_r_image = pygame.transform.scale(self.tv_image_r, (90, 80))
        self.tv_p_image = pygame.transform.scale(self.tv_image_p, (90, 80))
        self.tv_s_image = pygame.transform.scale(self.tv_image_s, (90, 80))
        self.p_win = pygame.transform.scale(self.winner, (80, 80))
        self.p_lose = pygame.transform.scale(self.loser, (80, 80))
        self.c_win = pygame.transform.scale(self.winner, (80, 80))
        self.c_lose = pygame.transform.scale(self.loser, (80, 80))

        # Create buttons
        self.create_buttons()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Rock Paper Scissors")
        self.U_choice = 0

    def load_images(self):
        self.background_image = pygame.image.load('Image/button/game_background.png')
        self.tv_image_r = pygame.image.load('Image/button_choice/rock.png')
        self.tv_image_p = pygame.image.load('Image/button_choice/Paper.png')
        self.tv_image_s = pygame.image.load('Image/button_choice/Scissor.png')
        self.rock = pygame.image.load('Image/button/rock_icon.png')
        self.paper = pygame.image.load('Image/button/paper_icon.png')
        self.scissors = pygame.image.load('Image/button/scissors_icon.png')
        try:
            self.winner = pygame.image.load('Image/button_choice/winner.png')
            self.loser = pygame.image.load('Image/button_choice/losser.png')
        except pygame.error:
            print("Error loading winner/loser images.")
            self.winner = None
            self.loser = None

    def create_buttons(self):
        self.rock_button = Button(200, 400, self.rock, 0.5)
        self.paper_button = Button(300, 400, self.paper, 0.5)
        self.scissors_button = Button(400, 400, self.scissors, 0.5)

    def run_game(self):
        run = True
        while run:
            self.screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.blit(self.background_1st_image, (0, 0))
            self.screen.blit(self.p_lose, (363, 147))
            self.screen.blit(self.c_lose, (233, 147))

            if self.c_choice is not None and self.winner is not None:
                if self.winner == 1 and not self.user_score_updated:
                    self.U_point += 1
                    self.user_score_updated = True  # Set flag to indicate score update
                elif self.winner == -1 and not self.comp_score_updated:
                    self.C_point += 1
                    self.comp_score_updated = True  # Set flag to indicate score update
                self.display_choice()
                self.display_c_choice()
                self.display_winner()

            if self.rock_button.draw(self.screen):
                self.U_choice = 1
                self.play_game()

            if self.paper_button.draw(self.screen):
                self.U_choice = 2
                self.play_game()

            if self.scissors_button.draw(self.screen):
                self.U_choice = 3
                self.play_game()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def play_game(self):
        self.game_logic = logic(self.U_choice)
        self.c_choice, self.winner = self.game_logic.game_checker()

        # Reset the score updated flags for the new round
        self.user_score_updated = False
        self.comp_score_updated = False

    def display_winner(self):
        font = pygame.font.Font(None, 50)
        u_x, u_y = 363, 147
        c_x, c_y = 233, 147
        if self.winner == 1:
            if self.U_point == 0:  # Check if not already incremented
                self.U_point += 1
            text = font.render("User wins!", True, (0, 255, 0))
            self.screen.blit(self.p_win, (u_x, u_y))
            self.screen.blit(self.c_lose, (c_x, c_y))
        elif self.winner == -1:
            if self.C_point == 0:  # Check if not already incremented
                self.C_point += 1
            text = font.render("Comp wins!", True, (255, 0, 0))
            self.screen.blit(self.p_lose, (u_x, u_y))
            self.screen.blit(self.c_win, (c_x, c_y))
        else:
            text = font.render("It's a tie!", True, (0, 0, 255))
            self.screen.blit(self.p_lose, (u_x, u_y))
            self.screen.blit(self.c_lose, (c_x, c_y))

        self.screen.blit(text, (75, 45))
        user_point = font.render(f"USER : {self.U_point}", True, (0, 0, 0))
        comp_point = font.render(f"COMP : {self.C_point}", True, (0, 0, 0))
        self.screen.blit(user_point, (500, 400))
        self.screen.blit(comp_point, (500, 450))

    def display_choice(self):
        if self.U_choice == 1:
            self.screen.blit(self.tv_r_image, (370, 275))
        elif self.U_choice == 2:
            self.screen.blit(self.tv_p_image, (370, 275))
        elif self.U_choice == 3:
            self.screen.blit(self.tv_s_image, (370, 275))

    def display_c_choice(self):
        if self.c_choice is None:
            pass
        elif self.c_choice == 1:
            self.screen.blit(self.tv_r_image, (220, 275))
        elif self.c_choice == 2:
            self.screen.blit(self.tv_p_image, (220, 275))
        elif self.c_choice == 3:
            self.screen.blit(self.tv_s_image, (220, 275))


if __name__ == "__main__":
    game = RockPaperScissorGame()
    game.run_game()
