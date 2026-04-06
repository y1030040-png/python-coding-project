"""
File: Steeplechase.py
Name: Angela Yeh
---------------------------------

"""

from karel.stanfordkarel import *



def turn_right():
    turn_left()
    turn_left()
    turn_left()
def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    move()
    for i in range(7):
        jump()
        # east
        if front_is_clear():
            move()

def up():
    while not front_is_clear():
        # east
        turn_left()
        move()
        # north
        turn_right()
        # east 迴圈開始結束的面對方向定相同
def cross():
    # east
    if front_is_clear():
        move()
        turn_right()
        # south

def down():
    # south
    while front_is_clear():
        move()
        # south
    turn_left()
    # east

def jump():
    up()
    cross()
    down()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
