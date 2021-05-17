#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program is the best guessing number game

import random


def main():
    print("Try to guess a number from 0 to 9:")

    number_random = random.randint(0, 9)

    while True:
        number_input = input()

        try:
            number_integer = int(number_input)

            if number_integer == number_random:
                print("\nCongratulations, you guessed right!")
                break
            else:
                print("\nSorry, you guessed wrong! Try again:")
        except Exception:
            print("\nThis input is invalid, please, insert an integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
