# CS 70 Fall 2022
## Note 2
### By Mihir Mirchandani
---


### Proofs

> A mathematical proof provides a means for guaranteeing that a statement is true

### Notation and Basic Facts

Integers (ℤ) are closed under addition and multiplication.

Natural Numbers (ℕ) are also closed under addition and multiplication.

Given integers a and b, we can say a divides b (a | b) iff there exists an integer q where b = aq

Lemma 2.1. Every natural number greater than one is either prime or has a prime divisor.

Lemma 2.2. If a<sup>2</sup> is even, then a is even.

> Note: we use the notation := to indicate a definition. ie) q := 6 defines variable q as having value 6.

### Direct Proof

> Theorem 2.1: For any a, b, c ∈ ℤ, if a | b and a | c, then a | (b+c).

If a | b, then b = q<sub>1</sub>a <br>
If a | c, then c = q<sub>2</sub>a <br>
b + c = q<sub>1</sub>a + q<sub>2</sub>a <br>
b + c = a(q<sub>1</sub> + q<sub>2</sub>) which is divisble by a so b + c must be divisible by a <br>
*So a | b + c*

> Theorem 2.2: Let 0 < n < 1000 be an integer. If the sum of the digits of n is divisible by 9, then n is divisible by

Let n be an integer of the form 100a + 10b + c where a, b, and c are the digits of n. <br>
We are trying to prove that if a + b + c = 9k, then 100a + 10b + c must be divisible by 9 as well. <br>
Add 99a + 9b to both sides <br>
a + b + c + 99a + 9b = 9k + 99a + 9b. <br>
100a + b + c = n = 9k + 99a + 9b = 9(k + 11a + b) <br>
This means that n is thus divisible by 9.

### Proof by Contraposition

> Note: P ⇒ Q is equivalent to its contrapositive ¬Q ⇒ ¬P

<br>

> Theorem 2.4. Let n be a positive integer and let d divide n. If n is odd then d is odd.

We can instead say if d is even (d = 2k, where k is an integer), then n is even. <br>
d = 2k <br>
From the problem, d | n, or n = dl <br>
n = (2k)l <br>
Thus n is divisible by 2 and is thus even.

> Theorem 2.5 (Pigeonhole Principle). Let n and k be positive integers. Place n objects into k boxes. If n > k, then at least one box must contain multiple objects.

If all boxes contain at most 1 pigeon, then the number of pigeons is at most the number of boxes. This must be true.

> Another fun example:
Here is an example. A quick search on the Internet reveals that the number of hairs on the human head is roughly, on average, 100000. So, we may be reasonably confident that no human has more than 500000 hairs on his or her head. On the other hand, the population of San Francisco (as of 2016) exceeds 800000. If we think of the residents of San Francisco as “pigeons” and the number of hairs on a resident’s head as the “box” into which he or she falls, then the Pigeonhole Principle allows us to conclude the intriguing fact that there are two people in San Francisco with exactly the same number of hairs on their heads!

### Proof by Contradiction

Prove P by assuming not P, then arriving at some statement R, then also arrive at some statement

> Theorem 2.6. There are infinitely many prime numbers.

Suppose Theorem 2.6 is false which means there are only finitely as many primes. <br>
Then we say that if hold a set of primes {p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>n</sub>}, then n = p<sub>1</sub> * p<sub>2</sub> * ... * p<sub>n</sub> + 1. <br>
This number is a product of all primes + 1. <br>
Since this number is the product of primes plus 1, it is outside the range of finite primes. So it cannot be a prime. However, it does not have a prime divisor. <br>
Thus we have reached a contradiction from Lemma 2.1.

> Theorem 2.7 √2 is irrational.

Assume √2 is rational. <br>
This means that √2 = a / b, where a and b are integers and a / b is a fraction in the simplest form. <br>
√2 * b = a <br>
2b<sup>2</sup> = a<sup>2</sup> <br>
From this we know that a<sup>2</sup> is even and thus a is even by Lemma 2.2. <br>
Since a is even, we can say a = 2c. <br>
Plugging this back into 2b<sup>2</sup> = (2c)<sup>2</sup> = 4c<sup>2</sup> <br>
Thus b<sup>2</sup> = 2c<sup>2</sup> and thus b<sup>2</sup> is even and thus b is even by Lemma 2.2. <br>
Earlier we defined √2 to be a rational number a / b where a and b have no common divisors however, we just established that they are both even and thus share a common factor of 2. <br>
So a / b is not the simplest form and this is a contradiction. <br>
Thus √2 must be irrational.

> Mihir's attempt at a Proof. Prove that √3 is irrational.

Let's prove by contradiction and say √3 is rational. <br>
This means that √3 can be expressed as a fraction a / b where a and b are integers and the fraction it makes is in the simplest form. <br>
√3 * b = a <br>
3 * b<sup>2</sup> = a<sup>2</sup> <br>
This means that a<sup>2</sup> has to be a multiple of 3. <br>
We must now prove that since a<sup>2</sup> is divisible by 3, a must also be divisble by 3.... <br>


*Sub-proof*: <br>
If a<sup>2</sup> is divisible by 3, then a is divisible by 3. <br>
Contrapositive: If a is not divisible by 3, then a<sup>2</sup> must not be divisible by 3. <br>
If a number is not divisible by 3, it must be of the form either 3k - 1 or 3k + 1.

Case 1: <br>
a = 3k - 1 <br>
a<sup>2</sup> = (3k - 1)<sup>2</sup> <br>
= 9k<sup>2</sup> - 6k + 1 <br>
= 3(3k<sup>2</sup> - 2k) + 1 <br>
Since this takes the form 3c + 1, a<sup>2</sup> must not be divisible by 3.

Case 2: <br>
a = 3k + 1 <br>
a<sup>2</sup> = (3k + 1)<sup>2</sup> <br>
= 9k<sup>2</sup> + 6k + 1 <br>
= 3(3k<sup>2</sup> + 2k + 1) <br>
This again takes the form 3c + 1, which means a<sup>2</sup> is not divisble by 3.

We proved the contrapositive is true: If a is not divisible by 3, then a<sup>2</sup> must not be divisible by 3.

Since the contrapositive is true in both cases, the statement that if a<sup>2</sup> is divisible by 3, then a is divisible by 3 must be true.

.....By the sub-proof, because a<sup>2</sup> is divisible by 3, this means a can be expressed as a = 3c. <br>
So 3 * b<sup>2</sup> = (3c)<sup>2</sup> = 9c<sup>2</sup>. <br>
So b<sup>2</sup> = 3c<sup>2</sup>. <br>
By the sub-proof, since b<sup>2</sup> is divisible by 3, it must be true that b must be divisible by 3. <br>
Since a and b are both divisible by 3, there is a contradiction that a / b for √3 being rational is not in its simplest form. <br>
Thus √3 must be irrational.



### Proof by Cases.

> Theorem 2.8. There exist irrational numbers x and y such that x<sup>y</sup>
is rational.

Since the theorem says there exists, we just need one case to prove this. <br>
Let x = √2 <br>
Let y = √2 <br>
Now we must solve for x<sup>y</sup> to test if it is rational. If it is we have solved the problem (Case 1). <br>
Case 1: √2<sup>√2</sup> is rational. <br>
Case 2: √2<sup>√2</sup> is irrational. <br>
With case 1 we are immediately done. Proof is solved. <br>
With case 2 we are not done but we assume √2<sup>√2</sup> is irrational. <br>
Thus we can try plugging in x = √2<sup>√2</sup>. <br>
Now we can use x = √2<sup>√2</sup>. and y = √2. <br>
Then we can say that x<sup>y</sup> is √2<sup>√2</sup><sup>√2</sup> <br>
This is √2<sup>2</sup> or 2 which is indeed rational. <br>
So in either case, Case 1 or 2, x<sup>y</sup> can be rational if x and y are ration. There exists a solution to x and y where the theorem holds.
