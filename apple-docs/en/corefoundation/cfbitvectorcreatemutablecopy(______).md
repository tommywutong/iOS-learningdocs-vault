---
title: 'CFBitVectorCreateMutableCopy(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorcreatemutablecopy(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorcreatemutablecopy(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorcreatemutablecopy%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:839d08595515638d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorCreateMutableCopy(_:_:_:)

<sub>Function</sub>

Creates a new mutable bit vector from a pre-existing bit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ bv: CFBitVector!) -> CFMutableBitVector!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `capacity` — The maximum number of values that can be contained by the new bit vector. The bit vector starts with the same number of values as `bv` and can grow to this number of values (it can have less). Pass `0` to specify that the maximum capacity is not limited. If non-`0`, `capacity` must be large enough to hold all bit values from `bv`.

- `bv` — The bit vector to copy.

## Return Value

A new bit vector holding the same bit values as `bv`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029)

## See Also

### Related Documentation

- [CFBitVectorSetCount](<cfbitvectorsetcount(____).md>) — Changes the size of a mutable bit vector.

### Creating a CFMutableBitVector Object

- [CFBitVectorCreateMutable](<cfbitvectorcreatemutable(____).md>) — Creates a mutable bit vector.
