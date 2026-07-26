---
title: 'CFAllocatorAllocate(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfallocatorallocate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorallocate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorallocate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1e4d24ff1ed1df4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorAllocate(_:_:_:)

<sub>Function</sub>

Allocates memory using the specified allocator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAllocatorAllocate(_ allocator: CFAllocator!, _ size: CFIndex, _ hint: CFOptionFlags) -> UnsafeMutableRawPointer!
```

## Parameters

- `allocator` — The allocator to use to allocate the memory. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `size` — The size of the memory to allocate.

- `hint` — A bitfield containing flags that suggest how memory is to be allocated. `0` indicates no hints. No hints are currently defined, so only `0` should be passed for this value.

## Return Value

A pointer to the newly allocated memory.

## See Also

### Managing Memory with an Allocator

- [CFAllocatorDeallocate](<cfallocatordeallocate(____).md>) — Deallocates a block of memory with a given allocator.
- [CFAllocatorGetPreferredSizeForSize](<cfallocatorgetpreferredsizeforsize(______).md>) — Obtains the number of bytes likely to be allocated upon a specific request.
- [CFAllocatorReallocate](<cfallocatorreallocate(________).md>) — Reallocates memory using the specified allocator.
