import random

""" The hundreds place and above will not affect whether or not the product is divisible by 100,
    so choose random numbers below 100.  These will simulate all numbers above 100 with the same
    ones and tens place"""

def simulate(numTests):
    numTrue = 0

    for _ in range(numTests):
        x = random.randrange(100)
        y = random.randrange(100)
        z = random.randrange(100)

        if x * y * z % 100 == 0:
            numTrue += 1
        
    return 100.0 * numTrue / numTests

numTests = 10000000
print('With ' + str(numTests) + ' trials, 3 numbers are divisible by 100 ' +
    str(simulate(numTests)) + ' percent of the time')
