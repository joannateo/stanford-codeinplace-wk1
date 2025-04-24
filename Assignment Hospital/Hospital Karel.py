from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    #needs to check if there is a beeper, then it builds 2 more
    #build another column of hospital
    while front_is_clear():
        if beepers_present():
            build_hospital()
        if front_is_clear(): #need this if condition 
            move() #don't need to use else since we will move anyway


def build_hospital():
    turn_left()
    put_2_beepers()
    turn_right()
    move()
    turn_right()
    put_beeper()
    put_2_beepers()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def put_2_beepers():
    for i in range(2):
        move()
        put_beeper()

def safe_move():
    if front_is_clear():
        move()



if __name__ == '__main__':
    main()
