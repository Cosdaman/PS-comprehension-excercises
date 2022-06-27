# Problem 1
# This is a classic problem given in technical interviews. First solve the problem WITHOUT using list comprehension.
# "Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number.
# For Multiples of five print "Buzz". Finally, for numbers which are multiples of both three and five print "FizzBuzz".
# Include comments for each step of your script explaining the Pseudo code/what each line is doing.
# After you have solved it, write a second version of your script using list comprehension.

# generate range of numbers
for i in range(1,101):
    # check for both conditions
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
