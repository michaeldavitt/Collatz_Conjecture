# Attempt at demonstrating the Collatz Conjecture that I saw on a YouTube video.
# https://www.youtube.com/watch?v=094y1Z2wpJg
# Start with any number
# If the number is odd, multiply by 3 and add 1
# If the number is even, divide by 2
# Keep going, and eventually, you will get stuck in a 4, 2, 1 loop
# Loop: 4 divided by 2 is 2, divided by 2 is 1, multiplied by 3 and add 1 is 4, then it repeats
# Need a program to accept a number from the user, then return the number of iterations before reaching 1


# function ensures that the user inputs a valid positive integer
def get_user_input():
    user_num = input("Please input a number: ")
    while not user_num.isdigit() or user_num == "0":
        user_num = input("Please enter a valid number (must be a natural number): ")

    return int(user_num)


# function to calculate the total stopping time
def stopping_time_calculator(num, stopping_time=0):
    while num != 1:

        # true if the number is odd
        if num % 2 != 0:
            num = (num * 3) + 1

        # true if the number is even
        else:
            num = num / 2

        print(num)

        stopping_time += 1

    return stopping_time


# Call functions to get number and calculate the total stopping time
init_num = get_user_input()
final_stop_time = stopping_time_calculator(init_num)

print("The total stopping time of", init_num, "is:", final_stop_time)

# comment solely to test Git