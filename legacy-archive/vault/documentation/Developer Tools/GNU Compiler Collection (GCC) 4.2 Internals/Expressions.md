---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Expressions.html
archived_at: '2026-07-15T07:31:01.831834Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Tagging Insns](Tagging-Insns.md#apple-krqwoz3jnzts2sloonxhg),
Previous: [Defining Attributes](Defining-Attributes.md#apple-irswm2lonfxgolkbor2he2lcov2gk4y),
Up: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)

---

#### 14.19.2 Attribute Expressions

RTL expressions used to define attributes use the codes described above
plus a few specific to attribute definitions, to be discussed below.
Attribute value expressions must have one of the following forms:

**`(const_int` i`)`**
: The integer i specifies the value of a numeric attribute. i
must be non-negative.

The value of a numeric attribute can be specified either with a
`const_int`, or as an integer represented as a string in
`const_string`, `eq_attr` (see below), `attr`,
`symbol_ref`, simple arithmetic expressions, and `set_attr`
overrides on specific instructions (see [Tagging Insns](Tagging-Insns.md#apple-krqwoz3jnzts2sloonxhg)).

**`(const_string` value`)`**
: The string value specifies a constant attribute value.
If value is specified as ``"*"`', it means that the default value of
the attribute is to be used for the insn containing this expression.
``"*"`' obviously cannot be used in the default expression
of a `define_attr`.

If the attribute whose value is being specified is numeric, value
must be a string containing a non-negative integer (normally
`const_int` would be used in this case). Otherwise, it must
contain one of the valid values for the attribute.

**`(if_then_else` test true-value false-value`)`**
: test specifies an attribute test, whose format is defined below.
The value of this expression is true-value if test is true,
otherwise it is false-value.

**`(cond [`test1 value1 `...]` default`)`**
: The first operand of this expression is a vector containing an even
number of expressions and consisting of pairs of test and value
expressions. The value of the `cond` expression is that of the
value corresponding to the first true test expression. If
none of the test expressions are true, the value of the `cond`
expression is that of the default expression.

test expressions can have one of the following forms:

**`(const_int` i`)`**
: This test is true if i is nonzero and false otherwise.

**`(not` test`)`

**`(ior` test1 test2`)`

**`(and` test1 test2`)`******
: These tests are true if the indicated logical function is true.

**`(match_operand:`m n pred constraints`)`**
: This test is true if operand n of the insn whose attribute value
is being determined has mode m (this part of the test is ignored
if m is `VOIDmode`) and the function specified by the string
pred returns a nonzero value when passed operand n and mode
m (this part of the test is ignored if pred is the null
string).

The constraints operand is ignored and should be the null string.

**`(le` arith1 arith2`)`

**`(leu` arith1 arith2`)`

**`(lt` arith1 arith2`)`

**`(ltu` arith1 arith2`)`

**`(gt` arith1 arith2`)`

**`(gtu` arith1 arith2`)`

**`(ge` arith1 arith2`)`

**`(geu` arith1 arith2`)`

**`(ne` arith1 arith2`)`

**`(eq` arith1 arith2`)`********************
: These tests are true if the indicated comparison of the two arithmetic
expressions is true. Arithmetic expressions are formed with
`plus`, `minus`, `mult`, `div`, `mod`,
`abs`, `neg`, `and`, `ior`, `xor`, `not`,
`ashift`, `lshiftrt`, and `ashiftrt` expressions.

`const_int` and `symbol_ref` are always valid terms (see [Insn Lengths](Insn-Lengths.md#apple-jfxhg3rnjrsw4z3unbzq),for additional forms). `symbol_ref` is a string
denoting a C expression that yields an `int` when evaluated by the
``get_attr_...`' routine. It should normally be a global
variable.

**`(eq_attr` name value`)`**
: name is a string specifying the name of an attribute.

value is a string that is either a valid value for attribute
name, a comma-separated list of values, or ``!`' followed by a
value or list. If value does not begin with a ``!`', this
test is true if the value of the name attribute of the current
insn is in the list specified by value. If value begins
with a ``!`', this test is true if the attribute's value is
_not_ in the specified list.

For example,

```
          (eq_attr "type" "load,store")

```

is equivalent to

```
          (ior (eq_attr "type" "load") (eq_attr "type" "store"))

```

If name specifies an attribute of ``alternative`', it refers to the
value of the compiler variable `which_alternative`
(see [Output Statement](Output-Statement.md#apple-j52xi4dvoqwvg5dborsw2zlooq)) and the values must be small integers. For
example,

```
          (eq_attr "alternative" "2,3")

```

is equivalent to

```
          (ior (eq (symbol_ref "which_alternative") (const_int 2))
               (eq (symbol_ref "which_alternative") (const_int 3)))

```

Note that, for most attributes, an `eq_attr` test is simplified in cases
where the value of the attribute being tested is known for all insns matching
a particular pattern. This is by far the most common case.

**`(attr_flag` name`)`**
: The value of an `attr_flag` expression is true if the flag
specified by name is true for the `insn` currently being
scheduled.

name is a string specifying one of a fixed set of flags to test.
Test the flags `forward` and `backward` to determine the
direction of a conditional branch. Test the flags `very_likely`,
`likely`, `very_unlikely`, and `unlikely` to determine
if a conditional branch is expected to be taken.

If the `very_likely` flag is true, then the `likely` flag is also
true. Likewise for the `very_unlikely` and `unlikely` flags.

This example describes a conditional branch delay slot which
can be nullified for forward branches that are taken (annul-true) or
for backward branches which are not taken (annul-false).

```
          (define_delay (eq_attr "type" "cbranch")
            [(eq_attr "in_branch_delay" "true")
             (and (eq_attr "in_branch_delay" "true")
                  (attr_flag "forward"))
             (and (eq_attr "in_branch_delay" "true")
                  (attr_flag "backward"))])

```

The `forward` and `backward` flags are false if the current
`insn` being scheduled is not a conditional branch.

The `very_likely` and `likely` flags are true if the
`insn` being scheduled is not a conditional branch.
The `very_unlikely` and `unlikely` flags are false if the
`insn` being scheduled is not a conditional branch.

`attr_flag` is only used during delay slot scheduling and has no
meaning to other passes of the compiler.

**`(attr` name`)`**
: The value of another attribute is returned. This is most useful
for numeric attributes, as `eq_attr` and `attr_flag`
produce more efficient code for non-numeric attributes.
