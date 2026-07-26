---
title: Invalid variable-length array
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/invalid-variable-length-array
source_url: 'https://developer.apple.com/documentation/xcode/invalid-variable-length-array'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/invalid-variable-length-array.json'
content_hash: 'sha256:94d2169d3c43a635'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)

# Invalid variable-length array

<sub>Article</sub>

Detects negative array bounds.

## Overview

Use this check to detect negative array bounds. Variable-length arrays with a negative length have undefined behavior, and may cause stack corruption. Available in Xcode 9 and later.

### Negative variable-length array bounds in C

In the following code, the call to the `invalid_index_returning_function` function returns a negative number that results in an invalid array:

```occ
int invalid_index_returning_function() {
    return -1;
}
int idx = invalid_index_returning_function();
int array[idx]; // Error: invalid array length
```

#### Solution

Fix the issue by checking array bounds before constructing arrays.

## See Also

### Undefined Behavior Sanitizer

- [Misaligned pointer](misaligned-pointer.md) — Detects when code accesses a misaligned pointer or creates a misaligned reference.
- [Invalid Boolean value](invalid-boolean.md) — Detects when a program accesses a Boolean variable and its value isn’t true or false.
- [Out-of-bounds array access](out-of-bounds-array-access.md) — Detects out-of-bounds access of arrays.
- [Invalid enumeration value](invalid-enumeration-value.md) — Detects when an enumeration variable has an invalid value.
- [Reaching of unreachable point](reaching-of-unreachable-point.md) — Detects when a program reaches an unreachable point.
- [Dynamic type violation](dynamic-type-violation.md) — Detects when an object has the wrong dynamic type.
- [Invalid float cast](invalid-float-cast.md) — Detects out-of-range casts to, from, or between floating-point types.
- [Division by zero](division-by-zero.md) — Detects division where the divisor is zero.
- [Nonnull argument violation](nonnull-argument-violation.md) — Detects when an argument incorrectly receives a null value.
- [Nonnull return value violation](nonnull-return-value-violation.md) — Detects when a function incorrectly returns null.
- [Nonnull variable assignment violation](nonnull-variable-assignment-violation.md) — Detects when you incorrectly assign null to a variable.
- [Null reference creation and null pointer dereference](null-reference-creation-and-null-pointer-dereference.md) — Detects the creation of null references and null pointer dereferences.
- [Invalid object size](invalid-object-size.md) — Detects invalid pointer casts due to differences in the sizes of types.
- [Invalid shift](invalid-shift.md) — Detects invalid and overflowing shifts.
- [Integer overflow](integer-overflow.md) — Detects overflow in arithmetic.
