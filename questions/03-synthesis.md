# Can joint graph and schedule search improve the complete child moment?

Can changing the addition graph, evaluation order and legal role reuse jointly produce a strictly better certified child moment, after all changes in physical role count are charged?

At a fixed target saving, optimize the complete recursive child moment, including the number of physical roles. Begin with the existing fixed-graph all-cardinality matching certificate. Declare which new choices are allowed: reassociation, interval decomposition, donor links, paid reclamation or frame changes. A lower operation count alone is not the objective.

**First experiment:** reproduce an exact optimum in one tiny existing strip or pair decomposition. Then allow one additional structural choice and enumerate the resulting class, retaining exact upper and lower bounds. Test at the current saving and at a rational value above $1/16383$, the necessary bit threshold for the chosen final target under the balanced assembly.

**Acceptance:** a physically replayed improved profile with rational moment enclosures, or an exact optimum for the declared finite class. Record the complete child distribution and the changed denominator $W$.

**Dependencies:** Q1–Q2 for admissibility and verification. Do not interpret search exhaustion outside a complete enumeration as a lower bound.
