import sys
from cx_Freeze import setup, Executable

setup(
    name="Rock,Paper,Scissors-game",
    version="1.0",
    description=""Rock, Paper, Scissors" is a classic hand game brought to life in this Python-based digital rendition. Players choose their hand symbol - rock, paper, or scissors - competing against the computer. A dynamic graphical interface enhances user experience. Scores update, displaying the victor for each round. The game employs logic and randomization, providing an engaging and interactive gaming experience. A blend of strategy, chance, and quick decision-making, it's a timeless game now in a modern, engaging format.",
    executables=[Executable("main_menu.py", base=None)]
)
