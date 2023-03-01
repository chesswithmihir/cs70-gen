# Computer Science 70, Lecture 1
## By Mihir Mirchandani
---
### Lecture Summary
Discrete Mathematics and Probability Theory is an introductory lecture that dives into the reasons for why we should study Discrete Mathematics as Computer Scientists. Coming out of the class, anyone should have the ability to be a decent problem solver. For future coursework, this means, algorithmic understanding and observation should be sharp. For industry, this means Google interviews should come easy. This course is based off the 2015 recordings posted on YouTube. Today's topic will be Proposition Logic. Scroll down to see more on our first lecture.

<br>

### Definition
When you look up Discrete on Google, you get the word meaning *careful, subtle, unobstrusive*. Then you realize you found the definition of the wrong word: *Discreet*. Discrete means *seperate and distinct*. So now we want to think about the difference between Discrete and Continuous.

<br>

### Discrete vs Continuous
```
Examples of Discrete and Continuous. {0, 1} vs [0, 1]

Discrete:
  - Natural Numbers, ℕ = {1, 2, 3, ...}
  - Integer Numbers, ℤ = {..., -2, -1, 0, 1, 2, ...}

Continuous:
  - Real Numbers, ℝ = (−∞,∞).
```

<br>

### Why study Discrete Mathematics?
It has heavily to do with Digital vs Analog. Discrete Math is the math behind digital computers. Its also the math that led to digital computers. Its the math used to do all the things we do today. Discrete Math was invented for computers and by computers. This is why in this class, we are trying to both learn discrete math, but also trying to meld it together with how it comes up in the context of computers. A lot of Discrete Math was developed long before digital computers. But today, a lot of discrete math is being developed after having digital computers. So it's a highly mashed up process. You can study math by itself, but in the context of digital computers, it is much more applied.

<br>

### Proofs
This course will heavily depend on proofs. A proof tells you if something is true or false. Try to get to the absolute level of truth. Things we do is restrict the domain a lot so that we can achieve a number of certainties. In other words, placing restrictions on the domain can provide freedoms to validate proofs with certainty. The analogy here is that True/False is heavily connected to 1/0 or programs. This is to say that proofs were mainly written for computer programs.

<br>

### Techniques
The ideas we talk about discuss history, but also techniques used across CS. Techniques are becoming more important. These techniques are used in analyzing algorithms, designing code. How do you store information on an unreliable media? How do you transmit information over an unreliable network? This is one of the most important problems in signal processing, one we learn about in our EE courses. How about cryptography and security or networks? Turns out everything I just mentioned has to do with the properties under prime numbers which are discrete structures. What we will be studying in the first half of the course is not just proofs, but also discrete structures like prime numbers. We will be learning how to solve all questions listed above. We tell you how to, in a nutshell, solve problems. This course is a template for better techniques. And why is this a CS course? Because CS is really math in action. This is Math 55, with CS applications and techniques.

<br>

### Problem Solving
Discrete Math has countless puzzles and problems and challenges, which help with problem solving. The right way to approach this is as fun. You have to think of it as fun. Because if you can, it will be easier and pleasant to learn. These problem solving skills will keep you in good standing for future courses because it is an important skill in coursework right now, but also later in life: interview questions.

<br>

### A Google interview question:

This was a popular question during interviews years ago.
```
There is a bridge in the night, its foggy.
There are 4 people who need to cross the bridge,
but remember the bridge is unsteady and missing some planks.
These 4 people have only 1 flashlight between them
and the bridge can only hold up to 2 people at a time.
Given that each person can move across the bridge in
1 minute, 2 minutes, 5 minutes, and 10 minutes respectively,
Is it possible to get everyone across from one side of
the bridge to the other in 17 minutes or less?
```

There is a solution that actually adds up to exactly 17 minutes.
```
Let Person A, B, C, and D be the people who can cross in
1, 2, 5, and 10 minutes, respectively.
A and B move across the Bridge (2 minutes)
B Comes back to bring the torchlight (2 minutes)
C and D go across the bridge (10 minutes)
A comes back with the torchlight. (1 minute)
A and B come back to join C and D on the other side (2 minutes)
2 + 2 + 10 + 1 + 2 = 17 minutes
```

<br>

### Course Policies:

You should realize that this is a fairly fast paced course. It covers a lot of material in 15 weeks. This course was started for accelerated honors students who were the brightest CS Majors. The department wanted to keep this course for important material taught in class. Sufficient mathematical maturity is needed for this class. Math 53, 54, and 55. You must have time to work on this course. This course is meant to consume 20 hours per week. The HW for the average person will be around 8 - 10 hours per week. If you find yourself falling behind, it will get worse and compound. If you feel terribly behind, take Math 55 first and come back to CS 70. Find a way to make more time for CS 70 if it's getting that bad. If at the worst, drop CS 70 and try again next semester.

<br>

### Learn:

Use TA and Office Hours Resources. Use homework parties and there should be no embarrassment when working or learning something new. It doesn't matter if you say *I don't know*. The question is *how well you get to it in the end*. I might take 2 hours to get it, but at the end of 2 hours, everything else becomes a piece of cake. This course will push your learning. There was a very accomplished sports coach who said practice with someone who's a little better than your, but its also important to practice with someone who may not be at your level. It's important to do things differently to keep up with someone who is better than you, but with someone who is not as good as you, its important to move at a comfortable pace and even teach. This course is all about proving something to someone and working with people is using your explanations to build on a proof making your ideas sharper and more valid.

<br>

### Discussion Sections

It is also important to look at the levels of TAs. You can attend multiple discussions if you want. There are easy sections, regular sections, and advanced sections. Attend all of them.

<br>

### Collaborations

Anything you write is not shared. You can collaborate to solve problems, but when writing your answers, it is your own work. his is an important line and is taken seriously. Crossing it has tremendous consequences. It is also not a good *technique*. This course is weighted such that a majority of your grade depends on your own work in examination. A poor grade in such a weighted category will lead to a failing grade. Knowing what you can do yourself is extremely important. But when you go out into the real world, the pars of the real world will greatly reward collaboration, but never cheating. Most collaboration involves leadership and integrity, the principles that all UC Berkeley students stand by.

<br>

### Today's Topic: Proposition Logic

```
A proposition is a statement that is either True or False.
```

Everyone has statements that have both True and False, and contradictory style. Sciences like Biology even have exceptions to everything. There is no absolute truth and discreteness.

```
Proposition Examples:
  1) 1 + 1 = 2, True
  2) Angles of a triangle sum to 180 degrees, True
  3) If N is a nonnegative integer, then N^2 + N + 41 is prime, True
  4) For any integer, n > 2, n can be written as a sum of 2 primes, False
  5) Washington D. C. is the capital of the U.S., True
  6) Berkeley is an interesting city, NOT A PROPOSITION
```

Example number 4: Goldbach's Conjecture, people have been working on it since 1742. No one knows the answer. However, whether this Conjecture is true or false, in either case, we know that if it's not true, then its false, or if it's not false, then its true. So it must be a proposition.

Berkeley being an interesting city is not a proposition because there might be someone who considers Berkeley uninteresting. Everything else was a proposition.

<br>

### How to denote a proposition

We always label proposition as P, so that we can refer to it as P is True or False. Instead of having to say the whole proposition. We can also label it as Q.

<br>

### Connectives:

```
Types:
AND (∧)
OR (∨)
NOT (¬)

Uses:
P ∧ Q is true iff P is true and Q is true.
P ∨ Q is false iff P is false and Q is false
¬P is true iff P is false.
(P ∧ Q) ∨ (¬R ∨ Q)
```

You can also generate a Truth Table to visualize better.
This is an OR Table.

| P | Q | P ∨ Q |
| - | - | ----- |
| True | True | True |
| False | True | True |
| True | False | True |
| False | False | False |


<br>

### Implications

One of the most important Connectives are implication, and it is in the form P implies Q (P ⇒ Q). One way of saying it is that if P is true, then Q must be true. Let's fill in the truth table for p implies q and see what it is telling us.

| P | Q | P ⇒ Q |
| - | - | ----- |
| False | False | True |
| False | True | True |
| True | False | False |
| True | True | True |

The first two in the table are vacuously true. It is true because P didn't even say anything about being true so why we should hold it to account.

<br>

Let's look at another thing. ¬Q ⇒ ¬P (Not Q implies Not P)

| P | Q | ¬Q ⇒ ¬P |
| - | - | ----- |
| False | False | True |
| False | True | True |
| True | False | False |
| True | True | True |

As we can see from both tables above, P ⇒ Q and ¬Q ⇒ ¬P yield identical boolean values. When saying P implies Q, one can also say not Q implies not P. Thus, we can label ¬Q ⇒ ¬P as the contrapositive. This maneuver is one of the most important techniques in proofs, especially when an implication is hard and its contrapositive is easy. Even though the implication and its contrapositive is completely equivalent, changing your perspective on an implication may be much simpler when validating proofs.

<br>

### Modus Ponens

```
This is Latin for method of affirming.
There is a rule of inference that you can do.
These are synonymous to implications. (⇒)
```

<br>

### Quantifiers

In many of the things we saw so far, it was just a simple proposition. Except some of them were more complex. They talked about if n is any nonnegative integer. So how do we express this in notation? You use quantifiers! For all N that is an element of a non negative integer...

### ∀ 𝓃 ∈ Z<sup>+</sup> &nbsp; &nbsp;  (𝓃<sup>2</sup> + 𝓃 + 41 is prime)

```
∀ is the universal quantifiers (for all)
∃ is the existential quantifier (there exists)
```

<br>

### Something interesting about Quantifiers

Let's say that you said

### ∃ 𝑥 ∈ ℕ &nbsp; (𝑥 > 5𝑥) &nbsp; &nbsp; (Proposition A)

If this is false, what would that be asserting? That there is no such element, meaning every x you look at has a property that 𝑥 is not > 5𝑥.

Let's define P(𝑥) to be (𝑥 > 5𝑥). ∃ 𝑥 ∈ ℕ holds for at least 1 𝑥 in the existential quantifier. Remember ∃ means there is a x, not holding for all x's like the universal quantifier, ∀.

let's say for Proposition A, you can write it as

### ¬ ∃ 𝑥 ∈ ℕ &nbsp; P(𝑥) &nbsp; &nbsp; (Proposition B)

Since Proposition A is a proposition, we can negate it and see whether it returns true or false in the form Proposition B. This is the same thing as saying Proposition C:

### ∀ 𝑥 ∈ ℕ &nbsp; ¬ P(𝑥) &nbsp; &nbsp; (Proposition C)

> Proposition B ⇔ Proposition C (if and only if)


<br>

### Negations
To negate any proposition, we must distribute the negation across.
Suppose you had the statement:

### ∃ 𝑥 ∀ 𝑦 ∈ ℕ &nbsp; P(𝑥, y) &nbsp; &nbsp; (Proposition D)

Negating this would mean

### ¬ (∃ 𝑥 ∀ 𝑦 ∈ ℕ &nbsp; P(𝑥, y)) &nbsp; &nbsp; (Proposition E)
### = &nbsp; ∀ 𝑥 ¬ (∀ 𝑦 ∈ ℕ &nbsp; P(𝑥, y)) &nbsp; &nbsp; (Proposition E)
### = &nbsp; ∀ 𝑥 ∃ 𝑦 ∈ ℕ &nbsp; ¬ P(𝑥, y) &nbsp; &nbsp; (Proposition E)
