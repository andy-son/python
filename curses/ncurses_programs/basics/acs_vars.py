#!/usr/bin/env python

# based on the hellow_world.c of the ncurses example code

import curses

myscreen = curses.initscr()                 # initialize my screen

myscreen.addstr("Upper left corner           ")
myscreen.addch(curses.ACS_ULCORNER)
myscreen.addstr("\n")

myscreen.addstr("Lower left corner           ")
myscreen.addch(curses.ACS_LLCORNER)
myscreen.addstr("\n")

myscreen.addstr("Upper right corner          ")
myscreen.addch(curses.ACS_URCORNER)
myscreen.addstr("\n")

myscreen.addstr("Lower right corner          ")
myscreen.addch(curses.ACS_LRCORNER)
myscreen.addstr("\n")

myscreen.addstr("Tee pointing right          ")
myscreen.addch(curses.ACS_LTEE)
myscreen.addstr("\n")

myscreen.addstr("Tee pointing left           ")
myscreen.addch(curses.ACS_RTEE)
myscreen.addstr("\n")

myscreen.addstr("Tee pointing up             ")
myscreen.addch(curses.ACS_BTEE)
myscreen.addstr("\n")

myscreen.addstr("Tee pointing down           ")
myscreen.addch(curses.ACS_TTEE)
myscreen.addstr("\n")

myscreen.addstr("Horizontal line             ")
myscreen.addch(curses.ACS_HLINE)
myscreen.addstr("\n")

myscreen.addstr("Vertical line               ")
myscreen.addch(curses.ACS_VLINE)
myscreen.addstr("\n")

myscreen.addstr("Large Plus or cross over    ")
myscreen.addch(curses.ACS_PLUS)
myscreen.addstr("\n")

myscreen.addstr("Scan Line 1                 ")
myscreen.addch(curses.ACS_S1)
myscreen.addstr("\n")

myscreen.addstr("Scan Line 3                 ")
myscreen.addch(curses.ACS_S3)
myscreen.addstr("\n")

myscreen.addstr("Scan Line 7                 ")
myscreen.addch(curses.ACS_S7)
myscreen.addstr("\n")

myscreen.addstr("Scan Line 9                 ")
myscreen.addch(curses.ACS_S9)
myscreen.addstr("\n")

myscreen.addstr("Diamond                     ")
myscreen.addch(curses.ACS_DIAMOND)
myscreen.addstr("\n")

myscreen.addstr("Checker board (stipple)     ")
myscreen.addch(curses.ACS_CKBOARD)
myscreen.addstr("\n")

myscreen.addstr("Degree Symbol               ")
myscreen.addch(curses.ACS_DEGREE)
myscreen.addstr("\n")

myscreen.addstr("Plus/Minus Symbol           ")
myscreen.addch(curses.ACS_PLMINUS)
myscreen.addstr("\n")


myscreen.addstr("Bullet                      ")
myscreen.addch(curses.ACS_BULLET)
myscreen.addstr("\n")

myscreen.addstr("Arrow Pointing Left         ")
myscreen.addch(curses.ACS_LARROW)
myscreen.addstr("\n")

myscreen.addstr("Arrow Pointing Right        ")
myscreen.addch(curses.ACS_RARROW)
myscreen.addstr("\n")

myscreen.addstr("Arrow Pointing Down         ")
myscreen.addch(curses.ACS_DARROW)
myscreen.addstr("\n")

myscreen.addstr("Arrow Pointing Up           ")
myscreen.addch(curses.ACS_UARROW)
myscreen.addstr("\n")

myscreen.addstr("Board of squares            ")
myscreen.addch(curses.ACS_BOARD)
myscreen.addstr("\n")

myscreen.addstr("Lantern Symbol              ")
myscreen.addch(curses.ACS_LANTERN)
myscreen.addstr("\n")

myscreen.addstr("Solid Square Block          ")
myscreen.addch(curses.ACS_BLOCK)
myscreen.addstr("\n")

myscreen.addstr("Less/Equal sign             ")
myscreen.addch(curses.ACS_LEQUAL)
myscreen.addstr("\n")

myscreen.addstr("Greater/Equal sign          ")
myscreen.addch(curses.ACS_GEQUAL)
myscreen.addstr("\n")

myscreen.addstr("Pi                          ")
myscreen.addch(curses.ACS_PI)
myscreen.addstr("\n")

myscreen.addstr("Not equal                   ")
myscreen.addch(curses.ACS_NEQUAL)
myscreen.addstr("\n")

myscreen.addstr("UK pound sign               ")
myscreen.addch(curses.ACS_STERLING)
myscreen.addstr("\n")

myscreen.refresh()
myscreen.getch()

curses.endwin()                             # close window
