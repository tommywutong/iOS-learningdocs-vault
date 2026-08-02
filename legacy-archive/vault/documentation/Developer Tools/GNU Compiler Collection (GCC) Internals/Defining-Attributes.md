---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Defining-Attributes.html
archived_at: '2026-07-15T07:30:59.708003Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Expressions](Expressions.md#apple-iv4ha4tfonzws33oom),
Up: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)

---

#### 12.19.1 Defining Attributes and their Values

The `define_attr` expression is used to define each attribute required
by the target machine. It looks like:

```
     (define_attr name list-of-values default)
```

name is a string specifying the name of the attribute being defined.

list-of-values is either a string that specifies a comma-separated
list of values that can be assigned to the attribute, or a null string to
indicate that the attribute takes numeric values.

default is an attribute expression that gives the value of this
attribute for insns that match patterns whose definition does not include
an explicit value for this attribute. See [Attr Example](Attr-Example.md#apple-if2hi4rniv4gc3lqnrsq), for more
information on the handling of defaults. See [Constant Attributes](Constant-Attributes.md#apple-inxw443umfxhilkbor2he2lcov2gk4y),
for information on attributes that do not depend on any particular insn.

For each defined attribute, a number of definitions are written to the
`insn-attr.h` file. For cases where an explicit set of values is
specified for an attribute, the following are defined:

- A ``#define`' is written for the symbol ``HAVE_ATTR_name`'.
- An enumerated class is defined for ``attr_name`' with
  elements of the form ``upper-name_upper-value`' where
  the attribute name and value are first converted to uppercase.
- A function ``get_attr_name`' is defined that is passed an insn and
  returns the attribute value for that insn.

For example, if the following is present in the `md` file:

```
     (define_attr "type" "branch,fp,load,store,arith" ...)
```

the following lines will be written to the file `insn-attr.h`.

```
     #define HAVE_ATTR_type
     enum attr_type {TYPE_BRANCH, TYPE_FP, TYPE_LOAD,
                      TYPE_STORE, TYPE_ARITH};
     extern enum attr_type get_attr_type ();
```

If the attribute takes numeric values, no `enum` type will be
defined and the function to obtain the attribute's value will return
`int`.
