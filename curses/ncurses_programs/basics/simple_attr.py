#!/usr/bin/env python

# based on the simple_attr.c of the ncurses example code

import curses
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="a c file name",
                    required=True)
args = parser.parse_args()

row = None                      # to store the number of rows of the screen
col = None                      # to store the number of columes of the screen
y = None
x = None
prev = None
ch = None

# initialize a curses screen
myscreen = curses.initscr()

# find the boundaries of the screen
(row, col) = myscreen.getmaxyx()

# read the file till we reach the end
with open(args.input) as f:
    while True:
        ch = f.read(1)
        if not ch:
            break
        # get the current cursor position
        (y, x) = myscreen.getyx()

        # if we are at the end of the screen
        if (y == (row - 1)):
            # tell the user to press a key
            myscreen.addstr("<-Press Any Key->")
            myscreen.getch()
            # clear the screen
            myscreen.clear()
            # start at the beginning of the screen
            myscreen.move(0, 0)

        # if it is / and * then only switch on bold
        if (prev == '/' and ch == '*'):
            # cut bold on
            myscreen.attron(curses.A_BOLD)
            # get the current cursor position
            (y, x) = myscreen.getyx()
            # back up one space
            myscreen.move(y, x - 1)
            # the actual priting is done here
            myscreen.addstr(prev + ch)
        else:
            myscreen.addch(ch)

        myscreen.refresh()

        # switch it off once we got * and then /
        if (prev == '*' and ch == '/'):
            myscreen.attroff(curses.A_BOLD)

        prev = ch

myscreen.addstr(row -1, 0, "<-Press Any Key->")
myscreen.getch()
curses.endwin()
