# Integer multiplication: circuits, certificates and exponent savings

An open research agenda on the [Public Observatory](https://public-observatory.github.io/). Questions and claims live in this repository's [issues](https://github.com/public-observatory/integer-multiplication/issues).

## Motivation

A transform-based multiplication algorithm pays both to move data and to perform arithmetic. Saving arithmetic operations alone does not help if moving the data still costs as much as the original computation. The [OpenAI manuscript](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Integer-multiplication-below-n-log-n-September-23-2026) proposes finite linear networks that reduce both costs. The [CrocSwap project](https://github.com/CrocSwap/integer-mult-bounds/tree/56b66d58297deca1d7dd130247d720e960f77a37) develops better networks and exact certificates within that framework.

The opportunity is to understand which network properties produce a larger saving, and which properties let that saving survive the passage from a finite circuit to an algorithm for every input length. More additions can sometimes help: they can make stored intermediate values reusable and reduce the number of physical wires. Thus neither operation count nor algebraic rank alone is the right objective.

## Root question

**Which finite linear networks yield larger certified exponent savings for exact integer multiplication on a fixed multitape Turing machine, and what hypotheses suffice to transfer their savings to every input length?**

For one deterministic machine $A$, let $T_A(n)$ denote its worst-case time to multiply two $n$-bit integers. Write $L(n):=\max\{1,\lceil\log_2 n\rceil\}$. The target is

$$
T_A(n)=O\!\left(nL(n)^{1-\kappa}\right),\qquad \kappa>0,
$$

with a fixed finite alphabet, a fixed number of one-dimensional tapes, and exact output for every input. The machine, its finite network and its constants must be independent of $n$.

The pinned community checkpoint reports the conditional saving

$$
\kappa_0:=\frac{25508460085039}{500000000000000000}
=0.000051016920170078.
$$

It inherits the OpenAI framework and subsequent analytic and tape interfaces. It is not a fully formalized multiplication theorem. The [baseline and evidence record](reproduction.md) distinguish checks executed for this agenda from upstream reports.

Our first numerical target is $\kappa\geq 2^{-14}$. This target is a research choice, not a conjecture that the existing construction can attain it. In fact, the [assembly calculation](formulation.md#why-parameter-tuning-is-not-enough) shows that the presently certified bit saving would have to increase by more than 19.63% within the stated assembly family. Merely tuning its remaining parameters cannot suffice.

## Research directions

| Question | First deliverable | What would count as progress? |
|---|---|---|
| [Q1. Transfer assumptions](questions/01-transfer.md) | A dependency table from finite profiles to exact output | A proved interface lemma or an explicit failure of a stated hypothesis |
| [Q2. Small independent verifier](questions/02-verifier.md) | A certificate format with negative controls | Independent replay of one reduced network and exact recurrence checks |
| [Q3. Search for the full recurrence objective](questions/03-synthesis.md) | A bounded search over graphs, schedules and role reuse | A certified improvement or a rigorous optimum in the declared search class |
| [Q4. Limits of restricted circuit families](questions/04-barriers.md) | A bound that survives all schedules in one specified family | A proof that a target requires leaving that family |
| [Q5. Precision and useful slack](questions/05-precision.md) | An explicit tradeoff between saving, contraction gap and thresholds | A simpler or more robust witness with all costs retained |
| [Q6. Coupled recursive constructions](questions/06-coupled.md) | A two-type recurrence with paid changes of representation | A certified gain beyond its scalar alternatives, or an obstruction |
| [Q7. Changing the algebraic construction](questions/07-algebra.md) | One new incidence or frame family with an exact compiler | A better complete profile, rather than only a lower abstract rank |
| [Q8. A reusable movement theorem](questions/08-movement.md) | A precise class of layouts covered by the address primitive | A proved application or a sharp boundary beyond existing transposition results |

Start with Q1 and Q2, then use their contracts to evaluate Q3 and Q4. Q5 can study the fixed checkpoint immediately. Q6–Q8 are exploratory and should begin with small exact examples. The [formulation](formulation.md) gives the recurrence and the [literature review](literature-review.md) records what these directions must improve upon.

## First research cycle

1. Pin and reconstruct the baseline. Identify the theorem supporting each interface, including dirty workspace, padding, numerical precision and final rounding. Stop any affected transfer claim if a required interface is missing.
2. Freeze a finite search class and budget before comparing candidates. Report physical role count and the entire child-width distribution. Retain rejected candidates and exact exclusion certificates.
3. Choose between extending the construction and changing it. If an exact family bound excludes the target, change a declared assumption instead of enlarging the same search without a reason.
4. Package one result: a proved lemma, a certificate with independent replay, a smaller trusted verifier, or a scoped impossibility theorem. Report an inconclusive bounded search as inconclusive.

## Contributions and evidence

Anyone may propose subquestions. Claims should name the question they address and be labeled in their text as **proved**, **conditional**, **computational**, **conjectural**, or **speculative**. State every hypothesis needed for a theorem and distinguish a reported source result from a result checked here. A failed route is useful when its failure has a precise scope.

Circuit submissions must charge workspace restoration, copying, changes of basis and representation, every recursive child, and source and sink costs. Give exact input files, source revisions, reproduction commands and the proof connecting a finite certificate to the claimed recurrence. A solver's failure to find a witness is not an impossibility proof; failure of an upper enclosure to certify a target is not a certified lower bound.

This agenda follows [the contribution record](https://github.com/CrocSwap/integer-mult-bounds/blob/56b66d58297deca1d7dd130247d720e960f77a37/CONTRIBUTORS.md) maintained by Douglas Colkitt. The selected checkpoint combines Avi Eisenberg's pair assembly, eumemic's frame compiler and Alejandro Zarzuelo Urdiales's parameter refinement, together with the earlier community constructions. The underlying manuscript is by OpenAI; the analytic starting point is Harvey and van der Hoeven. This agenda was prepared with OpenAI Codex assistance. It makes no priority or practical-speed claim.
