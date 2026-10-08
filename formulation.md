# Formulation and elementary baselines

## The finite data

Fix a finite network and its physical implementation. Let $m\geq2$ be its parent width and $W\geq1$ its number of physical roles. For each $1\leq t<m$, let $c_t$ be the number of recursive children of width $t$. Each child acts on $1/W$ of the parent's stored volume. These numbers must be obtained from the complete implementation, including endpoints and restored workspace.

For a proposed saving $0<a<1$, define

$$
\Phi(a):=\frac1W\sum_{t=1}^{m-1}c_t\left(\frac{t}{m}\right)^{1-a}.
$$

The strict inequality $\Phi(a)<1$ is the contraction condition. A smaller $\Phi(a)$ at a fixed target gives more room for recursive overhead. This is the child moment used by the community's [arithmetic checker](https://github.com/CrocSwap/integer-mult-bounds/blob/56b66d58297deca1d7dd130247d720e960f77a37/scripts/audit_community_candidate.py), not a new objective introduced by this agenda.

The simplified recurrence explains it. Suppose a nonnegative normalized cost $F$ satisfies, on admissible scales,

$$
F(x)\leq\frac1W\sum_{t=1}^{m-1}c_t F(tx/m)+C x^\eta,
\qquad 0\leq\eta<1-a,
$$

with bounded base-case cost and no uncharged rounding or layout cost. Substituting the inductive bound $F(x)\leq Kx^{1-a}$ gives a recursive contribution at most $K\Phi(a)x^{1-a}$. Since the gap $1-\Phi(a)$ is positive, choosing $K$ large enough absorbs the toll and the finitely many base cases. Thus $F(x)=O(x^{1-a})$.

This elementary induction is not the all-size tape theorem. Padding, arbitrary widths, changes in bit volume and numerical precision must first justify such a recurrence. Q1 asks for those hypotheses and their proofs.

## Why a rank deficit is insufficient

Define the weighted child sum and deficit by

$$
s:=\sum_{t=1}^{m-1}t c_t,\qquad \Delta:=mW-s.
$$

Then $\Phi(0)=1-\Delta/(mW)$. A positive deficit therefore gives $\Phi(0)<1$, and continuity gives a positive interval of admissible savings. But it does not specify its endpoint: for $0<a<1$, the power $(t/m)^{1-a}$ depends on the distribution of child widths.

For example, fix $m:=4$ and $W:=2$. A profile with $c_1:=2,c_2:=2$ and all other counts zero, and a profile with $c_3:=2$ and all other counts zero, both have $s=6$ and $\Delta=2$. Their moments at $a=1/2$ are respectively $1/2+1/\sqrt2>1$ and $\sqrt3/2<1$. These are recurrence examples, not claims that either profile has a physical realization.

Moreover, $\Phi$ is strictly increasing whenever at least one child is present, because each ratio $t/m$ lies strictly between zero and one. Hence a certified lower bound $\Phi(a_*)>1$ excludes every $a\geq a_*$ for this profile. It excludes neither other profiles nor other recurrence arguments.

## Why parameter tuning is not enough

The selected checkpoint certifies the bit saving

$$
a_0:=\frac{102039046058023}{2000000000000000000}.
$$

In its balanced assembly, a positive backoff $0<h<1/2$ defines

$$
q:=a(1-2h),\qquad \epsilon:=\frac{1-h}{1+q},\qquad G:=\epsilon q.
$$

The final saving must satisfy $\kappa<G$, together with the other assembly conditions. Because $0<q<a$ and the function $x\mapsto x/(1+x)$ is increasing for $x>0$,

$$
\kappa<G=\frac{(1-h)q}{1+q}<\frac{a}{1+a}.
$$

This upper bound applies only to the displayed assembly family. At $a=a_0$, its distance above the selected $\kappa_0$ is less than $1.35\times10^{-20}$. Consequently, reaching $\kappa\geq2^{-14}$ through this assembly requires

$$
a>\frac{1}{16383},
$$

which is more than 19.63% above $a_0$. This is a necessary condition, not a sufficient construction. The same assembly also requires $a<(1-\beta)b$, where $b$ is the complex saving and $0<\beta<1$ is a layer parameter; it has 47 strict constraints in total. Improving the bit profile can eventually make another condition binding.

The numerical comparisons above are exact rational checks in `scripts/check_baseline.py`. They do not establish an upper bound on the best saving attainable by the physical network: $a_0$ is a certified point, not an exact root certificate.

## Questions beyond one profile

**Joint synthesis.** At a fixed target $a_*$, optimize $\Phi(a_*)$ over explicitly permitted graphs, schedules, frames and role assignments. The denominator $W$ changes with the implementation; minimizing the numerator alone is not equivalent. Begin with the existing all-cardinality matching formulation before adding new search variables.

**Several recursive types.** Suppose type $i$ has $W_i$ roles and children of type $j$ with size ratios $r_{ije}\in(0,1)$, indexed by $e$. Define the nonnegative matrix

$$
B_{ij}(a):=\frac1{W_i}\sum_e r_{ije}^{1-a}.
$$

Under a valid coupled recurrence with smaller-order tolls, a positive vector $v$ satisfying $B(a)v<v$ supplies componentwise inductive constants. Indeed, the positive gaps $v_i-(B(a)v)_i$ absorb the tolls just as in the scalar argument. This is a standard weighted induction criterion. The research question is whether physically compatible network types can realize a useful matrix after every conversion cost is charged. An abstract matrix with a favorable spectral radius is insufficient.

**Slack and thresholds.** A contraction gap near zero increases the constant required by the induction. The selected numerical refinement reports a moment-gap lower bound of about $9.26\times10^{-21}$. Q5 asks for explicit dependence on this gap, guard precision and eventual thresholds. A witness with a slightly smaller exponent and a shorter proof may be preferable for verification, even when it is weaker asymptotically.

## Claims maintained here

| Statement | Status and scope |
|---|---|
| The selected checkpoint yields $\kappa_0$ | Conditional upstream result; arithmetic audit replayed here |
| Positive deficit yields some positive moment saving | Elementary consequence of continuity; finite profile only |
| Deficit alone does not determine a useful saving | Explicit abstract-profile example above |
| The displayed assembly has $\kappa<a/(1+a)$ | Proved algebraic consequence of its hypotheses |
| Coupling, new frames or new geometries improve the checkpoint | Open; no witness supplied |
| The complete multiplication algorithm is formally verified | Not established by this agenda or its baseline checks |
