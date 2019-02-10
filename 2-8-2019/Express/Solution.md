# Solution

The product of any given three numbers will be divisible by 100 about 12.4 percent of the time.  Note that my code simulates with random numbers between 0 and 99.

This works because any number n larger than 99 can be divided by 100 to obtain a quotient q that is a multiple of 100 and a remainder r that is between 0 and 99.  When multiplying two numbers together, n1 times n2, we can use this trick to rewrite the equation as n1 * n2 = (q1 * q2) + (q1 * r2) + (q2 * r1) + (r1 * r2).  The first three terms will always be divisible by 100, so we only need to look at the fourth term to determine if n1 times n2 is divisible by 100.

This also holds for the product of three numbers, as it holds for n1 times n2, and the product of (n1, n2) times n3.

## Completed Using
- Python
- Monte Carlo Simulation