"""
Module for Player and Enemy classes.
"""

import random

import exceptions
import settings


class Enemy:
    """
    Class to determine lives and level of the enemy.
    """

    def __init__(self, level):
        """
        Initialization
        :param level: level and lives are equal at the beginning of the game.
        """
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """
        Returns the enemy attack.
        :return: int (1, 2 or 3)
        """
        return random.randint(1, 3)

    def decrease_lives(self):
        """
        Decreases lives of the enemy when the player's attack is successful.
        :return: None
        """
        self.lives -= 1
        if self.lives == 0:
            raise exceptions.EnemyDown


class Player:
    """
    Class determines the basic player's attributes and methods.
    """
    def __init__(self, name):
        """
        Initialization
        :param name: input from the user.
        Other attributes are set by constants.
        """

        self.name = name
        self.lives = settings.LIVES
        self.score = 0
        self.allowed_attacks = settings.ALLOWED_ATTACKS
        self.mode = 'normal'

    @staticmethod
    def validate_turn_input(turn):
        """
        Validates user input.
        :param turn: player attack or defense
        :return: boolean
        """
        if turn not in ['1', '2', '3']:
            print('Please, choose 1, 2 or 3.')
            return False
        return True

    @staticmethod
    def fight(attack, defense):
        """
        Method to determine the result of the fight.
        :param attack: player or enemy turn, int 1, 2 or 3
        :param defense: player of enemy turn, int 1, 2 or 3
        :return: 0, 1 or -1 to explain the result of the fight
        """
        if attack == defense:
            return 0
        elif (attack == settings.WIZARD and defense == settings.WARRIOR) \
                or (attack == settings.WARRIOR and defense == settings.ROGUE) \
                or (attack == settings.ROGUE and defense == settings.WIZARD):
            return 1
        else:
            return -1

    def decrease_lives(self):
        """
        When enemy's attack is successful, the player looses life or finishes the game.
        :return: None
        """
        self.lives -= 1
        if self.lives == 0:
            exceptions.GameOver.log_score(self)
            exceptions.GameOver.write_top_ten_scores()
            raise exceptions.GameOver

    def attack(self, enemy_obj):
        """
        Compares player's and enemy's turns to determine the outcome.
        When the attack is successful the enemy looses life.
        :param enemy_obj: object at class Enemy
        :return: None
        """
        valid_turn = False
        user_attack = None
        while not valid_turn:
            user_attack = input('Choose a character to attack:\n '
                                '1 - Wizard\n 2 - Warrior\n 3 - Rogue\n ')
            valid_turn = self.validate_turn_input(user_attack)
        user_attack = int(user_attack)

        enemy_attack = enemy_obj.select_attack()
        fight_outcome = self.fight(user_attack, enemy_attack)
        if fight_outcome == 0:
            print('It\'s a draw!')
        elif fight_outcome == 1:
            print('Your attack was successful!')
            enemy_obj.decrease_lives()
        else:
            print('You missed! Better luck next time!')

    def defend(self, enemy_obj):
        """
        Compares player's and enemy's turns to determine the outcome.
        When the attack is successful the player looses life.
        :param enemy_obj: object at class Enemy
        :return: None
        """
        valid_turn = False
        user_defense = None
        while not valid_turn:
            user_defense = input('Choose a character to defend:\n '
                                 '1 - Wizard\n 2 - Warrior\n 3 - Rogue\n ')
            valid_turn = self.validate_turn_input(user_defense)
        user_defense = int(user_defense)

        enemy_attack = enemy_obj.select_attack()
        fight_outcome = self.fight(enemy_attack, user_defense)
        if fight_outcome == 0:
            print('It\'s a draw!')
        elif fight_outcome == 1:
            print('Your defense was unsuccessful!')
            self.decrease_lives()
            print(f'You have {self.lives} live(s) left.\n')
        else:
            print('The enemy missed! Ha-ha-ha!')
