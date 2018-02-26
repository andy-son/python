#!/usr/bin/env python

# based on the hellow_world.c of the ncurses example code

import curses

myscreen = curses.initscr()                 # initialize my screen

myscreen.addstr("Hello World !!!")         # add string to my screen
myscreen.refresh()                          # print to the real screen
myscreen.getch()                            # wait for user input

curses.endwin()                             # close window
