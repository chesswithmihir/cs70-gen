# CS 70 Fall 2022
## Note 10
### By Mihir Mirchandani
---

### Counting

The next major topic of this course is Probability Theory. But before learning that, you must learn counting. That is the subject of this note.

### 1 Counting Sequences
Let's start with a simple scenario. <br>
We pick k items in a set {1, 2, ..., n} taking one at a time, sampling without replacement. This means whenever we take something out of the set, the size of the set decreases by 1. <br>
If we were dealing with a set of cards (52), then the first time we take out of the set there are 52 possibilities to choose from and the second time there are 51 times to choose from. This is an example of the first rule of counting...

> **First Rule of Counting**: If an object can be made by a succession of k choices, where there are n<sub>1</sub> ways
of making the first choice, and for every way of making the first choice there are n<sub>2</sub> ways of making the
second choice, and for every way of making the first and second choice there are n<sub>3</sub> ways of making the
third choice, and so on up to the n<sub>k</sub> choice, then the total number of distinct objects that can be made in
this way is the product n<sub>1</sub> ×n<sub>2</sub> ×n<sub>3</sub> ×··· ×n<sub>k</sub>.

### 2 Counting Sets
Let's consider a slightly different problem. We would like to sample without replacement, but this time we do not care about the order in which we pick the k elements. For example, picking an Ace and then a Jack is equivalent to picking a Jack and then an Ace. This means that if we were to select 5 cards from a deck of 52 cards and we **care** about the order we will have 52 * 51 * 50 * 49 * 48 or 51! / 47! permutations of choosing 5 cards. But if we do not care about the order in our sampling then, we are eliminating all subsets of 5 cards that may repeat in any order which there are 5! of. <br>s

Let's think about this problem with a different approach. Let's think about these as bins corresponding to each 5 element subset. One bin is (1, 2, 3, 4, 5). Another bin is (5, 4, 3, 2, 1). There are exactly 5! such bins.

n choose k is also known as a binomial coefficient and can be written as n! / k!(n - k)!  Equivalently, it’s the number of ways of choosing k objects out of a total of n distinct objects, where the order of the choices does not matter.

> **Second Rule of Counting**:  Assume an object is made by a succession of choices, and the order in which
the choices are made does not matter. Let A be the set of ordered objects and let B be the set of unordered
objects. If there exists an m-to-1 function f from A to B, we can count the number of ordered objects
(pretending that the order matters) and divide by m (the number of ordered objects per unordered objects) to obtain |B|, the number of unordered objects.

### 3 Sampling with replacement

Sometimes we wish to see what would happen when we pick something out of a set, S = {1, 2, ..., n} and then put it back into the set. This is called sampling with replacement. Assume we are still picking k elements out of a set of n elements and that order matters. This creates n<sup>k</sup> sequences. Multiple trials can have the same outcome.
