# Computer Science 70, Lecture 2
## By Mihir Mirchandani
---

### Lecture Summary
This is a major topic for the course. We are going to be doing proofs in various forms throughout the course. And this is your opportunity to find out what proofs are.

<br>

### Definition
What are proofs?

*Proof*: A way of establishing that a proposition is true.

How do we establish that given some proposition, *P*,

ℤ⁺ means positive integers

### *P* = ∃x, y, z ∈ ℤ⁺ : x² + y² = z²

I can prove this with a case, x = 3, y = 4, z = 5.

You can write this as a program *P(x)* or function *f(x)*. Now you want to know whether the program you wrote was correct. What does it mean for a program to be correct. It means...

### ∀x *P(x)* = *f(x)*

There is a whole area called program verification. There is also circuit verifications. It's supposed to perform to certain specifications. But how do we be sure? If it is really an important circuit, how do we verify what it's supposed to do. Proofs are about taking these infinite objects and saying statements about infinitively many things. Here is how we know it is true. When you do science you say Newton's law of gravity. In some sense, it's something we accept. But we have to experiment. Try it with examples. We are trying to prove that without a doubt, unequivocally, that a proof is true. So what is the form that these propositions are going to take. Usually, it will take the form that...

### ∀x P(x) => Q(x).

This is a very general form of a statement. So for example, let's back up a lil, and show many examples of proofs. Many of us will see these proofs in high school about numbers. But, we are going to look at these behind a more complex manner and look behind the proofs, and then as we go along the course, we are going to be building up and study these proofs to understand what we are doing. These are really beautiful proofs. They are simple and we will talk about them. All these proofs are about numbers. So let's say about integers, ℤ.

### (a | b) iff ∃d : b = ad

This is what it means to divide. We may also say ¬ (a | b) if there is no such d that exists.

### ∀ a, b, c ∈ ℤ, (a | b) ∧ (a | c) => (a | b - c)
Let Proposition *P* be (a | b) ∧ (a | c)
Let Proposition *Q* be (a | b - c)
Then P(a, b, c) => Q(a, b, c)

So what are we doing. We're starting at P, but then we want to get to Q. What we want to do is take baby steps from P to Q. What you want to say is, "well actually *P* => *P1*" and *P2* => *Pn* and finally *Pn* = *Q*.

> Remember: If P => Q and Q => R, then P => R, chaining of implications
Let's do a truth table



| P | Q | R | P => Q | Q => R | P => Q ∧ Q => R | P => R |
|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T |
| F | T | T | T | T | T | T |
| T | F | T | F | T | F | T |
| F | F | T | T | T | T | T |
| T | T | F | T | F | F | F |
| F | T | F | T | F | F | T |
| T | F | F | F | T | F | F |
| F | F | F | F | T | F | T |

Remember we are not proving logical equivalence with the last 2 columns. We have to see if the second to last column implies the very last column. In other words, we are trying to see if we will ever see a T in column -2 and a F in column -1 because if that were the case, then the implication that *If P => Q and Q => R, then P => R* would not hold true.

### Back to (a | b) ∧ (a | c) => (a | (b - c))

This means...

b = a * d1

c = a * d2

b - c = (a\*d1 - a\*d2)

b - c = a \* (d1 - d2)

Therefore, a | (b - c)

Let's move onto a different proof

### ∀x ∈ ℤ, x % 2 == 1 => x² % 2 == 1

Proving that odd integers have odd squares.

Another way of writing an odd is x = 2a + 1

Prove that x² = 2b + 1, another odd integer.

x² = (2a + 1)² = 4a² + 4a + 1

x² = 2(2a² + 2a) + 1 = 2b + 1 where b = 2a² + 2a

Since x² can be represented as 2b + 1, it is odd.

This is called a direct proof. These are the simplest types of proofs.

Let's say we are proving a new statement

### (∀ d, n ∈ ℤ⁺) (d | n) ∧ n % 2 == 1 => d % 2 == 1

For all positive integers where d divides n, if n is odd, then d is odd.

n = 2a + 1, represented as an odd integer.

We want to conclude that d = 2b + 1

For this proof, we can use proof by contraposition. Using the contrapositive

*P* = (d | n) ∧ n % 2 == 1

*Q* = d % 2 == 1

We were trying to prove that **if *P*, then *Q***. However, we can now prove **if *¬Q*, then *¬P***. This is proof by contraposition. And this statement will be read...

if d is even, then n is even.

d = 2a

Since d divides n, n = d * e

n = 2a * e

n = 2b where b = (a * e)

Thus, n is even. Thus the contrapositive is true. Thus the initial implication is true. Proof is solved.

### Proof by Contradiction

Theorem R: *There are infinitely many primes*.

Wait wait wait. What is a theorem? Something that somebody proved.

>Prime Number: A natural numbers greater than 1 and has no divisors except 1 and itself

Proof: Assume that there are only finitely many primes. Assuming that the above theorem is false.

Let's even name these finite elements: P1, P2, ..., Pk

Somewhere along the way of proof, we find *Q* and *¬Q* which is a contradiction as it implies false. We have to prove that ¬R => false. So R must be true.

Remember when we starting talking about propositions, we said a proposition is either True or False, but never both. And that seemed like a big restriction because it reduces the expressivity of ambiguity.

In order to prove this theorem we will need a Lemma. **Every number greater than 1 is either prime or has a prime divisor.** This lemma can be proven with induction which we will learn more about next week.

So now, what we want to do is fill in the next steps of implications to prove a contradiction with our contradicting theory on a finite number of primes. Let's say q = p1 * p2 * p3 * p4 * ... * pn + 1

Remember q, cannot be prime because we already have a defined set of finite primes. So in our proof, we can assume q is not prime.

If q has a prime divisor, then there exists a number, Pi, such that the number divides q.

But that number must also divide q - 1.

And coming back to ∀ a, b, c ∈ ℤ, (a | b) ∧ (a | c) => (a | b - c), this means that Pi must divide (q - (q - 1)) or 1. and Pi | 1 is already a contradiction because any prime can not successfully divide a prime number. I am thinking now that the + 1 could have been any non prime number actually, because this is to say that q = p1 * p2 * p3 * p4 * ... * pn + c, where pi doesn't divide c and so c can be 1, 4, 6, ... (non-primes).

The only way this would work is if q was prime, and since q is not in the set of pre-determined primes, we have contradicted the statement that there are finite primes because q has to be a prime. And there will always be a q for every set of finite primes.

### Another Proof by Contradiction

Theorem: *√2 is irrational*

Proof: Assume for contradiction. Also remember that a rational number is a number that can be represented as a fraction between two integers.

With our proof by contradiction, let's assume √2 can be represented as a fraction a / b, a fraction in the simplest form (a and b don't share any common factors).

√2 = a / b => √2 * b = a => 2b² = a², this means that a² is even as it is equal to a factor of 2. This means a is even. Lemma. We will prove this later. Or prove it right now!!

If a is even, a = 2c. Substitute this back to √2 * b = a => √2 * b = 2 * c => b = √2 * c => b² = 2c². This means b² is even. Thus b is even. Same lemma. Thus a and b are both even and divisible by 2. But weren't a and b already in their simplest form having no 2 common factors. Contradiction!! Thus *√2 is irrational*

### Proof by cases. ∃ irrational numbers x, y such that x<sup>y</sup> is irrational

Proof:

Case 1: x = √2, y = √2 <br>
√2<sup>√2</sup> is rational in which case we are done. Who is actually going to compute this we must do Proof by cases.

Case 2: x = √2, y = √2<sup>√2</sup>
If √2<sup>√2</sup> is not a rational number, we can say it is irrational and feed this back into y an irrational number. Now we have √2<sup>√2</sup><sup>√2</sup> or √2<sup>2</sup> or 2 which we know is rational. As we can see an irrational here to the power of an assumed irrational is rational. If our assumed irrational was rational than we already know our proof is complete and we are done.
