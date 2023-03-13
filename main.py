"""
~ Main Program

@author: Драган Ћајић
@datetime: 10:15 PM Sunday, March 12, 2023
@description:
    Start your Square Root Finder program here.
"""
import babylonian
import helper_functions as hp


def start_program():
    hp.print_menu()

    while True:
        user_input = input("Enter number -- 1 (calculate), 2 (more) or 3 (EXIT): ")

        if user_input == "":
            print("Your input is not correct! Choose numbers: 1, 2, or 3")
            continue
        # 1. Take input data and perform calculation
        elif user_input == "1":
            while True:
                # TODO: Sanitize the user input
                s = int(input("Enter integer for which you want of find square root: "))
                x0 = float(input("Please, enter your approximate value of square root: "))
                result = babylonian.find_square_root(s, x0)
                hp.print_result(s, result)

                action = input("Calculate more -- YES or NO (y/n): ")
                if action.lower() == "yes" or action.lower() == "y":
                    continue
                else:
                    break
        # 2. Perform calculation using another method
        elif user_input == "2":
            print("Dear Customer, NEW SERVICES WILL BE SOON AVAILABLE!")
        # 3. Say hello to the user and exit program
        elif user_input == "3":
            print("Dear Customer, thank you and have a nice day! :-)")
            break
        # Inform the user if his/her input were not correct!
        else:
            print("Error occurred in the program! Check your input!")
            continue


start_program()
