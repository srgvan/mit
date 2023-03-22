#!/usr/bin/env python3


from math import log


# Problem Set 1
# Name: Sergey Vardanyan
# Collaborators: N/A
# Time: 1 hour
#

# Problem 2.
# Write a program that computes the sum of the logarithms of all the primes from 2 to some number 'n',
#   and print out the sum of the logs of the primes, the number n, and the ratio of these two quantities.
# Test this for different values of n.
# You should be able to make only some small changes to your solution to Problem 1 to solve this problem as well.
#
# Hints:
# While you should see the ratio of the sum of the logs of the primes to the value n slowly get closer to 1,
# it does not approach this limit monotonically.

number_to_check = 1
prime_numbers_counter = 2  # 2 and 3 are primes
sum_of_logs = log(2) + log(3)

while prime_numbers_counter < 1000:
    number_to_check = number_to_check + 2
    number_is_prime = None

    # skip over even numbers
    if number_to_check % 2 == 0:
        continue

    # if a number is divisible by an even number,
    # it is also divisible by 2, therefor skip over even divisors
    for divisor in range(3,  number_to_check, 2):  # 3, 5, 7, 9
        if number_to_check % divisor == 0:
            number_is_prime = False
            break
        else:
            number_is_prime = True

    if number_is_prime:
        prime = number_to_check

        prime_numbers_counter = prime_numbers_counter + 1
        sum_of_logs = sum_of_logs + log(prime)


print("Sum of the logs of the primes     :", sum_of_logs)
print("The number N                      :", prime)
print("The ratio of these two quantities :", prime / sum_of_logs)
