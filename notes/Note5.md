# CS 70 Fall 2022
## Note 5
### By Mihir Mirchandani
---

### Graph Theory, an Introduction

In the case of the internet, this network or graph specifies how web pages link to one another. In the case
of the brain, it is the interconnection network between neurons. We can describe these ideas in the beautiful
framework of graph theory, which is the subject of this lecture.

### An example

As the residents of the city, nowadays Kaliningrad, Russia, took their evening walks, many
would try to solve the challenge of picking a route that would cross each of the seven bridges precisely once
and return to the starting point.

![Figure 1](/Users/mihir/Desktop/git/cs70/images/graph1.png)

Figure 1: (Left) The city of Königsberg. (Right) The (multi-)graph modeling the bridge connections in
Königsberg. In 1736, the brilliant mathematician Leonhard Euler proved this task to be impossible.

### Formal definitions

Formally, a (undirected) graph is defined by a set of vertices V and a set of edges E. The vertices correspond
to the little circles in Figure 1 above, and the edges correspond to the line segments between the vertices. In Figure 1, V = {A,B,C,D} and E = {{A,B}, {A,B}, {A,C}, {B,C}, {B,D}, {B,D}, {C,D}}.

Note that here E is a multi-set (a set where an element can appear multiple times). We will generally not consider such a situation of multiple edges between a single pair of vertices, so in our definition, we require E to be a set, not a multi-set. Between any pair of vertices there must be either 0 or 1 edge. If there are multiple edges <br>

### Directed Graphs

![Figure 2](/Users/mihir/Desktop/git/cs70/images/graph2.png)

Note that each edge in G1 has a direction specified by an arrow. Such graphs are useful in modeling one-way relationships, such as one-way streets between two locations, and are called directed. For undirected graphs we drop the ordered pair notation for edges, and simply denote the edge between u and v by the set {u, v}.

Moving on with our example, we say that edge e = {u, v} (or e = (u, v)) is incident on vertices u and v, and that u and v are neighbors or adjacent.

If G is undirected, then the degree of vertex u ∈ V is the number
of edges incident to u, i.e., degree(u) = |{v ∈ V : {u, v} ∈ E}|.

A directed graph, on the other hand, has two different notions of degree due to the directions on the edges.
Specifically, the in-degree of a vertex u is the number of edges from other vertices to u, and the out-degree
of u is the number of edges from u to other vertices.

Thus, here and in general in these notes, we shall assume that our graphs have no self-loops,
unless stated otherwise. We shall also not allow multiple edges between a pair of vertices (unlike the case
of the Seven Bridges of Königsberg).

### Paths, walks, and cycles.
A **path** in G is a sequence of edges
{v1, v2},{v2, v3},...,{vn−2, vn−1},{vn−1, vn}. In this case we say that there is a path between v1 and vn.

A **cycle** (or circuit) is a sequence of edges {v1, v2},{v2, v3},...,{vn−2, vn−1},{vn−1, vn},{vn, v1}, where v1,..., vn are distinct.

A **walk** is a sequence of edges and vertices that may repeat to arrive finally from one vertex to another. It can look a lot like a random leisurely stroll.

Here is a table to represent everything much easier. <br>

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

One more definition: Connectivity <br>
A graph
is said to be connected if there is a path between any two distinct vertices.

### 2 &nbsp; &nbsp; Revisiting the Seven Bridges of Koenigsberg: Eulerian Tours

It says given a graph, G, Is there a walk in G that uses every edge once or in other words has no repeated edges.

> Theorem 5.1 (Euler’s Theorem (1736)). An undirected graph G = (V,E) has an Eulerian tour iff G is even degree (has all vertices have even degree), and connected (except possibly for isolated vertices).

Proof. To prove this, we must establish two directions: if, and only if.

*Only if.*: <br>
We give a direct proof for the forward direction, i.e., if G has an Eulerian tour, then it is connected
and has even degree. Assume that G has an Eulerian tour. This means every vertex that has an edge adjacent
to it (i.e., every non-isolated vertex) must lie on the tour, and is therefore connected with all other vertices
on the tour. This proves that the graph is connected (except for isolated vertices).
Next, we prove that each vertex has even degree by showing that all edges incident to a vertex can be paired
up. Notice that every time the tour enters a vertex along an edge it exits along a different edge. We can pair
these two edges up (they are never again traversed in the tour). The only exception is the start vertex, where
the first edge leaving it cannot be paired in this way. But notice that by definition, the tour necessarily ends
at the start vertex. Therefore, we can pair the first edge with the last edge entering the start vertex. So all
edges adjacent to any vertex of the tour can be paired up, and therefore each vertex has even degree.

*If*: <br>
Base case: <br>
m = 0, which means G is empty (it has no edges), so there is no tour to find.

Induction hypothesis: <br>
EULER(G,s) outputs an Eulerian Tour in G for any even degree, connected graph
with at most m ≥ 0 edges.

Induction step: <br>
Suppose G has m + 1 edges. Recall that T = FINDTOUR(G,s) is a tour, and therefore
has even degree at every vertex. When we remove the edges of T from G, we are therefore left with an
even degree graph with less than m edges, but it might be disconnected. Let G1,...,Gk be the connected
components. Each such connected component has even degree and is connected (up to isolated vertices).
Moreover, T intersects each of the Gi
, and as we traverse T there is a first vertex where it intersects Gi
. Call
it si
. By the induction hypothesis EULER(Gi
,s) outputs an Eulerian tour of Gi
. Now by the definition of
SPLICE, it splices the individual tours together into one large tour whose union is all the edges of G, hence
an Eulerian tour.

### 3 &nbsp; &nbsp; Planarity, Euler’s Formula, Coloring.

**Trees:** <br>
A graph is a tree if it is connected and acyclic (contains no cycles).

**Planar Graphs** <br>
A graph is planar if it can be drawn on the plane without crossings.

**Theorem 5.2. (Euler’s formula) For every connected planar graph, v + f = e + 2** <br>
Proof. <br>
By induction on e. It certainly holds when e = 0, and v = f = 1. Now take any connected planar
graph.  <br>
Two cases: <br>
• If it is a tree, then f = 1 (drawing a tree on the plane does not subdivide the plane), and e = v − 1
(check homework). <br>
• If it is not a tree, find a cycle and delete any edge of the cycle. This amounts to reducing both e and
f by one. By induction the formula is true in the smaller graph, and so it must be true in the original
one.

**If a graph is nonplanar, it follows that e ≤ 3v−6.**

This comes from the fact that  3f ≤ 2e.

**Theorem 5.3. A graph is non-planar if and only if it contains K5 or K3,3.**

**Theorem 5.4. Every planar graph can be colored with five colors**

Proof. Induction on v. The base case is not worth talking about, so we go directly to the inductive step.
Let G be a planar graph. I claim there is a node of degree five or less. In proof, consider the inequality
e ≤ 3v−6. If all vertices had degree six or more, then e would be at least 3v.
So, consider a node u of degree five or less. If it has degree four or less, we are done: Remove u, color the
remaining graph with 5 colors (by induction), and then put u back in and color it by a color that is missing
from its neighbors.
So, u must have 5 vertices, and in the coloring of G−u they all got different colors. Look at them clockwise
around u, and call them u1,u2,u3,u4,u5, and their colors 1,2,3,4,5.
Now try to change the color of u2 to color 4 by determining the connected component containing u2 and
consisting of vertices that are colored 2 or 4. If u4 is in the connected component, switching 2 and 4 is not
helpful. But, we do know that there is a path between u2 and u4 colored 2 and 4.
Similarly, we can try to change the color of u1 to 3, and this will succeed unless there is a path between u1
to u3 colored 1 and 3.
If both of these attempts fail, then we get two paths: one from u1 to u3 colored 1 and 3, and the other from
u2 to u4 colored 2 and 4. But planarity says that these two paths must intersect at some vertex. What is the
color of this vertex?

### Trees

**Theorem 5.5. The statements “G is connected and contains no cycles” and “G is connected and has n−1 edges” are equivalent.**

Proof. We proceed by showing the forward and converse directions.
Forward direction. We prove using strong induction on n that if G is connected and contains no cycles, then
G is connected and has n−1 edges. Assume G = (V,E) is connected and contains no cycles.
Base case (n = 1): In this case, G is a single vertex and has no edges. Thus, the claim holds.
Inductive hypothesis: Assume the claim is true for 1 ≤ n ≤ k.
Inductive proof: We show the claim for n = k +1. Remove an arbitrary vertex v ∈ V from G along with its
incident edges, and call the resulting graph G
′
. Clearly, removing a vertex cannot create a cycle; thus, G
′
contains no cycles. However, removing v may result in a disconnected graph G
′
, in which case the induction
hypothesis cannot be applied to G
′
as a whole. Thus, we have two cases to examine — either G
′
is connected,
or G
′
is disconnected. Here, we show the former case, as it is simpler and captures the essential proof ideas.
The latter case is left as an exercise below.
CS 70, Fall 2022, Note 5 13
So, assume G
′
is connected. But now G
′
is a connected graph with no cycles on k vertices, so we can apply
the induction hypothesis to G
′
to conclude that G
′
is connected and has k −1 edges. Let us now add v back
to G
′
to obtain G. How many edges can be incident on v? Well, since G
′
is connected, then if v is incident
on more than one edge, G will contain a cycle. But by assumption G has no cycles! Thus, v must be incident
on one edge, implying G has (k −1) +1 = k edges, as desired.
Converse direction. We prove using contradiction that if G is connected and has n − 1 edges, then G is
connected and contains no cycles. Assume G is connected, has n−1 edges, and contains a cycle. Then, by
definition of a cycle, removing any edge in the cycle does not disconnect the graph G. In other words, we
can remove an edge in the cycle to obtain a new connected graph G
′
consisting of n − 2 edges. However,
we claim that G
′ must be disconnected, which will yield our desired contradiction. This is because in order
for a graph to be connected, it must have at least n − 1 edges. This is a fact that you have to prove in the
exercise below. This completes the proof of the converse direction.

### Hypercubes

**Lemma 5.1. The total number of edges in an n-dimensional hypercube is n2 n−1.**

Proof 1. The degree of each vertex is n, since n bit positions can be flipped in any x ∈ {0,1}
n
. Since each
edge is counted twice, once from each endpoint, this yields a total of n2<sup>n</sup>/2 = n2<sup>n−1</sup>
edges. <br>

Proof 2. By the second definition of the hypercube, it follows that E(n) = 2E(n−1) +2<sup>n−1</sup>
, and E(1) = 1,
where E(n) denotes the number of edges in the n-dimensional hypercube. A straightforward induction
shows that E(n) = n2<sup>n−1</sup>
.
