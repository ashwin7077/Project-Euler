# A Pythagorean triplet is a set of three natural numbers, a<b<c for which
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a+b+c = 1000
# Find the product of abc.

while True:
    for a in range(1,400):
        for b in range (2,400):
            c=1000-a-b
            if a**2+b**2==c**2:
                print("The values are:\na is",a,"\nb is",b,"\nc is",c)
                print ("The product of abc is ",a*b*c)
                break
        if a**2+b**2==c**2:
            break
    if a**2+b**2==c**2:
            break