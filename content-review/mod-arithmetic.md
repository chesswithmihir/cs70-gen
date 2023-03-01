> What is the remainder when 7<sup>3,000,000,000</sup> is divided by 41? <br>

7<sup>3,000,000,000</sup> (mod 41) <br>
= 7<sup>40 * 75000000</sup> (mod 41) <br>
 = 1 (mod 41) by FLT.

---

> The least common multiple of two positive numbers m and n is the smallest positive number that is a
multiple of both. What is the least common multiple of m and n in terms of m, n and d = gcd(m,n)?

nm/d. There has to be all the factors of n and m, but multiplying them together gives the factors
in d twice. We can remove them by dividing.

---

> What is the maximum number of solutions in {0,1,...,n − 1} to the equation ax = b (mod n) if gcd(n,a) = d? (Answer in terms of n and d.)

d. If b is a multiple of d, then answer is d, otherwise there are no solutions.

---


> What is the size of the range of the function f(x) = ax (mod n) where x ∈ {0,1,...,n−1} if gcd(n,a) =
d?

n/d. The multiples of d is the range of this function.

---

> For a prime p, how many numbers in {0,1,..., p <sup>2</sup> −1} have an inverse modulo p<sup>2</sup>? (Answer in terms of p.)

p(p−1). The number of values in that range that are relatively prime to p

---

> Given x and m with gcd(x,m) = d, and d = ax+bm, what is a value of z where zx = 5d (mod m)? (In
terms of some subset of the variables x,m,a,d and b.)

5a. ax = ax+bm = d (mod m) and then multiply by 5.

---

> Given x and m with gcd(x,m) = d, and d = ax+bm, what is a value of z where zx = 5d (mod m)? (In
terms of some subset of the variables x,m,a,d and b.)

5a. ax = ax+bm = d (mod m) and then multiply by 5.

---

> A fixed point of a function is a value x where f(x) = x. Consider the function f(x) = x
3
(mod mn)
for relatively prime m > 2 and n > 2. Note that x = −1, x = 0, and x = 1 are fixed points for x
3
. Find
another fixed point of f(·). (Your answer can include m, n and their inverses.)

n(n<sup>−1</sup> (mod m)) − m(m<sup>−1</sup> (mod n)). <br>
A fixed point for x<sup>3</sup> are x = 1 or x = −1. That is also true (mod m) and (mod n) as well. So, take x = 1 (mod m) and x = −1 (mod n). Thus, we have n(n<sup>−1</sup> (mod m)) − m(m<sup>−1</sup> (mod n)).
