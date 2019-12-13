#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: September 2019
# This program is a number guessing game


def main():
    # This function does plays a game
    # Input
    number_guessed = int(input("Enter a number 0-9 to play: "))
    print(" ")
    # Process
    if number_guessed == 5:
        print("Congrats you are cool.")
    else:
        print("You are wrong, try again?.")


if __name__ == "__main__":
    main()
