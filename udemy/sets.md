# Sets, Section 1

A set is a collection of things (object) that are referred to as elements of the set.
A = {1, 2, 3}

Natural Numbers = N
Integers = Z
Rational Numbers = Q
Irrational Numbers = Q_hat

N inside Z inside Q
Q_hat and Q make up Real numbers R

Axiom of Extension: a set is determined by what its elements are - not the order in which they might be listed or the fact that some elements might be listed more than once.

Notation:
The set of numbers such that the numbers are positive is the same thing as writing {x | x > 0}

Types of sets:
1. Universal Set: U contains all the other subsets like Z contains all integer sets so Z is a U.
2. Empty Set {}
3. Singleton Set {1}, n(A) = 1
4. Finite Set {1, 2, 3}
5. Infinite Set {..., -2, -1, 0, 1, 2, ...}
6. Subset something smaller than a set.

A = {1, 2, 3}
n(A) = 3

B = {123}
n(A) = 1

Subsets: if A and B are sets then A is a subset of B iff every element of A is also an element of B

Power sets: Power set of A is the sets of all subsets A, denoted P(A)
ie) if L = {L, M, R}, then the power set P(L) =
{
  {}, {L}, {M}, {R}, {LM}, {LR}, {MR}, {LMR},
}
2^n(L) = n(P(L))

Ordered Pairs written as a tuple:
(1, 2) != (2, 1)

Cartesian Product: Given sets A and B, the Cartesian Product of A and B, denoted A x B and read A cross B is the set of all ordered pairs (a, b) where a is in A and b is in B.

A x B = {(a, b) | a E A and b E B}

Cartesian Plane: R x R yields all the points on the 2D cartesian Plane all (r, r).

U = or (Union)
∩ = and (Intersection)

<br>

Properties of union and intersections
A U B = B U A, A ∩ B = B ∩ A

(A U B) U C = A U (B U C), (A ∩ B) ∩ C = A ∩ (B ∩ C)

A U (B ∩ C) = (A U B) ∩ (A U C), A ∩ (B U C) = (A ∩ B) U (A ∩ C)

A U {} = A, A ∩ {} = {}

A U U = U (Universal set)

A U A = A, A ∩ A = A

<br>


Partition of Sets:

Disjoint sets: Two sets are called Disjoint iff they have no elements in common.

ie) A = {1, 2} B = {3, 4}
A ∩ B = {}

Mutually Disjoint Sets: Multiple sets with all sets each having unique elements (no shared elements across any combination of sets) A1 ∩ A2 ∩ A3 ∩ ... = {}. The Venn Diagram would just me multiple circles with no intersections


Partition of Sets: a finite or infinite collection of none empty sets. {A1, A2, A3, ...} is a Partition of a set A iff
1. A is the union of all of the sets
2. the sets are mutually disjoint
