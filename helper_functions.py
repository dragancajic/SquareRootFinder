"""
~ Helper Functions

@author: Драган Ћајић
@datetime: 11:49 PM Sunday, March 12, 2023
@description:
    Some helper functions to use in program.
"""


def print_menu():
    """Function for printing menu."""
    print("""
        M A I N  * * *  M E N U
========================================
    ~ Hello there!
    > Please, select menu option:
        Calculate square root -- press 1
        Choose another method -- press 2
        EXIT the program      -- press 3
========================================""")


def print_result(number, sqrt_value):
    """Function for printing the result"""
    print(f"""
    R E S U L T  * * *  SQUARE ROOT
========================================
~ Dear Customer, here is the result:
Square root of number {number} is: {sqrt_value}
========================================""")
    print("Square root of number {0} is: {1:.5f}".format(number, sqrt_value))


if __name__ == '__main__':
    pass
