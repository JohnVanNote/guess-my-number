#!/usr/bin/python
#
# guess_my_number.py
#
# simple guess my number program
#
# created by: john van note
# created on 9/11/13
#

import sys
import random

def main():
  name = raw_input( "Enter your name: " )
  print "Hello " + name
  max_range = raw_input( "Enter the maximum number you would like: " )
  if not isinstance( max_range, int ):
    print "error"

  random_num = generate_random( max_range )
  print random_num
  user_correct = False
  while( user_correct != True ):
    user_guess = int( raw_input( "Take a guess: " ))
    user_correct = judge( random_num, user_guess )
  return 0

def generate_random( max_range ):
  return random.randrange( max_range );


def judge( random_num, user_guess ):
  if random_num == user_guess:
    print "correct, you win"
    return True
  elif random_num > user_guess:
    print "too low"
  else:
    print "too high"
  return False

if __name__ == "__main__":
  main()
