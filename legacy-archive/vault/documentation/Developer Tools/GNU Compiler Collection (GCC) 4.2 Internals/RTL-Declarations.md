---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/RTL-Declarations.html
archived_at: '2026-07-15T07:31:02.642904Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Side Effects](Side-Effects.md#apple-knuwizjnivtgmzldorzq),
Previous: [Conversions](Conversions.md#apple-inxw45tfojzws33oom),
Up: [RTL](RTL.md#apple-kjkey)

---

### 12.14 Declarations

Declaration expression codes do not represent arithmetic operations
but rather state assertions about their operands.

**`(strict_low_part (subreg:`m `(reg:`n r`) 0))`**
: This expression code is used in only one context: as the destination operand of a
`set` expression. In addition, the operand of this expression
must be a non-paradoxical `subreg` expression.

The presence of `strict_low_part` says that the part of the
register which is meaningful in mode n, but is not part of
mode m, is not to be altered. Normally, an assignment to such
a subreg is allowed to have undefined effects on the rest of the
register when m is less than a word.
