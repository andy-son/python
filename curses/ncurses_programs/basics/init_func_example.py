#!/usr/bin/env python

# based on the init_func_example.c of the ncurses example code

import curses

myscreen = curses.initscr()                 # initialize my screen
curses.raw()                                # Line buffering disabled
myscreen.keypad(True)                       # We get F1, F2 etc...
curses.noecho()                             # Don't echo() while we do getch

myscreen.addstr("Type any character to see it in bold\n")
ch = myscreen.getch()                       # If raw() hadn't been called
                                            # we have to press enter before it
                                            # gets to the program
                        
if ch == curses.KEY_F1:                     # Without keypad enabled this will
    myscreen.addstr("F1 Key pressed")       #   not get to us either
                                            # Without noech() some ugly escape
                                            # characters might have been printed
                                            # on screen
else:
    myscreen.addstr("The pressed key is ")
    myscreen.attron(curses.A_BOLD)
    myscreen.addch(ch)
    myscreen.attroff(curses.A_BOLD)

myscreen.refresh()                          # Print it on the real screen
myscreen.getch()                            # Wait for user input
curses.endwin()                           # End curses
