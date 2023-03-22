from math import log, e


primes = [2, 3, 5, 7, 11, 13, 17, 
          19, 23, 29, 31, 37, 41, 
          43, 47 ,53 ,59 ,61 ,67,
          71 ,73 ,79 ,83 ,89 ,97] 

sum_of_logs = 0

for prime in primes:
    sum_of_logs += log(prime)

# Problem 2.
# Write a program that computes the sum of the logarithms of all the primes from 2 to some number 'n', 
#   and 
#   print out the sum of the logs of the primes, 
#   the number n, 
#   the ratio of these two quantities. 
# Test this for different values of n. 

print("#   Sum of the logs of the primes:", sum_of_logs)  
print("# -----------------> The number N:", 97)
print("The ratio of these two quantities:", 97 / sum_of_logs)