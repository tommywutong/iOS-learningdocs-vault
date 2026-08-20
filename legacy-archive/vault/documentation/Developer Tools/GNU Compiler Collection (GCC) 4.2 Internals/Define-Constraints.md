---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Define-Constraints.html
archived_at: '2026-07-15T07:31:01.691179Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [C Constraint Interface](C-Constraint-Interface.md#apple-imwug33oon2heyljnz2c2sloorsxeztbmnsq),
Previous: [Machine Constraints](Machine-Constraints.md#apple-jvqwg2djnzss2q3pnzzxi4tbnfxhi4y),
Up: [Constraints](Constraints.md#apple-inxw443uojqws3tuom)

---

#### 14.8.6 Defining Machine-Specific Constraints

Machine-specific constraints fall into two categories: register and
non-register constraints. Within the latter category, constraints
which allow subsets of all possible memory or address operands should
be specially marked, to give `reload` more information.

Machine-specific constraints can be given names of arbitrary length,
but they must be entirely composed of letters, digits, underscores
(``_`'), and angle brackets (``< >`'). Like C identifiers, they
must begin with a letter or underscore.

In order to avoid ambiguity in operand constraint strings, no
constraint can have a name that begins with any other constraint's
name. For example, if `x` is defined as a constraint name,
`xy` may not be, and vice versa. As a consequence of this rule,
no constraint may begin with one of the generic constraint letters:
``E F V X g i m n o p r s`'.

Register constraints correspond directly to register classes.
See [Register Classes](Register-Classes.md#apple-kjswo2ltorsxelkdnrqxg43fom). There is thus not much flexibility in their
definitions.

— MD Expression: __define_register_constraint__ name regclass docstring
> All three arguments are string constants.
> name is the name of the constraint, as it will appear in
> `match_operand` expressions. regclass can be either the
> name of the corresponding register class (see [Register Classes](Register-Classes.md#apple-kjswo2ltorsxelkdnrqxg43fom)),
> or a C expression which evaluates to the appropriate register class.
> If it is an expression, it must have no side effects, and it cannot
> look at the operand. The usual use of expressions is to map some
> register constraints to `NO_REGS` when the register class
> is not available on a given subarchitecture.
>
> docstring is a sentence documenting the meaning of the
> constraint. Docstrings are explained further below.

Non-register constraints are more like predicates: the constraint
definition gives a Boolean expression which indicates whether the
constraint matches.

— MD Expression: __define_constraint__ name docstring exp
> The name and docstring arguments are the same as for
> `define_register_constraint`, but note that the docstring comes
> immediately after the name for these expressions. exp is an RTL
> expression, obeying the same rules as the RTL expressions in predicate
> definitions. See [Defining Predicates](Defining-Predicates.md#apple-irswm2lonfxgolkqojswi2ldmf2gk4y), for details. If it
> evaluates true, the constraint matches; if it evaluates false, it
> doesn't. Constraint expressions should indicate which RTL codes they
> might match, just like predicate expressions.
>
> `match_test` C expressions have access to the
> following variables:
>
> **op**
> : The RTL object defining the operand.
>
> **mode**
> : The machine mode of op.
>
> **ival**
> : ``INTVAL (op)`', if op is a `const_int`.
>
> **hval**
> : ``CONST_DOUBLE_HIGH (op)`', if op is an integer
> `const_double`.
>
> **lval**
> : ``CONST_DOUBLE_LOW (op)`', if op is an integer
> `const_double`.
>
> **rval**
> : ``CONST_DOUBLE_REAL_VALUE (op)`', if op is a floating-point
> `const_double`.
>
> The \*val variables should only be used once another piece of the
> expression has verified that op is the appropriate kind of RTL
> object.

Most non-register constraints should be defined with
`define_constraint`. The remaining two definition expressions
are only appropriate for constraints that should be handled specially
by `reload` if they fail to match.

— MD Expression: __define_memory_constraint__ name docstring exp
> Use this expression for constraints that match a subset of all memory
> operands: that is, `reload` can make them match by converting the
> operand to the form ``(mem (reg X))`', where X is a
> base register (from the register class specified by
> `BASE_REG_CLASS`, see [Register Classes](Register-Classes.md#apple-kjswo2ltorsxelkdnrqxg43fom)).
>
> For example, on the S/390, some instructions do not accept arbitrary
> memory references, but only those that do not make use of an index
> register. The constraint letter ``Q`' is defined to represent a
> memory address of this type. If ``Q`' is defined with
> `define_memory_constraint`, a ``Q`' constraint can handle any
> memory operand, because `reload` knows it can simply copy the
> memory address into a base register if required. This is analogous to
> the way a ``o`' constraint can handle any memory operand.
>
> The syntax and semantics are otherwise identical to
> `define_constraint`.

— MD Expression: __define_address_constraint__ name docstring exp
> Use this expression for constraints that match a subset of all address
> operands: that is, `reload` can make the constraint match by
> converting the operand to the form ``(reg X)`', again
> with X a base register.
>
> Constraints defined with `define_address_constraint` can only be
> used with the `address_operand` predicate, or machine-specific
> predicates that work the same way. They are treated analogously to
> the generic ``p`' constraint.
>
> The syntax and semantics are otherwise identical to
> `define_constraint`.

For historical reasons, names beginning with the letters ``G H`'
are reserved for constraints that match only `const_double`s, and
names beginning with the letters ``I J K L M N O P`' are reserved
for constraints that match only `const_int`s. This may change in
the future. For the time being, constraints with these names must be
written in a stylized form, so that `genpreds` can tell you did
it correctly:

```
     (define_constraint "[GHIJKLMNOP]..."
       "doc..."
       (and (match_code "const_int")  ; const_double for G/H
            condition...))            ; usually a match_test
```

It is fine to use names beginning with other letters for constraints
that match `const_double`s or `const_int`s.

Each docstring in a constraint definition should be one or more complete
sentences, marked up in Texinfo format. _They are currently unused._
In the future they will be copied into the GCC manual, in [Machine Constraints](Machine-Constraints.md#apple-jvqwg2djnzss2q3pnzzxi4tbnfxhi4y), replacing the hand-maintained tables currently found in
that section. Also, in the future the compiler may use this to give
more helpful diagnostics when poor choice of `asm` constraints
causes a reload failure.

If you put the pseudo-Texinfo directive ``@internal`' at the
beginning of a docstring, then (in the future) it will appear only in
the internals manual's version of the machine-specific constraint tables.
Use this for constraints that should not appear in `asm` statements.
