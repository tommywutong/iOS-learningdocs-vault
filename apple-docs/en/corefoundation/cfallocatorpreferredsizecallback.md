---
title: CFAllocatorPreferredSizeCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorpreferredsizecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorpreferredsizecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorpreferredsizecallback.json'
content_hash: 'sha256:aaaef567bcd2d42e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorPreferredSizeCallBack

<sub>Type Alias</sub>

A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFAllocatorPreferredSizeCallBack = (CFIndex, CFOptionFlags, UnsafeMutableRawPointer?) -> CFIndex
```

## Parameters

- `size` — The amount of memory requested.

- `hint` — A bitfield that is currently not used (always set to 0).

- `info` — An untyped pointer to program-defined data.

## Return Value

The actual size the allocator is likely to allocate given this request.

## Discussion

A prototype for a function callback that determines whether there is enough free memory to satisfy a request. In implementing this function, return the actual size the allocator is likely to allocate given a request for a block of memory of size `size`. The `hint` argument is a bitfield that you should currently not use.

## See Also

### Callbacks

- [CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md) — A prototype for a function callback that allocates memory of a requested size.
- [CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md) — A prototype for a function callback that provides a description of the specified data.
- [CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md) — A prototype for a function callback that deallocates a block of memory.
- [CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md) — A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md) — A prototype for a function callback that releases the given data.
- [CFAllocatorRetainCallBack](cfallocatorretaincallback.md) — A prototype for a function callback that retains the given data.
