---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Predicates.html
archived_at: '2026-07-15T07:31:02.602557Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Constraints](Constraints.md#apple-inxw443uojqws3tuom),
Previous: [Output Statement](Output-Statement.md#apple-j52xi4dvoqwvg5dborsw2zlooq),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.7 Predicates

A predicate determines whether a `match_operand` or
`match_operator` expression matches, and therefore whether the
surrounding instruction pattern will be used for that combination of
operands. GCC has a number of machine-independent predicates, and you
can define machine-specific predicates as needed. By convention,
predicates used with `match_operand` have names that end in
``_operand`', and those used with `match_operator` have names
that end in ``_operator`'.

All predicates are Boolean functions (in the mathematical sense) of
two arguments: the RTL expression that is being considered at that
position in the instruction pattern, and the machine mode that the
`match_operand` or `match_operator` specifies. In this
section, the first argument is called op and the second argument
mode. Predicates can be called from C as ordinary two-argument
functions; this can be useful in output templates or other
machine-specific code.

Operand predicates can allow operands that are not actually acceptable
to the hardware, as long as the constraints give reload the ability to
fix them up (see [Constraints](Constraints.md#apple-inxw443uojqws3tuom)). However, GCC will usually generate
better code if the predicates specify the requirements of the machine
instructions as closely as possible. Reload cannot fix up operands
that must be constants (“immediate operands”); you must use a
predicate that allows only constants, or else enforce the requirement
in the extra condition.

Most predicates handle their mode argument in a uniform manner.
If mode is `VOIDmode` (unspecified), then op can have
any mode. If mode is anything else, then op must have the
same mode, unless op is a `CONST_INT` or integer
`CONST_DOUBLE`. These RTL expressions always have
`VOIDmode`, so it would be counterproductive to check that their
mode matches. Instead, predicates that accept `CONST_INT` and/or
integer `CONST_DOUBLE` check that the value stored in the
constant will fit in the requested mode.

Predicates with this behavior are called normal.
`genrecog` can optimize the instruction recognizer based on
knowledge of how normal predicates treat modes. It can also diagnose
certain kinds of common errors in the use of normal predicates; for
instance, it is almost always an error to use a normal predicate
without specifying a mode.

Predicates that do something different with their mode argument
are called special. The generic predicates
`address_operand` and `pmode_register_operand` are special
predicates. `genrecog` does not do any optimizations or
diagnosis when special predicates are used.

- [Machine-Independent Predicates](Machine_002dIndependent-Predicates.md#apple-jvqwg2djnzsv6mbqgjses3temvygk3temvxhilkqojswi2ldmf2gk4y): Predicates available to all back ends.
- [Defining Predicates](Defining-Predicates.md#apple-irswm2lonfxgolkqojswi2ldmf2gk4y): How to write machine-specific predicate
  functions.
