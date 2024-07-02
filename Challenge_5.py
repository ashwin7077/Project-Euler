# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# what is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
i = 20
while True:
    c = 0
    for j in range (10,20):
        if i % j !=0:
            break
        elif i%j==0:
            c=c+1
        if c == 10:
            break
    if c == 10:
        break
    i = i+20

print("The smallest number is ",i)