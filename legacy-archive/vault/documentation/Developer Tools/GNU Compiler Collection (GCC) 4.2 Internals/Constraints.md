---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Constraints.html
archived_at: '2026-07-15T07:31:01.581436Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Standard Names](Standard-Names.md#apple-kn2gc3temfzgilkomfwwk4y),
Previous: [Predicates](Predicates.md#apple-kbzgkzdjmnqxizlt),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.8 Operand Constraints

Each `match_operand` in an instruction pattern can specify
constraints for the operands allowed. The constraints allow you to
fine-tune matching within the set of operands allowed by the
predicate.

Constraints can say whether
an operand may be in a register, and which kinds of register; whether the
operand can be a memory reference, and which kinds of address; whether the
operand may be an immediate constant, and which possible values it may
have. Constraints can also require two operands to match.

- [Simple Constraints](Simple-Constraints.md#apple-knuw24dmmuwug33oon2heyljnz2hg): Basic use of constraints.
- [Multi-Alternative](Multi_002dAlternative.md#apple-jv2wy5djl4ydamteifwhizlsnzqxi2lwmu): When an insn has two alternative constraint-patterns.
- [Class Preferences](Class-Preferences.md#apple-inwgc43tfvihezlgmvzgk3tdmvzq): Constraints guide which hard register to put things in.
- [Modifiers](Modifiers.md#apple-jvxwi2lgnfsxe4y): More precise control over effects of constraints.
- [Machine Constraints](Machine-Constraints.md#apple-jvqwg2djnzss2q3pnzzxi4tbnfxhi4y): Existing constraints for some particular machines.
- [Define Constraints](Define-Constraints.md#apple-irswm2lomuwug33oon2heyljnz2hg): How to define machine-specific constraints.
- [C Constraint Interface](C-Constraint-Interface.md#apple-imwug33oon2heyljnz2c2sloorsxeztbmnsq): How to test constraints from C code.
