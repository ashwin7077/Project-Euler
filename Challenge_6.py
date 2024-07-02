# The sum of squares of the first 10 natural numbers is
# 1^2 + 2^2 +...+10^2 = 385
# The square of the sum of the first ten natural numbers is 
# (1+2+...+10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# 3025-385=2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

i=1
sum =0
square = 0
while i <= 100:
    square = square+i*i
    sum = sum+i
    i=i+1

sum = sum*sum
print("Difference is ",sum-square)