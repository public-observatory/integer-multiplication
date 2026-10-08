# Working on this agenda

- This is a standalone Public Observatory agenda repository. Keep it separate from the Observatory website and from source-construction repositories.
- Follow the user's mathematical writing guidelines at `~/Notes/WRITING.md` when available: justify claims promptly, minimize notation, define symbols before use, use `:=` for definitions, and state proof ideas before long arguments.
- Keep claims explicitly proved, conditional, computational, conjectural or speculative. Distinguish checks executed here from upstream reports.
- Keep immutable source references and preserve contributor attribution. Do not update the numerical checkpoint without its evidence.
- Use `$...$` and `$$...$$` for Markdown mathematics. In Typst, write `$u_i (x)$`, not `$u_i(x)$`.
- Validate with `python3 scripts/check_baseline.py` and the Observatory agenda schema. Neither check proves the full multiplication theorem.
