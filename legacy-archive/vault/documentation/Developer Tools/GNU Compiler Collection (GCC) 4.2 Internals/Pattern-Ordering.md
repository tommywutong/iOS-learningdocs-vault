---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Pattern-Ordering.html
archived_at: '2026-07-15T07:31:02.579401Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Dependent Patterns](Dependent-Patterns.md#apple-irsxazlomrsw45bnkbqxi5dfojxhg),
Previous: [Standard Names](Standard-Names.md#apple-kn2gc3temfzgilkomfwwk4y),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.10 When the Order of Patterns Matters

Sometimes an insn can match more than one instruction pattern. Then the
pattern that appears first in the machine description is the one used.
Therefore, more specific patterns (patterns that will match fewer things)
and faster instructions (those that will produce better code when they
do match) should usually go first in the description.

In some cases the effect of ordering the patterns can be used to hide
a pattern when it is not valid. For example, the 68000 has an
instruction for converting a fullword to floating point and another
for converting a byte to floating point. An instruction converting
an integer to floating point could match either one. We put the
pattern to convert the fullword first to make sure that one will
be used rather than the other. (Otherwise a large integer might
be generated as a single-byte immediate quantity, which would not work.)
Instead of using this pattern ordering it would be possible to make the
pattern for convert-a-byte smart enough to deal properly with any
constant value.
