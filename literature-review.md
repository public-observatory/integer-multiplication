# Literature and source review

Prepared 8 October 2026. This is a focused review of the supplied construction and its immediate mathematical context, not an exhaustive novelty survey. Repository references below use the fixed revision in `sources.json`; claims about an entire field require a separate literature check.

## Established analytic starting point

David Harvey and Joris van der Hoeven, [Integer multiplication in time $O(n\log n)$](https://annals.math.princeton.edu/2021/193-2/p04), *Annals of Mathematics* 193 (2021), 563–617, prove that upper bound in the multitape Turing model. Their Gaussian resampling reduces the required transforms to power-of-two dimensions. This is the analytic starting point inherited by the supplied manuscript. It does not provide the finite-network savings pursued here.

Their [Integer multiplication is at least as hard as matrix transposition](https://arxiv.org/abs/2503.22848v1), version 1, 28 March 2025, reduces matrix transposition to multiplication in the multitape model. A conjectural transposition lower bound would therefore imply a multiplication lower bound. This is not an unconditional lower bound against linear combinations of stored data. Any proposed obstruction in this agenda must state whether coded intermediate values are permitted.

## The supplied manuscript

OpenAI, [Integer multiplication below $n\log n$](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Integer-multiplication-below-n-log-n-September-23-2026), 23 September 2026, states a saving $2^{-182}$ for one deterministic fixed finite-tape machine. Its source describes the following chain:

| Source section | Contribution to the proposed algorithm | Agenda obligation |
|---|---|---|
| `03-motifs.tex` | Finite networks and recursive savings | Verify scalar maps, restored auxiliary data and frame compatibility |
| `04-swap.tex`, `05-layers.tex` | Address interchange and simultaneous numerical layers | Recover the exact tape, layout and precision hypotheses |
| `06-transforms.tex`, `07-resampling.tex` | Synthetic transforms and ordered resampling | Preserve permutations, normalizations and error estimates |
| `08-assembly.tex` | Setup, parameter choice and exact output recovery | Charge every operation and justify all sufficiently large sizes plus base cases |
| `10-transposition.tex` | A transposition application | Compare Q8 with this existing consequence before claiming an extension |

We treat this manuscript as a proposed framework to inspect, and the community extension as conditional on the interfaces it inherits. Reading or compiling the manuscript does not establish its theorem. The agenda does not assert that a flaw exists; Q1 asks which obligations can be proved independently and which remain imported.

## The community checkpoint

Douglas Colkitt and contributors, [integer-mult-bounds](https://github.com/CrocSwap/integer-mult-bounds/tree/56b66d58297deca1d7dd130247d720e960f77a37), selected revision `56b66d5`, supplies the baseline. Its [round-two review](https://github.com/CrocSwap/integer-mult-bounds/blob/56b66d58297deca1d7dd130247d720e960f77a37/docs/research/community-round2-review.md) separates physical replay, arithmetic checks, formal certificates and inherited assumptions. Historical release files contain superseded numerical values; they are not interchangeable with the selected certificate.

The checkpoint has parent width 575 and 137,151,806 physical roles. Its complete weighted child sum is 78,860,441,550, giving deficit 1,846,900. The role count reflects Avi Eisenberg's interval strips and core-aware pair assembly combined with eumemic's joint frame compiler. Alejandro Zarzuelo Urdiales's refinement selects the reported final rational saving. The [finite proof](https://github.com/CrocSwap/integer-mult-bounds/blob/56b66d58297deca1d7dd130247d720e960f77a37/research/pair-assembly/PROOF.md) explains why extra additions can reduce physical roles through legal reuse; the new agenda should not rediscover that observation as a novel result.

Three existing negative or optimality results constrain the agenda:

- The [ranked-pair screen](https://github.com/CrocSwap/integer-mult-bounds/blob/56b66d58297deca1d7dd130247d720e960f77a37/docs/research/pair-ranked-screen.json) certifies a moment lower bound above one at $2^{-14}$ for that particular compiled graph. It does not exclude every schedule, graph or recurrence.
- The [matching formulation](https://github.com/CrocSwap/integer-mult-bounds/blob/56b66d58297deca1d7dd130247d720e960f77a37/research/matrix-exponent-synthesis/catalogue/MATCHING_SEARCH.md) already includes all-cardinality feasibility and exact primal/dual certificates for a fixed graph and quantized objective. Q3 must extend the variables or improve the certified objective, not merely run maximum matching again.
- The [common-subset analysis](https://github.com/CrocSwap/integer-mult-bounds/blob/56b66d58297deca1d7dd130247d720e960f77a37/docs/research/prime-subset-limits.md) proves a restriction for a specified incidence map and cancellation-free compiler. Q4 asks for similarly explicit bounds in other families; it cannot promote this result into a bound for arbitrary linear networks.

## Formal and algebraic work already present

The [matrix and exponent synthesis package](https://github.com/CrocSwap/integer-mult-bounds/blob/56b66d58297deca1d7dd130247d720e960f77a37/research/matrix-exponent-synthesis/README.md) contains exact Gaussian matrix evaluation, denominator accounting, matching duality and finite arithmetic certificates. It also records that commuting phase operators need not remain in the eligible recursive child class. Consequently, low algebraic rank or operator commutativity alone is insufficient for Q6 or Q7.

The integrated review reports an axiom audit of 169 distinct Lean declarations, including 11 concrete frontier checks. Its scope excludes the full analytic enclosure and multiplication transfer. Q2 therefore starts from the existing checker and formal boundaries; it asks for a smaller independent path from circuit semantics to the recurrence, not another certificate that silently assumes the disputed interface.

## What this agenda adds

The proposed work is a coordinated set of questions, not a new multiplication theorem. The immediate deductions are the elementary recurrence examples and the assembly bound in `formulation.md`. The substantive open directions are a proved transfer contract, joint graph-and-schedule synthesis, family-level obstructions, explicit slack/precision tradeoffs, and physically realizable coupled recurrences. Each requires comparison with the cited packages before a novelty claim.
