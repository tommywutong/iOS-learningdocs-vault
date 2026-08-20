---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Defining-Mode-Macros.html
archived_at: '2026-07-15T07:30:59.713269Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [String Substitutions](String-Substitutions.md#apple-kn2he2lom4wvg5lcon2gs5dvoruw63tt),
Up: [Mode Macros](Mode-Macros.md#apple-jvxwizjnjvqwg4tpom)

---

##### 12.22.1.1 Defining Mode Macros

The syntax for defining a mode macro is:

```
     (define_mode_macro name [(mode1 "cond1") ... (moden "condn")])
```

This allows subsequent `.md` file constructs to use the mode suffix
`:`name. Every construct that does so will be expanded
n times, once with every use of `:`name replaced by
`:`mode1, once with every use replaced by `:`mode2,
and so on. In the expansion for a particular modei, every
C condition will also require that condi be true.

For example:

```
     (define_mode_macro P [(SI "Pmode == SImode") (DI "Pmode == DImode")])
```

defines a new mode suffix `:P`. Every construct that uses
`:P` will be expanded twice, once with every `:P` replaced
by `:SI` and once with every `:P` replaced by `:DI`.
The `:SI` version will only apply if `Pmode == SImode` and
the `:DI` version will only apply if `Pmode == DImode`.

As with other `.md` conditions, an empty string is treated
as “always true”. `(`mode `"")` can also be abbreviated
to mode. For example:

```
     (define_mode_macro GPR [SI (DI "TARGET_64BIT")])
```

means that the `:DI` expansion only applies if `TARGET_64BIT`
but that the `:SI` expansion has no such constraint.

Macros are applied in the order they are defined. This can be
significant if two macros are used in a construct that requires
string substitutions. See [String Substitutions](String-Substitutions.md#apple-kn2he2lom4wvg5lcon2gs5dvoruw63tt).
