# Can physically compatible recursive types beat the scalar construction?

Can two or more legal network types be composed recursively so that a weighted coupled recurrence improves on using the available types separately?

Use the matrix $B(a)$ in [the formulation](../formulation.md). A positive vector $v$ with $B(a)v<v$ is a sufficient induction certificate under the stated recurrence assumptions. This elementary matrix criterion is not itself the research contribution.

**First experiment:** choose two types that act on the same mathematical data but differ in layout or decomposition. Specify input and output representations, legal recursive children, normalization and conversion costs. Construct the smallest cycle between them and compare its full bound with each scalar alternative.

**Acceptance:** a finite, physically realizable coupled witness with exact interval bounds and a positive rational weight vector, or a proof that the allowed conversions remove every gain in the stated class. If conversion costs fail to fit the recurrence, reject the candidate.

**Dependencies:** Q1–Q2. Compare with the upstream matrix and typed-catalogue work before claiming novelty; commutativity does not establish closure of the legal child class.
