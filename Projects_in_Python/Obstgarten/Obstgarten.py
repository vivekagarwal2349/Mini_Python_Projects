#!/usr/bin/env python3
"""
Simulation of the child game "Obstgarten" to calculate the profit-marking
"""

import random

NUMBER_OF_GAMES = 1000000


class Dice:
    """
    a dict for obstgarten
    """

    def __init__(self):
        " init elements for dict statistic "
        self.red = 0
        self.green = 0
        self.blue = 0
        self.yellow = 0
        self.raven = 0
        self.basket = 0


    def roll_the_dice(self) -> str:
        " returns the dicted value and increment value for statistic"
        augen = random.randint(1, 6)

        if augen == 1:
            self.red += 1
            return "red"
        elif augen == 2:
            self.green += 1
            return "green"
        elif augen == 3:
            self.blue += 1
            return "blue"
        elif augen == 4:
            self.yellow += 1
            return "yellow"
        elif augen == 5:
            self.raven += 1
            return "raven"
        else:
            self.basket += 1
            return "basket"

    def get_statistic(self) -> None:
        " print dict statistic "
        sum_of_dice = self.red + self.green + self.blue + self.yellow + self.raven + self.basket
        print(str(self.red / sum_of_dice * 100.0) + "% red apple")
        print(str(self.green / sum_of_dice * 100.0) + "% green apple")
        print(str(self.blue / sum_of_dice * 100.0) + "% blue plum")
        print(str(self.yellow / sum_of_dice * 100.0) + "% yellow pear")
        print(str(self.raven / sum_of_dice * 100.0) + "% black raven")
        print(str(self.basket / sum_of_dice * 100.0) + "% fruit basket")


class ObstgartenGame:

    def __init__(self):
        self.red_fruit = 4
        self.green_fruit = 4
        self.yellow_fruit = 4
        self.blue_fruit = 4
        self.black_raven = 5

    def reset(self):
        " reset game 'Obstgarten'"
        self.red_fruit = 4
        self.green_fruit = 4
        self.yellow_fruit = 4
        self.blue_fruit = 4
        self.black_raven = 5

    def play(self, dice=str):
        "play one time"
        if dice == 'red' and self.red_fruit > 0:
            self.red_fruit -= 1
        elif dice == 'green' and self.green_fruit > 0:
            self.green_fruit -= 1
        elif dice == 'yellow' and self.yellow_fruit > 0:
            self.yellow_fruit -= 1
        elif dice == 'blue' and self.blue_fruit > 0:
            self.blue_fruit -= 1
        elif dice == 'raven' and self.black_raven > 0:
            self.black_raven -= 1
        else:
            if self.red_fruit >= self.green_fruit and self.red_fruit >= self.yellow_fruit and self.red_fruit >= self.blue_fruit:
                self.red_fruit -= 1
            elif self.green_fruit >= self.yellow_fruit and self.green_fruit >= self.blue_fruit:
                self.green_fruit -= 1
            elif self.yellow_fruit >= self.blue_fruit:
                self.yellow_fruit -= 1
            else:
                self.blue_fruit -= 1

    def get_scor(self) -> None:
        "get actual game score"
        print("red apple:   " + str(self.red_fruit))
        print("green apple: " + str(self.green_fruit))
        print("yellow pear:  " + str(self.yellow_fruit))
        print("blue plum:   " + str(self.blue_fruit))
        print("black raven: " + str(self.black_raven))

    def get_status(self) -> str:
        "get game status"
        if self.red_fruit == 0 and self.green_fruit == 0 and self.yellow_fruit == 0 and self.blue_fruit == 0:
            return "win"
        elif self.black_raven == 0:
            return "lose"
        else:
            return "return"


def main():
    win_game = 0
    lose_game = 0

    game_dice = Dice()
    game_play = ObstgartenGame()

    for i in range(1, NUMBER_OF_GAMES):
        game_play.reset()
        while game_play.get_status() == 'return':
            dice = game_dice.roll_the_dice()
            game_play.play(dice)

        if game_play.get_status() == 'win':
            win_game += 1
        else:
            lose_game += 1

    print("")
    print("Number of Games: " + str(NUMBER_OF_GAMES))
    print("")
    print("winning games: " + str(win_game) + " - " + str(round((win_game / (win_game + lose_game)) * 100.0, 4)))
    print("losing games:  " + str(lose_game) + " - " + str(round((lose_game / (win_game + lose_game)) * 100.0, 4)))
    print("")

    print("dict statistic:")
    game_dice.get_statistic()


if __name__ == "__main__":
    main()
