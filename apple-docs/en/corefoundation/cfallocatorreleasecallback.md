---
title: CFAllocatorReleaseCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorreleasecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorreleasecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorreleasecallback.json'
content_hash: 'sha256:5aa88056422102c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorReleaseCallBack

<sub>Type Alias</sub>

A prototype for a function callback that releases the given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFAllocatorReleaseCallBack = (UnsafeRawPointer?) -> Void
```

## Parameters

- `info` — The data to be released.

## Discussion

A prototype for a function callback that releases the data pointed to by the `info` field. In implementing this function, release (or free) the data you have defined for the allocator context.

## See Also

### Callbacks

- [CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md) — A prototype for a function callback that allocates memory of a requested size.
- [CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md) — A prototype for a function callback that provides a description of the specified data.
- [CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md) — A prototype for a function callback that deallocates a block of memory.
- [CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md) — A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md) — A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [CFAllocatorRetainCallBack](cfallocatorretaincallback.md) — A prototype for a function callback that retains the given data.
