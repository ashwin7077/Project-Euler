# By listing the first six prime numbers: 2,3,5,7,11 and 13.
# We can see that the 6th prime number is 13.
# What is the 10001st prime number?
i=7
prime = [2,3,5]
while True:
    flag = 0
    if i%2==0 or i%3==0:
        flag = 1
    else: 
        for j in prime:
            if i%j==0:
                flag = 1
                break
    
    if flag==0:
        prime.append(i)

    i = i+2
    if len(prime)==10001:
        break

print("The 10,001st prime number is ",prime[10000])