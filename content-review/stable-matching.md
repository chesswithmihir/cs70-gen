# Questions I got wrong...

> In a stable marriage instance where there is a man at the bottom of each woman’s preference list, the
man is paired with his least favorite woman in every stable pairing.

Correct Answer: False. Consider lists M1: W1>W2, M2: W2>W1, W1: M1>M2, W2: M1>M2

---

> In a stable marriage instance where there is a man at the top of each woman’s preference list, the man is paired with his favorite woman in every stable pairing.

Correct Answer: True, if M is the man at the top and his favorite woman is W, then if (M,W’) and (W,M’) are in a pairing, (M,W) are a rogue couple because they mutually prefer each other.

---

>  For n = 2, or any 2-men, 2 woman stable marriage instance, man A has the same optimal and pessimal woman. (True or False)

False. This says there is only one stable pairing. But preference list for man A is (1,2) and for man
B is (2,1) and preference list for woman 1 is (B,A) and woman 2 is (A,B) produce different male and
female optimal pairings.

---

> In any stable marriage instance, in the pairing in the TMA there is some man who gets his favorite
woman (the first women on his preference list.) (True or False.)

False. Let man A have preference list (1,3,1), B have (1,2,3), and C have (2,1,3). If woman 1 prefers
A over B, B does not get his favorite, and ask 2, who prefers B over C who then asks 1, who prefers C
over A who is then rejected. No man got his favorite.

---

> In any stable marriage instance with n men and women, if every man has a different favorite woman,
a different second favorite, a different third, and so on, and every woman has the same preference list,
how many days does it take for TMA to finish? (Form of Answer: An expression that may contain n.)

1.
On the first day every woman gets a proposal since each man has a different woman in their first
position. The algorithm terminates.

---

> Consider a stable marriage instance with n men and n women, and where all men have the same
preference list, and all women have different favorites, and different second men, and so on. How
many days does the TMA take to finish? (Form of Answer: An expression that may contain n)

n.
Every man proposes to their common favorite. One man is kept on the string. The rest propose to the
second. And so one. After each day, a new woman gets a man on a string. After n days, we finish.
Note: that the women’s preference list were irrelevant.

---

> It is possible for a stable pairing to have a man A and a woman 1 be paired if A is 1’s least preferred
choice and 1 is A’s least preferred choice. (True or False)

True.
A and 1 are respectively all the women’s and men’s least favorite.

---

> It is possible for a stable pairing to have two couples where each person is paired with their lowest
possible choice. (True or False)

False.
Just consider the two couples. The man from the first and the woman from the other prefer each other,
thus they form a rogue couple.

---

> In a propose-and-reject algorithm execution which takes n days, there is an applicant who did not receive a job offer on day (n-1).

True. If there wasn't an applicant who didn't receive a job offer on day (n - 1), then the algorithm would have ended on day n - 1.

---

> In a propose-and-reject algorithm execution if an applicant receives a job offer on day d, they receive at least one proposal on every subsequent day until algorithm termination.

True. If an applicant has job offer, then by the Improvement Lemma that applicant will always have a job offer on hand that is at least as good as the current job.

---

> In a propose-and-reject algorithm execution, given n jobs and n applicants where n > 1, there is a set of preferences such that the algorithm fills every job with its applicant that is lowest on its hiring list.

False. There will always be one applicant who only receives a single proposal. In order for every applicant to end up with the job lowest on their preference list, this would mean every applicant must have rejected n-1 jobs. Hence, this is impossible.

---

> In a propose-and-reject algorithm execution, if an applicant receives no offer on day dd, then they also receive no offer on all previous days.

This is contrapositive of the 1.2: In a propose-and-reject algorithm execution if an applicant receives a job offer on day d, they receive at least one proposal on every subsequent day until algorithm termination.

---

> For n > 2, there is a stable marriage instance of n men and n women in which the traditional marriage algorithm takes at least n<sup>2</sup> days

False. If this were true, then there must have been at least n
<sup>2</sup> − 1 > n(n − 1) rejections.
Therefore, by Pigeonhole, somebody got rejected n times, which is impossible.

---

> If a stable pairing P has a pair (m,w) where P is optimal for both m and w, then every stable pairing is
optimal for both m and w.

True. They would be a rogue couple in any supposed stable pairing where they are not
paired, thus they would always be together in every stable pairing. Thus, every stable pairing would
be optimal for both of them.

---

> If at any point in the traditional marriage algorithm a woman’s optimal partner proposes to her, then
every stable pairing is optimal for her.

Answer: True. It only gets better for women, so she must end up with her optimal partner. This
suggests that in any other stable pairing, either this couple is rogue or this pairing is not optimal for
both her and her partner, which it is. Thus, there are no pairings where they are not paired.

---

> For any two job, two candidate stable matching instance, a matching where both jobs have their favorite candidate is stable

True. Neither job can participate in a rogue pair since they both have their favorite candidate.

---

> For any stable matching instance, any matching is stable if for each pair in the matching either the job
has their favorite candidate or the candidate has their favorite job.

False. Consider the preference lists. <br>

| Jobs | Candidates |
|--- | ---|
| 1 | A, B |
| 2 | A, B |

| Candidates | Jobs |
|--- | ---|
| A | 1, 2 |
| B | 1, 2 |

The pairing (A,1) and (B,2) satisfies the property and B and 1 is a rogue couple.

---

> For any stable matching instance, every stable matching has at least one candidate who gets their favorite job.

False. (for each job, they are the least favorite job of the candidate
they prefer to their current partner), and nobody is paired with their favorite partner.

---

> In any job optimal pairing for a stable matching instance with n jobs, at least job(s) must get
their favorite partner.

0, This is really asking if every job can get rejected during a run of the job-proposed algorithm. Consider a 3-job example where the first two jobs ask the first candidate, one is rejected and
then asks the same candidate as the third job, who is rejected and then ask the first candidate who
then rejects the first job. So everyone got rejected once.

---

> At most how many rogue pairs could there be for an unstable matching for an n job, n candidate stable
matching instance?

n(n - 1). There are at most that many unmatched pairs, and any matching that consists of
pairs where the entities are each other’s least favorite partner has the property that all pairs not in the
matching are rogue. One can set up preference lists where everyone’s least favorite partners form a
matching.

---

> Given two stable matchings M1 and M2, we say that M1 is job-preferred to M2 if every job prefers M1
at least as much as M2. In other words, every job is matched to a candidate in M1 that is at least as high
on the job’s preference list as its candidate in M2. Similarly, we say that M1 is candidate-preferred to
M2 if every candidate prefers M1 at least as much as M2.
Prove that if M1 is job-preferred to M2, then M2 is candidate-preferred to M1.

Proceed by contradiction. Suppose M1 is job-preferred to M2, but M2 is not candidate preferred to M1. Then there exists a candidate C that prefers M1 over M2. Let (J,C) ∈ M1 and let (J0,C) ∈ M2, where C prefers J over J0. Let C0 be the candidate matched to J in M2, so (J,C0) ∈ M2. Since M1 is job-preferred to M2, J prefers C over C0. However, this means that (J,C) would be a rogue
couple in M2, contradicting the assumption that M2 is stable.

---

> For any stable matching instance, the job optimal stable matching has at least one job that is paired with their
favorite candidate

False. See Spring 2022 for Explanation.

---

> For any stable matching instance, the job optimal stable matching has no job paired with their least favorite
candi

False. In general, if all jobs have a common least favorite candidate, some job must end up paired with it in the end

---

> For any stable matching instance, the job optimal stable matching has at least one candidate that does not get
their favorite

False. s. In general, if every job has a distinct favorite candidate, and each one of those candidates like the corresponding job the most, then the propose and reject algorithm ends in one day, and every job and every candidate
gets their favorite choices

---

> For any stable matching instance, all matchings have an even number of rogue couples. (Recall, a stable matching has 0 rogue couples.)

False. See Spring 2022 for Explanation.

---

> Consider an output from running the Propose-and-Reject algorithm on a stable matching instance with n
jobs and n candidates. We then arbitrarily permute one job’s preference list? What is the maximum number of jobs that can participate in a rogue couple in the outputted matching
with respect to the permuted preference list?

Answer: 1. The only job that can participate in a rogue couple is the one whose preference list was
permuted.
To see why, suppose we look at some other job j, paired with candidate c in the matching. All candidates
that j prefers more than c would have rejected j for some other job they liked more. This means that j
can’t be in a rogue couple with any other candidate—the other candidate wouldn’t like j more than what
they currently have.

---

> Consider an output from running the Propose-and-Reject algorithm on a stable matching instance with n
jobs and n candidates. We then arbitrarily permute one job’s preference list? What is the maximum number of rogue couples in the outputted matching with respect to the permuted
preference list?

Answer: We know that no other job can be in a rogue couple, so all possible rogue couples must include
the job whose preference list we permuted.
Suppose the job whose preference list we permuted is job j, paired with candidate c in the matching. If
all other candidates put j at the top of their preference lists, and the permutation moved c to the bottom
of j’s preference list, then (j,c′) will be a rogue couple for all other candidates c′. This is because j would prefer any other candidate c′ more than c, and any other candidate c′ prefers j the most. Since there are n −1 other candidates to form the rogue couple with, the maximum number of rogue
couples with respect to the permuted preference list is n − 1.
