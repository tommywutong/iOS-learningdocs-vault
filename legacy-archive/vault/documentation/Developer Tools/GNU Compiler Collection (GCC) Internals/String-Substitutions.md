---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/String-Substitutions.html
archived_at: '2026-07-15T07:31:00.841136Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Examples](Examples.md#apple-iv4gc3lqnrsxg),
Previous: [Defining Mode Macros](Defining-Mode-Macros.md#apple-irswm2lonfxgolknn5sgklknmfrxe33t),
Up: [Mode Macros](Mode-Macros.md#apple-jvxwizjnjvqwg4tpom)

---

##### 12.22.1.2 String Substitution in Mode Macros

If an `.md` file construct uses mode macros, each version of the
construct will often need slightly different strings. For example:

- When a `define_expand` defines several `add`m`3` patterns
  (see [Standard Names](Standard-Names.md#apple-kn2gc3temfzgilkomfwwk4y)), each expander will need to use the
  appropriate mode name for m.
- When a `define_insn` defines several instruction patterns,
  each instruction will often use a different assembler mnemonic.

GCC supports such variations through a system of “mode attributes”.
There are two standard attributes: `mode`, which is the name of
the mode in lower case, and `MODE`, which is the same thing in
upper case. You can define other attributes using:

```
     (define_mode_attr name [(mode1 "value1") ... (moden "valuen")])
```

where name is the name of the attribute and valuei
is the value associated with modei.

When GCC replaces some :macro with :mode, it will
scan each string in the pattern for sequences of the form
`<`macro`:`attr`>`, where attr is the name of
a mode attribute. If the attribute is defined for mode, the
whole `<...>` sequence will be replaced by the appropriate
attribute value.

For example, suppose an `.md` file has:

```
     (define_mode_macro P [(SI "Pmode == SImode") (DI "Pmode == DImode")])
     (define_mode_attr load [(SI "lw") (DI "ld")])
```

If one of the patterns that uses `:P` contains the string
`"<P:load>\t%0,%1"`, the `SI` version of that pattern
will use `"lw\t%0,%1"` and the `DI` version will use
`"ld\t%0,%1"`.

The macro`:` prefix may be omitted, in which case the
substitution will be attempted for every macro expansion.
