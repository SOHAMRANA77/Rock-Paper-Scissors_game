import random


class logic:
    def __init__(self, U_choice):
        self.winner = None
        self.p_choice = U_choice
        self.c_choice = random.randint(1, 3)
        self.user_point = 0
        self.comp_point = 0

    def game_checker(self):
        if self.p_choice == 1 and self.c_choice == 3 or self.p_choice == 2 and self.c_choice == 1 or \
                self.p_choice == 3 and self.c_choice == 2:
            print("User is winner")
            self.user_point += 1
            self.winner = 1

        elif self.p_choice == self.c_choice:
            print("tie")
            self.winner = 0

        elif self.p_choice == 3 and self.c_choice == 1 or self.p_choice == 1 and self.c_choice == 2 or \
                self.p_choice == 2 and self.c_choice == 3:
            print("Computer is winner")
            self.comp_point += 1
            self.winner = -1

        return self.c_choice, self.winner


# if __name__ == '__main__':
#     game = logic(1)
#     c_choice, winner = game.game_checker()
#     print(c_choice)
#     print(winner)

