# Which restricted circuit families cannot reach the next exponent target?

Can we prove a lower bound on $Phi(a_*)$ that holds for every legal graph or schedule in an explicitly defined family, and hence excludes a desired saving within that family?

The upstream ranked-pair experiment excludes one compiled graph at $2^{-14}$. The common-subset analysis and fixed-graph matching duality provide stronger results in other restricted settings. The next task is to bridge from individual certificates to a family theorem without silently fixing the very choices that a better construction could change.

**First experiment:** specify the support sets, permitted gates, envelopes, terminal encoding and restoration rules of one small family. Enumerate it to identify a candidate invariant; then prove a dual bound or a combinatorial counting inequality that does not depend on the enumerated size.

**Acceptance:** a theorem with all restrictions stated, plus examples attaining or separating the bound. Explain whether it constrains the total rank deficit, the full moment, or both. A bound on cancellation-free addition circuits does not automatically constrain circuits with cancellation.

**Dependencies:** Q3 supplies the explicit search family; progress can also begin from the upstream restricted lower bounds. If the bound excludes the target, name the restriction to relax next.
