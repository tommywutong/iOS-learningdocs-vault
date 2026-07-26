---
title: 'CFBitVectorCreate(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorcreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorcreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorcreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:680779b7c90e85a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorCreate(_:_:_:)

<sub>Function</sub>

Creates an immutable bit vector from a block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ numBits: CFIndex) -> CFBitVector!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new bit vector. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `bytes` — A pointer to the bit values to store in the new bit vector. The values are copied into the bit vector’s own memory. The bit indices are numbered left-to-right with `0` being the left-most, or most-significant, bit in the byte stream.

- `numBits` — The number of bits in the bit vector.

## Return Value

A new bit vector. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Bit Vector

- [CFBitVectorCreateCopy](<cfbitvectorcreatecopy(____).md>) — Creates an immutable bit vector that is a copy of another bit vector.
