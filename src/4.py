def is_palindrome(n):
    return str(n) == str(n)[::-1]

largest_palindrome = 0
factors = (0, 0)

for i in range(900, 1000):
    for j in range(900, 1000):
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product
            factors = (i, j)

print(factors[0], "*", factors[1], "=", largest_palindrome)
