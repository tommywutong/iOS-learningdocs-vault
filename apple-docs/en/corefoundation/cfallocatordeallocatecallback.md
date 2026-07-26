---
title: CFAllocatorDeallocateCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatordeallocatecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatordeallocatecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatordeallocatecallback.json'
content_hash: 'sha256:dbbcc98e4dcae6e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorDeallocateCallBack

<sub>Type Alias</sub>

A prototype for a function callback that deallocates a block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFAllocatorDeallocateCallBack = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `ptr` — The block of memory to deallocate.

- `info` — An untyped pointer to program-defined data.

## Discussion

A prototype for a function callback that deallocates a given block of memory. In implementing this function, make the block of memory pointed to by `ptr` available for subsequent reuse by the allocator but unavailable for continued use by the program. The `ptr` parameter cannot be NULL and if the `ptr` parameter is not a block of memory that has been previously allocated by the allocator, the results are undefined; abnormal program termination can occur.

## See Also

### Callbacks

- [CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md) — A prototype for a function callback that allocates memory of a requested size.
- [CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md) — A prototype for a function callback that provides a description of the specified data.
- [CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md) — A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md) — A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md) — A prototype for a function callback that releases the given data.
- [CFAllocatorRetainCallBack](cfallocatorretaincallback.md) — A prototype for a function callback that retains the given data.
