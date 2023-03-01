# CS 70 Fall 2022
## Note 6
### By Mihir Mirchandani
---

### 1 Modular Arithmetic

if x (mod m) ≡ r then x = mq + r where 0 ≤ r ≤ m−1 <br>
Thus 29 (mod 12) ≡ 5 and 13 (mod 5) ≡ 3.

**Computation** <br>
x + y = 14 + 25 = 39 by 12 to get 3.

x−y (mod 12) is −11 (mod 12), which is 1

Again, we could have obtained this directly by simplifying first, i.e., (x (mod 12))−(y (mod 12)) ≡ 2−1 ≡ 1.

**Theorem 6.1. If a ≡ c (mod m) and b ≡ d (mod m), then a+b ≡ c+d (mod m) and a·b ≡ c·d (mod m).** <br>
Proof. We know that c = a + k · m and d = b + ℓ · m for integers k, ℓ, so c + d = a + k · m + b + ℓ · m =
a+b+ (k+ℓ)·m, which means that a+b ≡ c+d (mod m). The proof for multiplication is similar and left
as an exercise.

### 3 Bijections

A function is a mapping from a set (called the domain) of inputs A to a set of outputs B: for input x ∈ A,
f(x) must be in the set B. To denote such a function, we write f : A → B.

A bijection is a function for which every b ∈ B has a unique pre-image a ∈ A such that f(a) = b. Note that
this consists of two conditions:

1. f is onto: every b ∈ B has a pre-image a ∈ A.
2. f is one-to-one: for all a,a′ ∈ A, if f(a) = f(a′) then a = a′.

Lemma: For a finite set A, f : A → A is a bijection if there is an inverse function g : A → A such that ∀x ∈ A
g(f(x)) = x.

### 4 Inverses

Theorem 6.2. Let m, x be positive integers such that gcd(m, x) = 1. Then x has a multiplicative inverse
modulo m, and it is unique (modulo m).

Proof. Consider the sequence of m numbers 0, x,2x,...(m−1)x. We claim that these are all distinct modulo m. Since there are only m distinct values modulo m, it must then be the case that ax ≡ 1 (mod m) for
exactly one a (modulo m). This a is the unique multiplicative inverse of x.
To verify the above claim, suppose for contradiction that ax ≡ bx (mod m) for two distinct values a,b in the
range 0 ≤ b ≤ a ≤ m−1. Then we would have (a−b)x ≡ 0 (mod m), or equivalently, (a−b)x = km for
some integer k (possibly zero or negative).
However, x and m are relatively prime, so x cannot share any factors with m. This implies that a−b must be
an integer multiple of m. This is not possible, since a−b ranges between 1 and m−1.

### 5 Computing Inverses: Euclid’s Algorithm

**Theorem 6.3. Let x ≥ y > 0. Then gcd(x, y) = gcd(y, x (mod y)).**

```
algorithm gcd(x, y)
  if y = 0 then return(x)
  else return(gcd(y, x (mod y)))
```
