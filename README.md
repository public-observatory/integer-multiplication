# Improving the integer multiplication bound

**Can we improve the bound in OpenAI's [Integer multiplication below $n\log n$](https://github.com/openai/math/blob/main/preprints/Integer-multiplication-below-n-log-n-September-23-2026/paper.pdf)?**

The paper gives an algorithm for multiplying two $n$-bit integers in time

$$
O\!\left(n(\log n)^{1-\kappa}\right),\qquad \kappa=2^{-182},
$$

on a fixed multitape Turing machine. The aim is to obtain a better asymptotic bound in the same model, in particular by increasing $\kappa$.

The [CrocSwap project](https://github.com/CrocSwap/integer-mult-bounds) already reports substantial improvements conditional on the paper's framework. It provides a starting point for further work. Improvements to its constructions and different approaches are both welcome.
