---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Vector-Operations.html
archived_at: '2026-07-15T07:31:03.096859Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Conversions](Conversions.md#apple-inxw45tfojzws33oom),
Previous: [Bit-Fields](Bit_002dFields.md#apple-ijuxixzqgazgirtjmvwgi4y),
Up: [RTL](RTL.md#apple-kjkey)

---

### 12.12 Vector Operations

All normal RTL expressions can be used with vector modes; they are
interpreted as operating on each part of the vector independently.
Additionally, there are a few new expressions to describe specific vector
operations.

**`(vec_merge:`m vec1 vec2 items`)`**
: This describes a merge operation between two vectors. The result is a vector
of mode m; its elements are selected from either vec1 or
vec2. Which elements are selected is described by items, which
is a bit mask represented by a `const_int`; a zero bit indicates the
corresponding element in the result vector is taken from vec2 while
a set bit indicates it is taken from vec1.

**`(vec_select:`m vec1 selection`)`**
: This describes an operation that selects parts of a vector. vec1 is
the source vector, selection is a `parallel` that contains a
`const_int` for each of the subparts of the result vector, giving the
number of the source subpart that should be stored into it.

**`(vec_concat:`m vec1 vec2`)`**
: Describes a vector concat operation. The result is a concatenation of the
vectors vec1 and vec2; its length is the sum of the lengths of
the two inputs.

**`(vec_duplicate:`m vec`)`**
: This operation converts a small vector into a larger one by duplicating the
input values. The output vector mode must have the same submodes as the
input vector mode, and the number of output parts must be an integer multiple
of the number of input parts.
