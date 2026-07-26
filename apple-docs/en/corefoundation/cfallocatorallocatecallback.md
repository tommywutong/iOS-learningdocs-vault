---
title: CFAllocatorAllocateCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorallocatecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorallocatecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorallocatecallback.json'
content_hash: 'sha256:e388c9017bf34714'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorAllocateCallBack

<sub>Type Alias</sub>

A prototype for a function callback that allocates memory of a requested size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFAllocatorAllocateCallBack = (CFIndex, CFOptionFlags, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?
```

## Parameters

- `allocSize` — This function allocates a block of memory of at least `allocSize` bytes (always greater than 0).

- `hint` — A bitfield that is currently not used (always set to 0).

- `info` — An untyped pointer to program-defined data. Allocate memory for the data and assign a pointer to it. This data is often control information for the allocator. It may be `NULL`.

## Return Value

A pointer to the start of the block.

## See Also

### Callbacks

- [CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md) — A prototype for a function callback that provides a description of the specified data.
- [CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md) — A prototype for a function callback that deallocates a block of memory.
- [CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md) — A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md) — A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md) — A prototype for a function callback that releases the given data.
- [CFAllocatorRetainCallBack](cfallocatorretaincallback.md) — A prototype for a function callback that retains the given data.
