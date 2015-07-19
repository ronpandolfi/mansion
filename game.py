import character
import dice
import intro
import npyscreen
import curses

curses.initscr()
import menus


def newgame():
    print 'newgame!'


if __name__ == "__main__":
    c = menus.cmenu([
        {"New Game": newgame},
        {"Exit": exit},
    ], "The Mansion", "Main Menu")
    c.display()
