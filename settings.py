"""
Module for constants for Wizards, Warriors and Rogues.
"""
LIVES = 1
SCORE = 0
WIZARD = 1
WARRIOR = 2
ROGUE = 3
ALLOWED_ATTACKS = [WIZARD, WARRIOR, ROGUE]
HARD_MODE_MULTIPLIER = 3
NORMAL_MODE_SCORE_GAIN = 5
HARD_MODE_SCORE_GAIN = NORMAL_MODE_SCORE_GAIN * HARD_MODE_MULTIPLIER
HELP_INFO = 'To start the game enter START.\n' \
            'To look through the best players enter SHOW SCORES.\n' \
            'To get additional information enter HELP.\n' \
            'To leave the game enter EXIT.\n'
