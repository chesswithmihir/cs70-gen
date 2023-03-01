# Countability/Computability Questions I got wrong...

> Every finite set is countable.

Answer: True. It's always possible to map a finite set to a subset of ℕ, so any finite set is always countable.

---

> ℕ and 2ℕ have the same cardinality.

Answer: True. The map f(x) = 2x is a bijective map from ℕ to 2ℕ (reference the notes for more information).

---

> Every countable set is a subset of ℕ.

Answer: False. Not all countable sets need to be made up of numbers. We could have a countable set of other kinds of objects too.

---

> If A and B have the same cardinality, and B and C have the same cardinality, then A and C have the same cardinality.

Answer: True. Transitive Property.

---

> The set A = {(x,y) | x ∈ ℚ, y ∈ ℚ} is countable.

Answer: True. The Cartesian product of two countable sets is always countable (see discussion).

---

> The set ℤ \ ℕ is uncountable.

Answer: False. The set ℤ \ ℕ is a subset of the integers (namely, the set of negative integers), which is countable. The set ℤ of (positive, zero and negative) integers is countable.

---

> The set ℝ \ ℚ is uncountable.

Answer: True. If ℝ \ ℚ is countable, then ℚ ∪ (ℝ \ ℚ) = ℝ must be countable as well, which is a contradiction.

---

> The set of all (finite-length) words in the English language is uncountable.

Answer: False. The set of all finite-length words can be proven to be countable similar to how the set of all finite-length binary strings is countable; we can enumerate all strings of length i iteratively for all i = 0, 1, ...

---

> Suppose you want to prove that a program P is uncomputable. Which of the following should you do?

Answer: Show that the halting problem can be solved if P can be computed.

---

> The power set (the set of all subsets) of any infinite set is uncountable. (True/False)

Answer: True. If the infinite set has the same cardinality as the integers, we know its power set is uncountable.
If it is already uncountable, then its power set is at least as large and is thus uncountable.

---

> There is a computer program that prints all rational numbers. (True/False)

Answer: True. We can write a program to enumerate the set of rational numbers in the same manner as we
counted them

---

> A computer program can print out √2. (True/False)

Answer: True. We can calculate successive digits of √2 using say binary search and print the digits as we go

---

> There is a computer program that prints all real numbers. (True/False)

False. This would produce a listing of all the real numbers which we know does not exist due to its
uncountability

---

> There is an efficiency checking program that takes another program P and an input n and verifies that
P halts within 2n steps for all inputs of size n. (True/False)

True. We can enumerate all the inputs of size less than n and then run the program on each for 2n +1 steps and see if it halts before then.

---

**For the following, select True if computable and False if not computable.**

> Determining whether a given program P halts when given an empty input

Answer: False. We have the following reduction to the halting problem, where TestHaltEmpty is the program in question.

```
def TestHalt(P, x):
      def Q(y):
          run P(x)
          return
      return TestHaltEmpty(Q)
```
Notice that the inner program Q halts on the empty input if and only if P(x) halts.

---

> Determining whether a given program P halts on input x without executing more than 10<sup>100</sup> instructions

Answer: True. We can just run P(x)P(x) for only the first 10<sup>100</sup> instructions; this is a very very long time in practice, but it's still computable.

---

> Determining whether a given program P halts on input xx, without using more than n bits of memory (including registers, tape, and anything else can be used to store state)

Answer: True. Similarly, we can just run P(x) with only n bits of memory; if the memory ever revisits the exact same state, then we know the program will not halt, as the currently stored memory completely determines the program's future behavior.

---

> Determining whether a given program P on input x prints anything during execution

Answer: False. We have the following reduction to the halting problem, where TestPrint is the program in question.

```
def TestHalt(P, x):
      def Q(y):
          run P(x) suppressing output
          print("CS70 is the best")
      return TestPrint(Q)
```
Notice that the inner program Q will print "CS70 is the best" if and only if P(x) halts.

---

> Determining whether a given program P returns 0 for exactly 10 input values

Answer: False. We have the following reduction to the halting problem, where TestReturn10 is the program in question.
```
def TestHalt(P, x):
      def Q(y):
          run P(x)
          if 1 <= y <= 10: return 0
          else: return 1
      return TestReturn10(Q)
```
Notice that the inner program Q will return 0 for exactly 10 inputs if and only if P(x) halts.

---
