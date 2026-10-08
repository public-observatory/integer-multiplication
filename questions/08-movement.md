# How far does the coded address-movement primitive extend beyond its current layouts?

For which precisely specified classes of array layouts can the framework's address-interchange primitive give a sublogarithmic movement overhead while restoring arbitrary auxiliary data?

Start with complete Cartesian address sets and disjoint contiguous fields, where the source primitive applies. Choose one extension, such as unequal field widths or a sparse address domain. State the input and output encoding and charge the cost of embedding, padding and restoring the original layout.

**First experiment:** either give a reduction for one extended class with explicit volume and time bounds, or construct a family for which the proposed padding destroys the saving. Distinguish a failure of that reduction from an impossibility theorem for the task.

**Acceptance:** a proved extension or a sharp limitation with exact hypotheses. The OpenAI manuscript already treats matrix transposition, and Harvey–van der Hoeven already reduce it to multiplication; reproducing those implications is a baseline, not a new application.

**Dependencies:** Q1. Keep the fixed tape count and finite alphabet explicit; an uncharged random-access operation changes the problem.
