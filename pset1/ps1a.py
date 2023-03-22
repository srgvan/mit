#!/usr/bin/env python3


# Problem Set 1
# Name: Sergey Vardanyan
# Collaborators: N/A 
# Time: 
#

# Program that computes and prints the 1000th prime number.

# 1. Initialize some state variables
# 2. Generate all (odd) integers > 1 as candidates to be prime
# 3. For each candidate integer, test whether it is prime
#     1. One easy way to do this 
#        is to test whether any other integer > 1 evenly divides the candidate with 0 remainder. 
#        To do this, you can use modular arithmetic, 
#        for example, 
#        the expression a % b returns the remainder after dividing the integer a by the integer b.
#     2. You might think about which integers you need to check 
#        as divisors – certainly you don’t need to go beyond the candidate you are checking, 
#        but how much sooner can you stop checking?
#     4. If the candidate is prime, 
#        print out some information so you know where you are in the computation, 
#        and update the state variables
#     5. Stop when you reach some appropriate end condition. 
#        In formulating this condition, don’t forget that your program did not generate the first prime (2).

number_to_check = 3
prime_numbers_counter = 2

while prime_numbers_counter < 1000:

    number_is_prime = None

    if number_to_check % 2 == 0:
        number_to_check = number_to_check + 1
        continue

    # if number is divisible by an even number, 
    #   it is also divisible by 2, so no need to check it - skip even divisors
    for divisor in range(3,  number_to_check, 2): # 3, 5, 7, 9 
        if number_to_check % divisor == 0:
            number_is_prime = False
            break
        else:
            number_is_prime = True
            continue

    if number_is_prime:
        prime_numbers_counter = prime_numbers_counter + 1
        print(number_to_check)
    
    number_to_check = number_to_check + 1
