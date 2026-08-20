---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/C-Constraint-Interface.html
archived_at: '2026-07-15T07:31:01.266572Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Define Constraints](Define-Constraints.md#apple-irswm2lomuwug33oon2heyljnz2hg),
Up: [Constraints](Constraints.md#apple-inxw443uojqws3tuom)

---

#### 14.8.7 Testing constraints from C

It is occasionally useful to test a constraint from C code rather than
implicitly via the constraint string in a `match_operand`. The
generated file `tm_p.h` declares a few interfaces for working
with machine-specific constraints. None of these interfaces work with
the generic constraints described in [Simple Constraints](Simple-Constraints.md#apple-knuw24dmmuwug33oon2heyljnz2hg). This
may change in the future.

__Warning:__ `tm_p.h` may declare other functions that
operate on constraints, besides the ones documented here. Do not use
those functions from machine-dependent code. They exist to implement
the old constraint interface that machine-independent components of
the compiler still expect. They will change or disappear in the
future.

Some valid constraint names are not valid C identifiers, so there is a
mangling scheme for referring to them from C. Constraint names that
do not contain angle brackets or underscores are left unchanged.
Underscores are doubled, each ``<`' is replaced with ``_l`', and
each ``>`' with ``_g`'. Here are some examples:

```

```

|  |  |
| --- | --- |
| __Original__ | __Mangled__ |
| `x` | `x` |
| `P42x` | `P42x` |
| `P4_x` | `P4__x` |
| `P4>x` | `P4_gx` |
| `P4>>` | `P4_g_g` |
| `P4_g>` | `P4__g_g` |

Throughout this section, the variable c is either a constraint
in the abstract sense, or a constant from `enum constraint_num`;
the variable m is a mangled constraint name (usually as part of
a larger identifier).

— Enum: __constraint_num__
> For each machine-specific constraint, there is a corresponding
> enumeration constant: ``CONSTRAINT_`' plus the mangled name of the
> constraint. Functions that take an `enum constraint_num` as an
> argument expect one of these constants.
>
> Machine-independent constraints do not have associated constants.
> This may change in the future.

— Function: inline bool __satisfies_constraint___m (rtx exp)
> For each machine-specific, non-register constraint m, there is
> one of these functions; it returns `true` if exp satisfies the
> constraint. These functions are only visible if `rtl.h` was included
> before `tm_p.h`.

— Function: bool __constraint_satisfied_p__ (rtx exp, enum constraint_num c)
> Like the `satisfies_constraint_`m functions, but the
> constraint to test is given as an argument, c. If c
> specifies a register constraint, this function will always return
> `false`.

— Function: enum reg_class __regclass_for_constraint__ (enum constraint_num c)
> Returns the register class associated with c. If c is not
> a register constraint, or those registers are not available for the
> currently selected subtarget, returns `NO_REGS`.

Here is an example use of `satisfies_constraint_`m. In
peephole optimizations (see [Peephole Definitions](Peephole-Definitions.md#apple-kbswk4din5wgklkemvtgs3tjoruw63tt)), operand
constraint strings are ignored, so if there are relevant constraints,
they must be tested in the C condition. In the example, the
optimization is applied if operand 2 does _not_ satisfy the
``K`' constraint. (This is a simplified version of a peephole
definition from the i386 machine description.)

```
     (define_peephole2
       [(match_scratch:SI 3 "r")
        (set (match_operand:SI 0 "register_operand" "")
         (mult:SI (match_operand:SI 1 "memory_operand" "")
              (match_operand:SI 2 "immediate_operand" "")))]

       "!satisfies_constraint_K (operands[2])"

       [(set (match_dup 3) (match_dup 1))
        (set (match_dup 0) (mult:SI (match_dup 3) (match_dup 2)))]

       "")
```
