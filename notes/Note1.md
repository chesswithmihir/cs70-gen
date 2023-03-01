# CS 70 Fall 2022
## Note 1
### By Mihir Mirchandani
---

### Propositional Logic

> Proposition: a statement which is either true or false.

```
These statements are all propositions:
(1) √3 is irrational.
(2) 1 + 1 = 5.
(3) Julius Caesar had 2 eggs for breakfast on his 10th birthday.

These statements are clearly not propositions:
(4) 2+2.
(5) x² + 3x = 5. [What is x?]

These statements aren’t propositions either (although some books say they are). Propositions should not
include fuzzy terms.
(6) Arnold Schwarzenegger often eats broccoli. [What is “often?”]
(7) Henry VIII was unpopular. [What is “unpopular?”]

```

### Combined Propositional Logic

```
Propositional Forms:

(1) Conjunction: P ∧ Q (P and Q)
(2) Disjunction: P ∨ Q (P or Q)
(3) Negation: ¬P (not P)
```

> A fundamental law known as the law of **the excluded middle** says that, for any proposition P, either P is true or ¬P is true (but not both).

- Thus P ∨ ¬P is always true
- P ∧ ¬P is always false, actually called a *contradiction*

### Truth Tables

| P | Q | P ∧ Q |
| ---|--- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

| P | ¬P |
|---|---|
| T | F |
| F | T |

### Implications
The most important and subtle propositional form is an implication.

> **Implication**: P ⇒ Q (“P implies Q”). This is the same as “If P, then Q.”

Here, *P* is called the hypothesis of the implication, and Q is the conclusion.

```
We encounter implications frequently in everyday life
If you stand in the rain, then you’ll get wet.
If you passed the class, you received a certificate

The first statement above would be false only if you stood in the rain but didn’t get wet. The second statement would be false only if you passed the class but didn’t receive a certificate.
```

Truth table for implication. Notice that P =⇒ Q is logically equivalent to ¬P∨Q

| P | Q | P ⇒ Q | ¬P∨Q |
|---|---|---|---|
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |


Notice P ⇒ Q is always true when P is false. This is called vacuously true because the hypothesis is false.

Here are some other ways of saying implications:

```
(1) if P, then Q;
(2) Q if P;
(3) P only if Q;
(4) P is sufficient for Q;
(5) Q is necessary for P;
(6) Q unless not P.
```

If both P implies Q and Q implies P, then this means that P iff Q.

Implication: P ⇒ Q <br>
Inverse: ¬P ⇒ ¬Q <br>
Converse: Q ⇒ P  <br>
Contrapositive: ¬Q ⇒ ¬P <br>

| P | Q | ¬P | ¬Q| P ⇒ Q | Q ⇒ P | ¬Q ⇒ ¬P | P ⇐⇒ Q |
|---|---|---|---|---|---|---|---|
| T | T | F  |F| T | T | T | T |
| T | F | F  |T| F | T | F | F |
| F | T | T  |F| T | F | T | F |
| F | F | T  |T| T | T | T | T |

Notice (P =⇒ Q) ≡ (¬Q =⇒ ¬P).

### Quantifiers

The mathematical statements you’ll see in practice will not be made up of simple propositions like “3 is odd.” Instead you’ll see statements like:

(1) For all natural numbers n, n² + n + 41 is prime. <br>
(2) If n is an odd integer, so is n<sup>3</sup>. <br>
(3) There is an integer k that is both even and odd. <br>

1. (∀x ∈ Z)(∃y ∈ Z)(x < y)
2. (∃y ∈ Z)(∀x ∈ Z)(x < y)

The first statement says that, given an integer, I can find a larger one. The second statement says something
very different: that there is a largest integer! The first statement is true, the second is not.

### Negation and De Morgan's Laws
```
¬(P∧Q) ≡ (¬P∨ ¬Q)
¬(P∨Q) ≡ (¬P∧ ¬Q)

Similarly,

¬(∀xP(x)) ≡ ∃x¬P(x)
¬(∃xP(x)) ≡ ∀x¬P(x)

And also,

¬(∀x∃yP(x, y)) ≡ ∃x¬(∃yP(x, y)) ≡ ∃x∀y¬P(x, y)
```


> A tricker example of Negation
Write the sentence “there are at least three distinct integers x that satisfy P(x)” as a proposition using quantifiers! One way to do it is

∃x∃y∃z(x != y ∧ y != z ∧ z != x ∧ P(x) ∧ P(y) ∧ P(z)).

<br><br>

> Now write the sentence “there are at most three distinct integers x that satisfy P(x)” as a proposition using quantifiers. One way to do it is

∃x∃y∃z∀d(P(d) ⇒ (d = x) ∨ (d = y) ∨ (d = z)).

> Finally, what if we want to express the sentence “there are exactly three distinct integers x that satisfy P(x)”? This is now easy: we can just use the
conjunction of the two propositions above.
