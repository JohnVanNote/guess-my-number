#!/usr/bin/env python
#
# guess_my_number.py
#
# Simple guess my number program
#
# created by: John Van Note
#

import sys
import random

def main():
    """Main Program"""
    name = raw_input("Enter your name: ")
    print "Hello " + name
    max_range = raw_input("Enter the maximum number you would like: ")
    max_range = verify_int(max_range)

    random_num = generate_random(max_range)
    user_correct = False
    while(user_correct != True):
        user_guess = verify_int(raw_input("Take a guess: "))
        user_correct = judge(random_num, user_guess)
    return 0


def generate_random(max_range):
    """Generate's Random Number"""
    return random.randrange(max_range)


def judge(random_num, user_guess):
    """Checks"""
    if random_num == user_guess:
        print "correct, you win"
        return True
    elif random_num > user_guess:
        print "too low"
    else:
        print "too high"
    return False


def verify_int(possible_int):
    """Verifies something is an int"""
    if isinstance(possible_int, int):
        return possible_int
    if isinstance(possible_int, str):
        if possible_int.isdigit():
            return int(possible_int)
    raise TypeError(possible_int + " cannot be converted to integer.")


if __name__ == "__main__":
    main()
