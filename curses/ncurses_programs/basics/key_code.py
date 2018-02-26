#!/usr/bin/env python

# based on the key_code.c of the ncurses example code

import curses

myscreen = curses.initscr()
curses.cbreak()
curses.noecho()
myscreen.keypad(True)

ch = myscreen.getch()
curses.endwin()

print("The key pressed is " + str(ch))
