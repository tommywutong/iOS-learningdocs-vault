---
title: Invalid float cast
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/invalid-float-cast
source_url: 'https://developer.apple.com/documentation/xcode/invalid-float-cast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/invalid-float-cast.json'
content_hash: 'sha256:736ae067a707eecc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)

# Invalid float cast

<sub>Article</sub>

Detects out-of-range casts to, from, or between floating-point types.

## Overview

Use this check to detect out-of-range casts to, from, or between floating-point types. Invalid casts have undefined behavior, and typically yield arbitrary values. These values may differ from platform to platform. Available in Xcode 9 and later.

### Invalid assignment of a double to a float in C

The cast from `n` to `m` results in undefined behavior because the destination type can’t represent its value.

```occ
double n = 10e50;
float m = (float)n; // Error: 10e50 can't be represented as a float.
```

#### Solution

Use a different destination type or avoid the cast altogether.

## See Also

### Undefined Behavior Sanitizer

- [Misaligned pointer](misaligned-pointer.md) — Detects when code accesses a misaligned pointer or creates a misaligned reference.
- [Invalid Boolean value](invalid-boolean.md) — Detects when a program accesses a Boolean variable and its value isn’t true or false.
- [Out-of-bounds array access](out-of-bounds-array-access.md) — Detects out-of-bounds access of arrays.
- [Invalid enumeration value](invalid-enumeration-value.md) — Detects when an enumeration variable has an invalid value.
- [Reaching of unreachable point](reaching-of-unreachable-point.md) — Detects when a program reaches an unreachable point.
- [Dynamic type violation](dynamic-type-violation.md) — Detects when an object has the wrong dynamic type.
- [Division by zero](division-by-zero.md) — Detects division where the divisor is zero.
- [Nonnull argument violation](nonnull-argument-violation.md) — Detects when an argument incorrectly receives a null value.
- [Nonnull return value violation](nonnull-return-value-violation.md) — Detects when a function incorrectly returns null.
- [Nonnull variable assignment violation](nonnull-variable-assignment-violation.md) — Detects when you incorrectly assign null to a variable.
- [Null reference creation and null pointer dereference](null-reference-creation-and-null-pointer-dereference.md) — Detects the creation of null references and null pointer dereferences.
- [Invalid object size](invalid-object-size.md) — Detects invalid pointer casts due to differences in the sizes of types.
- [Invalid shift](invalid-shift.md) — Detects invalid and overflowing shifts.
- [Integer overflow](integer-overflow.md) — Detects overflow in arithmetic.
- [Invalid variable-length array](invalid-variable-length-array.md) — Detects negative array bounds.
