#!/usr/bin/env python

# based on the simple_key.c of the ncurses example code

import curses
import time

WIDTH = 30
HEIGHT = 10

choices = [
    "Choice 1",
    "Choice 2",
    "Choice 3",
    "Choice 4",
    "Exit"
]


def print_menu(menu_win, highlight):

    # the following doesn't seem to work on python 2.7, aborts
    # with a stack smaching detected error
    # it works on python 3.6
    #
    # menu_win.box(1, 1)

    x = 2
    y = 2
    for i in range(len(choices)):
        # High light the present choice
        if (highlight == i + 1):
            menu_win.attron(curses.A_REVERSE)
            menu_win.addstr(y, x, choices[i])
            menu_win.attroff(curses.A_REVERSE)
        else:
            menu_win.addstr(y, x, choices[i])
        y += 1
    menu_win.refresh()


def main():

    highlight = 1
    choice = 0

    myscreen = curses.initscr()
    myscreen.clear()
    curses.noecho()
    # Line buffering disabled. pass on everything
    curses.cbreak()
    startx = int((80 - WIDTH) / 2)
    starty = int((24 - HEIGHT) / 2)

    menu_win = curses.newwin(HEIGHT, WIDTH, starty, startx)
    menu_win.keypad(True)
    myscreen.addstr(0, 0, "Use arrow keys to go up and down, Press enter to" +
                    " select a choice")
    myscreen.refresh()

    print_menu(menu_win, highlight)

    while True:
        c = menu_win.getch()

        if c == curses.KEY_UP:
            if highlight == 1:
                highlight = len(choices)
            else:
                highlight -= 1
        elif c == curses.KEY_DOWN:
            if highlight == len(choices):
                highlight = 1
            else:
                highlight += 1
        elif c == 10:
            choice = highlight
        else:
            myscreen.addstr(24, 0, "Charcter pressed is = " + str(c) +
                            " Hopefully it can be printed as '" +
                            str(c) + "'")

        print_menu(menu_win, highlight)
      
        # User did a choice come out of the infinite loop
        if choice != 0:
            break
    
    myscreen.addstr(24, 0, "You chose choice " + str(choice) +
                    " with choice string " + str(choices[choice - 1]))
    myscreen.clrtoeol()
    myscreen.refresh()
    myscreen.getch()
    curses.endwin()

if __name__ == "__main__":
    main()
