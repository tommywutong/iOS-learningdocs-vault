---
title: 'CFBitVectorCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorcreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorcreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorcreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:25d2d517fa053e6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorCreateCopy(_:_:)

<sub>Function</sub>

Creates an immutable bit vector that is a copy of another bit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorCreateCopy(_ allocator: CFAllocator!, _ bv: CFBitVector!) -> CFBitVector!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new bit vector. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `bv` — The bit vector to copy.

## Return Value

A new bit vector holding the same bit values as `bv`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Bit Vector

- [CFBitVectorCreate](<cfbitvectorcreate(______).md>) — Creates an immutable bit vector from a block of memory.
