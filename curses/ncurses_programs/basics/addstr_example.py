#!/usr/bin/env python

# based on the printw_example.c of the ncurses example code

import curses

mesg = "Just a string"          # message to be appeard on the screen
row = None                      # to store the number of rows of the screen
col = None                      # to store the number of columes of the screen

# initialize a curses screen
myscreen = curses.initscr()

# get the number of rows and columns
(row, col) = myscreen.getmaxyx()

# print the message at the center of the screen
myscreen.addstr(row/2, (col - len(mesg))/2, mesg)
myscreen.addstr(row-2, 0, "This screen has " + str(row) + " rows and " +
                str(col) + " columns\n")
myscreen.addstr("Try resizing your window(if possible) and then run this " +
                "program again")
myscreen.refresh()
myscreen.getch()
curses.endwin()
