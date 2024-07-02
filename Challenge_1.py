# If we listed all natural numbers below 10 that are multiple of 3 or 5 ,
# we get 3,5,6, and 9. The sum of these multiples is 23.
# Find the sum of all multiples of 3 or 5 below 1000.

sum = 0
n = 1
while n < 1000:
    if n%3==0 or n%5==0:
        sum = sum + n 
    n=n+1
print(("The sum of all the multiples of 3 or 5 below 1000"),sum)