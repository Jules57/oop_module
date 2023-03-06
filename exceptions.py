"""
Module for exceptions for Wizards, Warriors and Rogues.
"""
import datetime


class GameOver(Exception):
    """
    Exception to catch the end of the game when the player goes out of lives.
    """
    @classmethod
    def log_score(cls, player_obj):
        """
        Func to write the game score after the end of the round.
        :param player_obj: it's needed to access the Player class attributes
        :return: None
        """

        with open('scores.txt', 'a+', encoding='utf-8') as outfile:
            outfile.write(
                    f'x '
                    f'{player_obj.name} '
                    f'{datetime.datetime.now().strftime("%Y-%m-%d")} '
                    f'{player_obj.score} '
                    f'{player_obj.mode}\n'
            )

    @staticmethod
    def sort_file():
        """
        Reads the scores file, processes it and sorts out by score value.
        :return: list of records sorted by scores
        """
        with open('scores.txt', 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
            sorted_scores = []
            for elem in lines:
                elem = elem.split()
                single_list = [elem[0], elem[1], elem[2], elem[3], elem[4]]
                sorted_scores.append(single_list)
            sorted_scores.sort(key=lambda x: x[3], reverse=True)
        return sorted_scores

    @staticmethod
    def write_top_ten_scores():
        """
        This func calls sort_file and gets the sorted lists
        of records to write the ten top of them into the file.
        :return: None
        """

        score_lists = GameOver.sort_file()
        with open('scores.txt', 'w+', encoding='utf-8') as outfile:
            for i in range(0, 10):
                try:
                    outfile.write(f'{i + 1:^3}'
                                  f'{score_lists[i][1]:^20} '
                                  f'{score_lists[i][2]:^35} '
                                  f'{score_lists[i][3]:^10} '
                                  f'{score_lists[i][4]:^15}\n')
                except IndexError:
                    break


class EnemyDown(Exception):
    """
    Exception to stop the game when the enemy is defeated.
    """


class GameExit(Exception):
    """
    Exception to stop the game by user's choice.
    """
