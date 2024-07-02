# A palindromic number reads the same both ways. The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91*99. 
# Find the largest palindrome made from the product of two 3-digit numbers.

product = []
max =0 
for i in range (100,1000):
    for j in range(i,1000):
        pal = i*j
        p = str(pal)
        p = p[::-1]
        p = int(p)
        if pal == p:
            product.append(pal)
            if pal > max:
                max = pal

print("The largest palindrome number is ",max)
