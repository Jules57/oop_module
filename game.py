"""
Module with basic game logic.
"""

from exceptions import EnemyDown, GameExit, GameOver
from models import Enemy, Player
import settings


def validate_name_input(name):
    """
    Validates user input, accepts only letters.
    :param name: string, user input
    :return: boolean
    """
    if not name.isalpha():
        print('Please, enter only letters.')
        return False
    return True


def show_menu():
    """
    Shows game menu with options.
    :return: string output
    """
    print(f'Hello! Welcome to the Wizards, Warriors and Rogues!\n'
          f'{settings.HELP_INFO}')


def show_scores():
    """
    Reads the scores.txt file and outputs the scores in console.
    :return: score records with name, date, result and mode.
    """
    with open('scores.txt', 'r', encoding='utf-8') as outfile:
        lines = outfile.readlines()
        for line in lines:
            print(line.strip())


def exit_game():
    """
    Exit game by raising custom exception.
    :return: None
    """
    raise GameExit


def show_help_info():
    """
    Show the game menu such as start, show scores, help and exit game.
    :return: None
    """
    print(f'{settings.HELP_INFO}')


def provide_options():
    """
    Shows game options and calls corresponding functions.
    :return: None
    """

    show_menu()
    user_choice = input('Tell me your choice: ').lower()
    if user_choice == 'start':
        play()
    elif user_choice == 'show scores':
        show_scores()
    elif user_choice == 'exit':
        exit_game()
    elif user_choice == 'help':
        show_help_info()


def play():
    """
    The main game process. Receives user input for name, mode and turns.
    Creates player and enemy objects depending on the mode.
    :return: None
    """
    valid_name = False
    player_name = None
    while not valid_name:
        player_name = input('Enter your name: ')
        valid_name = validate_name_input(player_name)
    player = Player(name=player_name)
    mode = input('It\'s time to choose the game mode!\n'
                 'To play the normal mode press N.\n'
                 'To try the hard mode press H.\n'
                 'Mode: ').lower()
    if mode == 'h':
        player.mode = 'hard'
        level = settings.HARD_MODE_MULTIPLIER
        enemy = Enemy(level)
    elif mode == 'n':
        level = 1
        enemy = Enemy(level)

    while True:
        try:
            player.attack(enemy)
            player.defend(enemy)
        except EnemyDown:
            level += 1
            enemy = Enemy(level)
            if mode == 'h':
                player.score += settings.HARD_MODE_SCORE_GAIN
            elif mode == 'n':
                player.score += settings.NORMAL_MODE_SCORE_GAIN
            print(f'The enemy is defeated! '
                  f'Your score is {player.score}')


if __name__ == '__main__':
    while True:
        try:
            provide_options()
        except GameOver:
            print('Game over.')

        except KeyboardInterrupt:
            print('Already bored? Come back later!')
        except GameExit:
            print('We accept your choice, and hope to see you again.')
            break
        finally:
            print('Goodbye!')
