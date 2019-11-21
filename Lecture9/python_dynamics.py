# coding=utf-8
"""
Module aimed to demonstrate dynamic nature of Python's code.
"""

import datetime


class Lecture:
    def __init__(self, no):
        self.no = no

    if datetime.datetime.now().hour > 16:
        def __str__(self):
            return f"{self.no} has finished."
    else:
        def __str__(self):
            return f"{self.no} has started."


if __name__ == '__main__':
    l9 = Lecture(9)
    print(l9)
