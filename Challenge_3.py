# The prime factors of 13195 are 5,7,13 and 29.
# What is the largest prime factor of the number 600851475143?

def natural_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    for i in range (0,len(factors)-2):
        flag=0
        if factors[i]%2==0 or factors[i]%3==0:
            flag=1
        else:
            for j in range (5,factors[i],2):
                if factors[i]%j==0:
                    flag = 1
                    break
        if flag==0:
            prime.append(factors[i])
    return factors
prime = []
n = 600851475143
natural_factors_list = natural_factors(n)
print("The highest prime number is ",prime[len(prime)-1])
