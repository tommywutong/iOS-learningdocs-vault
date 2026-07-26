---
title: 'CFAllocatorDeallocate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfallocatordeallocate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatordeallocate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatordeallocate%28_%3A_%3A%29.json'
content_hash: 'sha256:8c9e3f66a2909a2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorDeallocate(_:_:)

<sub>Function</sub>

Deallocates a block of memory with a given allocator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAllocatorDeallocate(_ allocator: CFAllocator!, _ ptr: UnsafeMutableRawPointer!)
```

## Parameters

- `allocator` — The allocator that was used to allocate the block of memory pointed to by `ptr`.

- `ptr` — An untyped pointer to a block of memory to deallocate using `allocator`.

## Discussion

If the allocator does not specify a `deallocate` callback function, the memory is not deallocated.

### Special Considerations

You must use the same allocator to deallocate memory as was used to allocate it.

## See Also

### Managing Memory with an Allocator

- [CFAllocatorAllocate](<cfallocatorallocate(______).md>) — Allocates memory using the specified allocator.
- [CFAllocatorGetPreferredSizeForSize](<cfallocatorgetpreferredsizeforsize(______).md>) — Obtains the number of bytes likely to be allocated upon a specific request.
- [CFAllocatorReallocate](<cfallocatorreallocate(________).md>) — Reallocates memory using the specified allocator.
