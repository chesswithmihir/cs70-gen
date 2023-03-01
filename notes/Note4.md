# CS 70 Fall 2022
## Note 4
### By Mihir Mirchandani
---

### 1 &nbsp; &nbsp; The Stable Matching Problem

This is one of the most concepts in algorithms. There is an algorithm to make matching stable between jobs and candidates a common problem in economics. This algorithm is called the Propose and Reject algorithm.

### 2 &nbsp; &nbsp; The Propose-and-Reject Algorithm

**Every Morning**: Each job proposes (i.e. makes an offer) to the most preferred candidate on its list who has not yet rejected this job.

**Every Afternoon**: Each candidate collects all the offers she received in the morning; to the job offer
she likes best among these, she responds “maybe” (she now has it in hand or on a string), and to the
other offers she says “no” (i.e., she rejects them). (This is just a way for us to virtually model that there
are no “exploding offers” and a job can’t withdraw an offer once an offer is made.)

**Every evening**: : Each rejected job crosses off the candidate who rejected its offer from its list.

*The above loop is repeated each successive day until there are no offers rejected. At that point, each candidate has a job offer in hand (i.e. on a string); and on this day, each candidate accepts their offered job (i.e. the job offer she has in hand) and the algorithm terminates.*

### Lemma 4.1. The propose-and-reject algorithm always halts.

*Proof.*

The argument is simple: On each day that the algorithm does not halt, at least one job must eliminate
some candidate from its list (otherwise the halting condition for the algorithm would be invoked). Since
each list has n elements, and there are n lists, this means that the algorithm must terminate in at most n<sup>2</sup> iterations (days).

### 4.1 &nbsp; &nbsp; Stability

We always want good properties or favorable properties in a stable matching. Stability includes having an algorithm that ensures that no rogue pairs can exist. Now what do we mean by rogue pairs? It means that every pairing between Job and Candidate prefer each other over any other pairings. If J' is paired with C when C' is paired with J and J and C both would prefer each other. There exists a rogue pair. We call this an unstable matching.

### 4.2 &nbsp; &nbsp; Proving Stability

> Lemma 4.2 (Improvement Lemma). If job J makes an offer to candidate C on the kth day, then on every
subsequent day C has a job offer in hand (on a string) which she likes at least as much as J.

We can do a Proof by Induction to show why this is the case. Induct on the day i, with i ≥ k.

Base Case: <br>
i = k; On day k, C receives at least one offer (from J). At the end of day k, she will therefore
have an offer in hand either from J or a job she likes more than J, since she chooses the best among her
offers.

Inductive Hypothesis: <br>
Suppose the claim is true for some arbitrary i ≥ k.

Inductive Step: <br>
We prove the claim for day i + 1. By the Induction Hypothesis, on day i, C had an offer from job J′ on a string which she likes at least as much as J. (Note that J′ may be J.) According to the
algorithm, J′ proposes again to C again on day i+1 (since this job offer hasn’t yet been rejected by her and is not allowed to explode). Therefore, at the end of day i + 1, C will have on a string either J′ or an offer
from a job she likes more than J′; in both cases, she likes this job at least as much as J. Hence the claim holds for day i+1, completing the inductive step.

You can actually use Proof by Contradiction to say something very similar <br>
As in our original proof, the claim certainly holds on day i = k. Suppose
now, for the sake of contradiction, that the ith day for i > k is the first counterexample where C has either no offer or an offer from some J<sup>*</sup>
inferior to J on a string. On day i−1, she had an offer from some job J′ on a string and liked J′ at least as much as J. According to the algorithm, J′ still has an offer out to C on the ith day. (i.e. offers don’t explode and can’t be withdrawn) So C has the choice of at least one job (J′) on the ith day; consequently, her best choice must be at least as good as J′, and therefore certainly better than J<sup>∗</sup> or nothing. This contradicts our initial assumption.

### Lemma 4.3. The propose-and-reject algorithm always terminates with a matching.

Proof. We proceed by contradiction. Suppose that there is a job J that is left unpaired when the algorithm
terminates. It must have made an offer to all n of the candidates on its list and been rejected by all of them.
By the Improvement Lemma, since its offer was rejected, each of these n candidates has had a better offer
in hand since J made an offer to her. Thus, when the algorithm terminates, n candidates have n jobs on a
string not including J. So there must be at least n+1 jobs. But this is a contradiction, since there are only n
jobs by assumption.

### Theorem 4.1. The matching produced by the algorithm is always stable.

Proof. We give a direct proof that, in the matching output by the algorithm, no job can be involved in a
rogue couple. Consider any couple (J,C) in the final matching and suppose that J prefers some candidate
C
∗
to C. We will argue that C
∗ prefers her job to J, so that (J,C
∗
) cannot be a rogue couple. Since C
∗
occurs before C in J’s list, J must have made an offer to C
∗ before it made an offer to C. Therefore, by the
Improvement Lemma, C
∗
likes her final job at least as much as J, and therefore prefers it to J. Thus no job
J can be involved in a rogue couple, and the matching is stable.


### Theorem 4.2. The matching output by the Propose-and-Reject algorithm is job/employer optimal.

Proof. Suppose for sake of contradiction that the matching is not employer optimal. Then, there exists a
day on which some job had its offer rejected by its optimal candidate; let day k be the first such day. On
this day, suppose J was rejected by C
∗
(its optimal candidate) in favor of an offer from J
∗
. By the definition
of optimal candidate, there must exist a stable matching T in which J and C
∗
are paired together. Suppose T looks like this: {...,(J,C
∗
),...,(J
∗
,C
′
),...}. We will argue that (J
∗
,C
∗
) is a rogue couple in T, thus
contradicting stability.

### Theorem 4.3. If a matching is employer/job optimal, then it is also candidate pessimal.

Proof. We proceed by contradiction. Let T = {...,(J,C),...} be the employer optimal matching (which we
know from Theorem 4.2 is output by the algorithm). Suppose for the sake of contradiction that there exists a
stable matching S = {...,(J
∗
,C),...,(J,C
′
),...} such that job J
∗
is lower-ranked on C’s preference list than
job J (i.e., J is not her pessimal job). We will argue that S cannot be stable by showing that (J,C) is a rogue
couple in S. By assumption, C prefers job J to J
∗
since J
∗
is lower on her list. And J prefers candidate C to
its partner C
′
in S because C is its partner in the employer optimal matching T. Contradiction. Therefore,
the employer optimal matching is candidate pessimal.
