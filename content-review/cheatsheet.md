
---
# Logic

Write a logical formula that describes the proposition: the square of any natural number is a natural number:∀n ∈ N,∃m ∈ N,n<sup>2</sup> = m


---
# Stable Matching
Every job can get rejected during a run of the job-proposed algorithm

Every stable matching must have a candidate that was not proposed to until the very last day. (**Discussion 2A**)

The worst case of stable matching is always 𝑛2−2𝑛+2  less than n. The best case is always 1.

In any execution of the algorithm, there is at least one candidate who only receives a single proposal.

Max rejections: (n - 1)<sup>2</sup><br>
Max rogue pairs: n(n - 1)


---
# Graphs

For trees maybe induct on vertices instead of edges. For other graphs maybe induct on edges. (**discussion 2B**)

Every tree must always have two leaves. Leaves are always degree 1. (**fa21 midterm 1**)

hypercube is bipartite. (**fa21 midterm 1**) <br>
n-dimensional hypercube is edge colorable with n colors.
n-dimensional hypercube is vertex colorable with 2 colors.

A connected acyclic graph is known as a tree (**fa21 midterm 1**)

4-color theorem: <br>
If a graph is planar, it can be colored only using 4 colors. <br>
Contrapositive is also true: <br>
If a graph can't be colored in 4 colors (requires more than 4 colors), it must be nonplanar. (**Discussion 3A**)

If a graph is planar, then it must follow that e ≤ 3v - 6.

Recall that any bipartite planar graph G = (V,E) satisfies |E| ≤ 2|V |−4.

What the frick is bijection?

| Term | no repeated vertices | no repeated edges | start = end |
| -- | -- | -- | -- |
| walk | | | |
| path | ✓ | ✓ | |
| tour | | | ✓ |
| cycle | ✓ | ✓ | ✓ |
| Eulerian Walk | | ✓ | |
| Eulerian Tour | | ✓ | ✓ |


*Note that for a cycle, there are no repeated vertices except for the start and end vertices.*

*Note an Eulerian Walk typically had even degree for every vertex or has starting and ending vertices of odd degree. (0, 2 odd degree vertices)*

A hypercube of dimension 4 and above contains K<sub>3, 3</sub> which means that it is nonplanar. This means that a hypercube of dimension 3 or less is planar.

(Euler’s formula) For every connected planar graph, v + f = e + 2

In a planar drawing, each edge is adjacent to at most 2 faces. And for a graph where the minimum length cycle is 6, each face is adjacent to at least 6 edges. Thus we have that 6f ≤ 2e. <br>
Plugging in to Euler's formula, we see that v + 2/6e ≥ e + 2 or that 2e ≤ 3v - 6. Thus the average degree is 2e/v ≤ 3 - 2/v

There is always a vertex of degree 3 at most in a connected bipartite planar graph. Recall that any bipartite planar graph G = (V,E) satisfies |E| ≤ 2|V| − 4. (You should give as tight of a bound as possible.)

To show this: 2|E| ≤ 4|V| − 8. Total degree at most 4|V| − 8. Divide by |V| to get 4 - 8 / |V|. So the total degree must have at most a little less than 4 or 3 degree.

---
# Modular Arithmetic

If you are trying to find inverse of a in mod m, it can only exist if gcd(a, m) <br>
gcd(a, a + b) = gcd(a, b) <br>
gcd(Fib(n), Fib(n - 1)) = 1

*Abridged CRT* <br>
x ≡ a (mod p) <br>
x ≡ b (mod q) <br>
⇒ x ≡ aq(q<sup>−1</sup> mod p) +bp(p<sup>−1</sup> mod q) (mod pq).

CRT can be coprime

---
# RSA
N = pq <br>
To find the private key d from the public key (N, e), we need gcd(e, (p − 1)(q − 1)) = 1


---
# Distribution

Geometric Distributions: <br>
x = 10, p = 0.04, 1 - p: 0.96 <br>
μ = 1 / p <br>
variance = σ<sup>2</sup> = (1 / p)((1 / p) - 1) <br>
= 25(24) = 600 <br>
σ = sqrt(600)


---
# CDF

A valid CDF must be nonnegative and integrate to 1.


---
# Correlation

Two events A and B are positively correlated if Pr[A∩B] > Pr[A]Pr[B].

---
