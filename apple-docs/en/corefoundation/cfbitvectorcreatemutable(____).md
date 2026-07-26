---
title: 'CFBitVectorCreateMutable(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorcreatemutable(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorcreatemutable(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorcreatemutable%28_%3A_%3A%29.json'
content_hash: 'sha256:3799ade32afc4dee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorCreateMutable(_:_:)

<sub>Function</sub>

Creates a mutable bit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex) -> CFMutableBitVector!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `capacity` — The maximum number of values that can be contained by the new bit vector. The bit vector starts empty and can grow to this number of values (and it can have less). Pass `0` to specify that the maximum capacity is not limited. The value must not be negative.

## Return Value

A new bit vector. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Related Documentation

- [Collections Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)
- [CFBitVectorSetCount](<cfbitvectorsetcount(____).md>) — Changes the size of a mutable bit vector.

### Creating a CFMutableBitVector Object

- [CFBitVectorCreateMutableCopy](<cfbitvectorcreatemutablecopy(______).md>) — Creates a new mutable bit vector from a pre-existing bit vector.
