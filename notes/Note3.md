# CS 70 Fall 2022
## Note 3
### By Mihir Mirchandani
---

### Define Induction?
Induction is a powerful tool which is used to establish that a statement holds for all natural numbers. Of course, there are infinitely many natural numbers — induction provides a way to reason about them by finite means.

### Sumtorial

> Prove that 1 + 2 + 3 + ... + n = n(n + 1) / 2.

**Proof By Induction**

*Base Case*: <br>
n = 0 results in the sum being 0. By the formula 0(0 + 1) / 2 is also 0 so the formula holds.

*Inductive Hypothesis*: <br>
Assume for any positive integer, k, 1 + 2 + 3 + .. + k = k(k + 1) / 2.

*Inductive Step*: <br>
The sum of numbers from 1 to k can be represented as... <br>
<u>1 + 2 + 3 + ... + k</u> + (k + 1). <br>
Notice here our summation contains our inductive hypothesis which we can plugin to get... <br>
k(k + 1) / 2 + (k + 1) <br>
= k(k + 1) / 2 + 2(k + 1) / 2 <br>
= [k(k + 1) + 2(k + 1)] / 2 <br>
= [(k + 1)(k + 2)] / 2 <br>
= [(k + 1)((k + 1)+ 1)] / 2 <br>
This is the same formula with k + 1 plugged in as k, so by induction this proof is complete.

### Theorem 3.2. For all n ∈ ℕ, n<sup>3</sup> − n is divisible by 3. Prove this.

*Base Case*: <br>
n = 0 as this is the lowest natural number. (0)<sup>3</sup> - 0 = 0 which is divisible by 3 so the base case passes.

*Inductive Hypothesis*: <br>
Assume for any k, that k<sup>3</sup> - k is divisible by 3.

*Inductive Step*: <br>
When plugging in k + 1, we arrive at (k + 1)<sup>3</sup> - (k + 1) and we must test if this is also divisible by 3 to prove that any natural number following the formula is divisible by 3. <br>
(k + 1)<sup>3</sup> - k - 1 <br>
= k<sup>3</sup> + 3k<sup>2</sup> + 3k + 1 - k - 1 <br>
= (k<sup>3</sup> - k) + 3k<sup>2</sup> + 3k <br>
Since we know k<sup>3</sup> - k is divisble by 3 from our inductive hypothesis, we can say that it is equal to 3c where c is an integer. <br>
= 3c + 3k<sup>2</sup> + 3k <br>
= 3(c + k<sup>2</sup> + k) which is divisble by 3 since c + k<sup>2</sup> + k must be an integer. <br>
Thus for any natural number, n<sup>3</sup> − n is divisible by 3

### Strengthening the induction hypothesis.

> Induction Hypothesis: Assume that the sum of the first k odd numbers is a perfect square, say m
2

Notice how this is different from saying any k odd number.

the sum of the first n odd numbers is a perfect square becomes too weak because the proof reaches a point in its induction that doesn't help us reach a perfect square. We can instead make this stronger by saying the sum of the first n odd numbers is a n<sup>2</sup>.


Proof. We proceed by induction on n.

Base Case (n = 1): The first odd number is 1, which is equal to 1<sup>2</sup>

Induction Hypothesis: Assume that the sum of the first k odd numbers is k<sup>2</sup>

Inductive Step: The (k+1)st odd number is 2k+1. Applying the Induction Hypothesis, the sum of the first k + 1 odd numbers is k<sup>2</sup> + (2k + 1) = (k + 1)<sup>2</sup>

Thus, by the principle of induction the theorem holds.

### Theorem 3.7. Every natural number n > 1 can be written as a product of one or more primes.

Proof. We proceed by induction on n. Let P(n) be the proposition that n can be written as a product of
primes. We will prove that P(n) is true for all n ≥ 2.

Base Case (n = 2): We start at n = 2. Clearly P(2) holds, since 2 is a prime number.

Induction Hypothesis: Assume P(n) is true for all 2 ≤ n ≤ k.

Inductive Step: Prove that n = k + 1 can be written as a product of primes. We have two cases: either k + 1
is a prime number, or it is not. For the first case, if k +1 is a prime number, then we are done since k + 1
is trivially the product of one prime (itself). For the second case, if k + 1 is not a prime number, then by
definition k + 1 = xy for some x,y ∈ ℤ<sup>+</sup>
satisfying 1 < x, y < k + 1. By the Induction Hypothesis, x and y
can each be written as a product of primes (since x, y ≤ n). But this implies that k + 1 can also be written as
a product of primes.
