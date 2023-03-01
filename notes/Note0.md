# CS 70 Fall 2022
## Note 0
### By Mihir Mirchandani
---

### Review of Sets and Mathematical Notation

> A <u>set</u> is a well defined collection of objects. These objects are called elements or members of the set, and they can be anything, including numbers, letters, people, cities, and even other sets.

Sets are conventionally noted as Capital Letters.

For example:
```
A = {2, 3, 5, 7, 11}
```

If x is an element of A, then we write x ∈ A or x belongs to A.

Two sets, A and B, are equal if all the elements of A are in B and all elements of B are in A.

<br>

> <u>Cardinality</u> is defined by the size of the set.

The set A above has a cardinality of 5. Or |A| = 5

If the cardinality of a set is 0, the respective set must be the empty set denoted by 0.

The cardinality of a set may also be infinite when describing sets like all integers or all rational numbers or all prime numbers or all odd numbers.

<br>

> If every element of a set A is also in set B, then we say that A is a <u>subset</u> of B, written A ⊆ B.

> Equivalently we can write B ⊇ A, or B is a <u>superset</u> of A.

> A <u>proper subset</u> is a set A that is strictly contained in B, written as A ⊂ B, meaning that A excludes at least one element of B.

- C can never by a proper subset of C.
- 0 is a proper subset of any nonempty set A: {} ⊂ A.
- 0 is a subset of every set B: {} ⊆ B.
- Every set A is a subset of itself: A ⊆ A.

<br><br>

Intersections and Unions

> The <u>intersection</u> of a set A with a set B written as A ∩ B, is the set containing all elements which are in both A and B. Two sets are said to be <u>disjoint</u> if A∩B = 0.

<br>

> The <u>union</u> of a set A and with a set B, written as A ∪ B, is the set of all elements which are in either A or B or both.


For example, if A is the set of all positive even numbers, and B is the set of all positive odd numbers, then A∩B = /0, and A∪B = Zx<sup>+</sup>, or the set of all positive integers.

- A ∪ B = B ∪ A
- A ∪ 0 = A
- A ∩ B = B ∩ A
- A ∩ 0 = 0

<br>

> If A and B are two sets, then the <u>relative complement</u> of A in B, or the <u>set difference</u> between B and A, written as B - A or B \ A is the  set of elements in B, but not in A: B \ A = {x ∈ B | ¬(x ∈ A)}. For example,
if B = {1,2,3} and A = {3,4,5}, then B\A = {1,2}.

- A \ A = 0
- A \ 0 = A
- 0 \ A = 0

<br>

> The Cartesian product (also called the cross product) of two sets A and B, written as A × B, is the set of all pairs whose first component is an element of A and whose second component is an element of B. In set notation, A × B = {(a,b) | a ∈ A,b ∈ B}. For example, if A = {1,2,3} and B = {u, v},
then A × B = {(1,u),(1, v),(2,u),(2, v),(3,u),(3, v)}.

<br>

> Given a set S, the power set of S, denoted by P(S), is the set of all subsets of S: {T | T ⊆ S}. For example, if S = {1,2,3}, then the power set of S is: P(S) = {{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}. Note that, if |S| = k, then |P(S)| = 2<sup>k</sup>. In how many ways can you choose a subset (say, 𝑋) of 𝐴? Well, every element in 𝐴 has a choice of either being in 𝑋 or not, i.e. 2 choices. Thus there are 2<sup>n</sup> ways you can form a subset 𝑋. Thus the total number of subsets is 2<sup>n</sup>

### Mathematical Notation

> There is a compact notation for writing sums or products of large numbers of items. For example, to write
1+2+···+n, without having to say “dot dot dot”, we write ∑<sup>n</sup> <sub>i=1</sub> &nbsp; (i).

> Analogously, to write the product f(m)f(m + 1)··· f(n) we use the notation ∏n i=m f(i). For example, ∏ n i=1 (i) = 1 · 2···n is the product of the first n positive integers.

<br>

> Universal and Existential Quantifiers

There exists. For All.
1. (∀x ∈ Z)(∃y ∈ Z)(y > x)
2. (∃y ∈ Z)(∀x ∈ Z)(y > x)

Statement 1 is true. Statement 2 is false. Why??
