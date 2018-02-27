#!/usr/bin/env python

# based on the simple_color.c of the ncurses example code

import curses
import os


def print_in_middle(screen, starty, startx, width, string):
    length = None
    x = None
    y = None
    temp = None

    if screen is None:
        screen = curses.initscr()

    (y, x) = screen.getyx()
    if startx != 0:
        x = startx
    if starty != 0:
        y = starty
    if width == 0:
        width = 80

    x = startx + (width - len(string))/2
    screen.addstr(y, x, string)
    screen.refresh()


def main():
    myscreen = curses.initscr()
    (row, col) = myscreen.getmaxyx()
    lines = os.getenv("LINES", row)
    if not curses.has_colors():
        curses.endwin()
        print("Your terminal does not support color")
    else:
        # start color
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

        myscreen.attron(curses.color_pair(1))
        print_in_middle(myscreen, lines / 2, 0, 0, "Voila !!! In color ...")
        myscreen.getch()
        curses.endwin()

if __name__ == "__main__":
    main()
