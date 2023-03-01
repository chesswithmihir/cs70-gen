# Computer Science 70, Lecture 3
## By Mihir Mirchandani
---

### Lecture Summary
This lecture will focus on induction. Mathematical induction is a fundamental proof technique. It is one we use most often. It is tied to computation in the following sense. It is intimately tied to recursion. It is analyzing a loop. This is an important technique you need when analyzing programs. We will learn induction at a deeper level.

### An example
∀n ∈ ℕ, The sume of all consecutive integers from 0 to n is n(n + 1) / 2

<br>

![](https://i.ytimg.com/vi/tpkzn2e5mtI/hqdefault.jpg)

Let's make a table.

| n | summation     |
| :------------- | :------------- |
| 0       | 0       |
| 1       | 1       |
| 2       | 3       |
| 3       | 6       |
| 4       | 10      |

You can't use this table to prove all example (∀n). So we must use a recursive methodology to prove this. We know this will work for n = any k. But will it work for k + 1 and so on.

So we've checked out that for 0 and some k, that the summation from 0 to k is just k(k + 1) / 2. Now we have to check for k + 1. <br>
The summation of 0 to k + 1 must be the summation of k + k + 1. <br>
The summation of k is k(k + 1) / 2 and if we add k + 1 to this we will get (k + 1)(k + 2) / 2 which matches if we replaced k + 1 with k in our initial equation for k(k + 1) / 2. <br>
Thus k + 1 also holds under the equation and by induction the equation does indeed equal the summation of all consecutive numbers between 0 and any integer n.


### Proof by Induction on n:

We start with what we call the **base case**. To begin with for n = 0, we check if the statement is correct. <br>
Then we say **induction hypothesis**. Suppose we say for some k, we've established that for any n, there is a summation upto k where k * (k + 1) / 2 works for our our summation. <br>
Then we need an **induction step**. We want to show that the equation for this summation holds for k + 1. The equation will be k + 1)(k + 2) / 2. To prove this we must include the induction hypothesis in our induction step thus creating a relationship between our hypothesis and our induction step. <br>

### Goal of Induction

We are trying to prove that ∀n ∈ ℕ, *P*(n)

Base Case: *P*(0), a check to see if *P*(0) holds.

Induction Hypothesis: Assume P(k)

Induction Step: Show that P(k + 1) holds. In other words, once you assume P(k), show that P(k + 1) holds.

Picture it as a bunch of dominoes that you line up. As soon as you tip one over the next one tips over as well.

![](https://i.stack.imgur.com/bBHiC.png)

### Let's do another example
∀n ∈ ℕ &nbsp;&nbsp; 3 | n<sup>3</sup> + 2n

Base Case: n = 0, everything divides 0 so it works

Induction Hypothesis: Assume 3 divides k<sup>3</sup> + 2k. Let's call (k<sup>3</sup> + 2k) / 3 = z, an integer.

Induction Step: Prove that 3 divides (k + 1)<sup>3</sup> + 2(k + 1) <br>


> Remember Pascal's Triangle <br>
(a + b)<sup>2</sup> = a<sup>2</sup> + 2ab + b<sup>2</sup> <br>
(a + b)<sup>3</sup> = a<sup>3</sup> + 2a<sup>2</sup>b + 2ab<sup>2</sup> +  b<sup>3</sup> <br>

So by Pascal's Triange, (k + 1)<sup>3</sup> + 2(k + 1) <br>
= k<sup>3</sup> + 3k<sup>2</sup> + 3k + 1 + 2k + 2 <br>
= (k<sup>3</sup> + 2k) + 3k<sup>2</sup> + 3k + 3 <br>
= 3(z + k<sup>2</sup> + k + 1) which is divisible by 3, thus proving that n = k + 1 holds for this proof.

### Map coloring

> Proving 2 color proof with Induction

n = number of lines on map.

Base case: n = 0. Does this hold for no number of lines? Of course! There are no lines so no colors. We can either fill the region with a Blue or Red color.

Induction hypothesis: Holds true for k lines. Any map with k lines, can be colored using 2 colors.

Induction Step: Have k + 1 lines <br>
We temporarily delete one line. <br>
Then apply hypothesis to assume for k lines. We can 2 color this. <br>
Then we put the line we removed back.
Negate every coloring, if was red, make blue. If was blue, make red on inside. <br>
This is a valid coloring.
