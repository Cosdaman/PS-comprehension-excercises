# Problem 1
# This is a classic problem given in technical interviews. First solve the problem WITHOUT using list comprehension.
# "Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number.
# For Multiples of five print "Buzz". Finally, for numbers which are multiples of both three and five print "FizzBuzz".
# Include comments for each step of your script explaining the Pseudo code/what each line is doing.
# After you have solved it, write a second version of your script using list comprehension.

# generate range of numbers
def FizzBuzz1():
    for i in range(1, 101):
        # check if cleanly divisible by 3
        if i % 3 == 0:
            # checks if also cleanly divisible by 5
            if i % 5 == 0:
                print("FizzBuzz")
            print("Fizz")
        # checks if cleanly divisible by 5 but not 3
        elif i % 5 == 0:
            print("Buzz")
        # everything else
        else:
            print(i)


# solution 2
FizzBuzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i %
            3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101)]
for i in FizzBuzz:
    print(i)
