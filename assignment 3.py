# Task 1

n = int(input('Enter a number: '))


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)


ans = factorial(n)
print(ans)

# ------------------------------------------------------------------------------------------------

# Task 2

import math

y = int(input('Enter a number: '))
print('Square root: ', math.sqrt(y))
print('Logarithm: ', math.log(y))
print('Sine: ', math.sin(y))
