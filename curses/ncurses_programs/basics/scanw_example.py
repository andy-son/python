#!/usr/bin/env python

# based on the scanw_example.c of the ncurses example code

import curses
import os

mesg = "Enter a string: "       # message to be appeard on the screen
enteredstr = None
row = None                      # to store the number of rows of the screen
col = None                      # to store the number of columes of the screen

# initialize a curses screen
myscreen = curses.initscr()

# get the number of rows and columns
(row, col) = myscreen.getmaxyx()

# print the message at the center of the screen
myscreen.addstr(row/2, (col - len(mesg))/2, mesg)
enteredstr = myscreen.getstr()

lines = os.getenv("LINES", row)
myscreen.addstr(lines - 2, 0, "You Entered: " + enteredstr)
myscreen.getch()
curses.endwin()
