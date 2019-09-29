#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# This program calculates the cost of a pizza by getting the diameter.

import ugame
import stage

# an image bank for CircuitPython
bank = stage.Bank.from_bmp16("ball.bmp")


def main():
    # this function sets the backround

    # sets the backround to the image 0 in the bank
    # if your 0 image is magenta, your backround will most lickley be distorted
    # backrounds do not have megenta as a transparent color
    background = stage.Grid(bank, 10, 8)
    # changes (0,0) image to the thrid image
    ball = stage.Sprite(bank, 4, 3, 3)

    # create a stage for the backround to show up on
    #     and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, 60)
    # set the backround layer
    game.layers = [ball, background]
    # render the backround
    # most likely you will only render backound once per scene
    game.render_block()


if __name__ == "__main__":
    main()
