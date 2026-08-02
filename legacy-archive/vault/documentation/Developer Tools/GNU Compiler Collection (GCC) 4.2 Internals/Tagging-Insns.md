---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Tagging-Insns.html
archived_at: '2026-07-15T07:31:02.938916Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Attr Example](Attr-Example.md#apple-if2hi4rniv4gc3lqnrsq),
Previous: [Expressions](Expressions.md#apple-iv4ha4tfonzws33oom),
Up: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)

---

#### 14.19.3 Assigning Attribute Values to Insns

The value assigned to an attribute of an insn is primarily determined by
which pattern is matched by that insn (or which `define_peephole`
generated it). Every `define_insn` and `define_peephole` can
have an optional last argument to specify the values of attributes for
matching insns. The value of any attribute not specified in a particular
insn is set to the default value for that attribute, as specified in its
`define_attr`. Extensive use of default values for attributes
permits the specification of the values for only one or two attributes
in the definition of most insn patterns, as seen in the example in the
next section.

The optional last argument of `define_insn` and
`define_peephole` is a vector of expressions, each of which defines
the value for a single attribute. The most general way of assigning an
attribute's value is to use a `set` expression whose first operand is an
`attr` expression giving the name of the attribute being set. The
second operand of the `set` is an attribute expression
(see [Expressions](Expressions.md#apple-iv4ha4tfonzws33oom)) giving the value of the attribute.

When the attribute value depends on the ``alternative`' attribute
(i.e., which is the applicable alternative in the constraint of the
insn), the `set_attr_alternative` expression can be used. It
allows the specification of a vector of attribute expressions, one for
each alternative.

When the generality of arbitrary attribute expressions is not required,
the simpler `set_attr` expression can be used, which allows
specifying a string giving either a single attribute value or a list
of attribute values, one for each alternative.

The form of each of the above specifications is shown below. In each case,
name is a string specifying the attribute to be set.

**`(set_attr` name value-string`)`**
: value-string is either a string giving the desired attribute value,
or a string containing a comma-separated list giving the values for
succeeding alternatives. The number of elements must match the number
of alternatives in the constraint of the insn pattern.

Note that it may be useful to specify ``*`' for some alternative, in
which case the attribute will assume its default value for insns matching
that alternative.

**`(set_attr_alternative` name `[`value1 value2 `...])`**
: Depending on the alternative of the insn, the value will be one of the
specified values. This is a shorthand for using a `cond` with
tests on the ``alternative`' attribute.

**`(set (attr` name`)` value`)`**
: The first operand of this `set` must be the special RTL expression
`attr`, whose sole operand is a string giving the name of the
attribute being set. value is the value of the attribute.

The following shows three different ways of representing the same
attribute value specification:

```
     (set_attr "type" "load,store,arith")

     (set_attr_alternative "type"
                           [(const_string "load") (const_string "store")
                            (const_string "arith")])

     (set (attr "type")
          (cond [(eq_attr "alternative" "1") (const_string "load")
                 (eq_attr "alternative" "2") (const_string "store")]
                (const_string "arith")))
```

The `define_asm_attributes` expression provides a mechanism to
specify the attributes assigned to insns produced from an `asm`
statement. It has the form:

```
     (define_asm_attributes [attr-sets])
```

where attr-sets is specified the same as for both the
`define_insn` and the `define_peephole` expressions.

These values will typically be the “worst case” attribute values. For
example, they might indicate that the condition code will be clobbered.

A specification for a `length` attribute is handled specially. The
way to compute the length of an `asm` insn is to multiply the
length specified in the expression `define_asm_attributes` by the
number of machine instructions specified in the `asm` statement,
determined by counting the number of semicolons and newlines in the
string. Therefore, the value of the `length` attribute specified
in a `define_asm_attributes` should be the maximum possible length
of a single machine instruction.
