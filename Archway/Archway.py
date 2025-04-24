from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    turn_left()
    while right_is_blocked():
        move()
    turn_right()
    for i in range(3):
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
