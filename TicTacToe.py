# -*- coding: utf-8 -*-

import random


"""
Created on %(date)s

@author: %(Alexander Schnurpfeil)s
"""


p = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def createBoard():
    board = """
               -------
               |{}|{}|{}|
               -------
               |{}|{}|{}|
               -------
               |{}|{}|{}|
               -------
            """.format(p[0], p[1], p[2], p[3], p[4], p[5],
                       p[6], p[7], p[8])
    return board


def isValidInput(position):
    if position < 1 or position > 9:
        return False
    elif p[position-1] == "X" or p[position-1] == "O":
        return False
    else:
        return True


def getPlayerSymbol(player):
    for k, v in player.items():
        return k


def getPlayerNumber(player):
    for k, v in player.items():
        return v


def updateBoard(player, position):
    p[position-1] = getPlayerSymbol(player)


def playerInput(player):
    position = -1
    while True:
        position = input("Player {}, position for {}: "
                        .format(getPlayerNumber(player),
                                getPlayerSymbol(player)))
        position = int(position)
        if isValidInput(position) is False:
            continue
        else:
            updateBoard(player, position)
            break


def hasWon(player):
    symbol = None
    for k, v in player.items():
        symbol = k
    if p[0] == p[3] == p[6] == symbol:
        return True
    elif p[1] == p[4] == p[7] == symbol:
        return True
    elif p[2] == p[5] == p[8] == symbol:
        return True
    elif p[0] == p[1] == p[2] == symbol:
        return True
    elif p[3] == p[4] == p[5] == symbol:
        return True
    elif p[6] == p[7] == p[8] == symbol:
        return True
    elif p[0] == p[4] == p[8] == symbol:
        return True
    elif p[2] == p[4] == p[6] == symbol:
        return True
    else:
        return False


if __name__ == "__main__":
    playerOne = {"X": 1}
    playerTwo = {"O": 2}

    board = createBoard()
    print(board)
    whoStarts = random.randint(1, 2)
    currentPlayer = None
    nextPlayer = None
    if whoStarts == 1:
        currentPlayer = playerOne
        nextPlayer = playerTwo
    else:
        currentPlayer = playerTwo
        nextPlayer = playerOne
    countdown = 9
    while countdown > 0:
        playerInput(currentPlayer)
        print(createBoard())
        if hasWon(currentPlayer) is True:
            break
        else:
            t = currentPlayer
            currentPlayer = nextPlayer
            nextPlayer = t
            countdown -= 1
    if countdown < 1:
        print("Nobody wins!")
    else:
        print("Player {} wins the game, congratulations!"
            .format(getPlayerNumber(currentPlayer)))
