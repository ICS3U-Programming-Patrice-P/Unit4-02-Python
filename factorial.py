#!/usr/bin/env python3

# Created by: Patrice Pat-Odita
# Created on: Oct 31, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the factorial of that number
def main():
    # initializations
    loop_counter = 0
    factorial_answer = 1

    # Get user input
    user_number_string = input("Enter a positive number: ")
    print()

    # try catch invalid input
    try:
        # Changing string to integer
        user_number = int(user_number_string)

        # Check to see if user inputs a positive number
        if user_number > 0:

            # calculate the sum of all numbers from 0 to user number
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {0} times through loop.".format(loop_counter))
                if loop_counter >= user_number:
                    break
            print()
            print("{}! = {}".format(user_number, factorial_answer))

        else:
            print("You entered a negative number, please try again.")
    except Exception:
        print("\033[1;35;38mThis is not an integer")
    finally:
        print()
        print("\033[1;35;38mThanks for playing")


if __name__ == "__main__":
    main()
