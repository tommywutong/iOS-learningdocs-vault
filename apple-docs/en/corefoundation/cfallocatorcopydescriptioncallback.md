---
title: CFAllocatorCopyDescriptionCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorcopydescriptioncallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorcopydescriptioncallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorcopydescriptioncallback.json'
content_hash: 'sha256:9ab21977311cfd28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorCopyDescriptionCallBack

<sub>Type Alias</sub>

A prototype for a function callback that provides a description of the specified data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFAllocatorCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

## Parameters

- `info` — An untyped pointer to program-defined data.

## Return Value

A CFString object that describes the allocator. The caller is responsible for releasing this object.

## Discussion

A prototype for a function callback that provides a description of the data pointed to by the `info` field. In implementing this function, return a reference to a CFString object that describes your allocator, particularly some characteristics of your program-defined data.

## See Also

### Callbacks

- [CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md) — A prototype for a function callback that allocates memory of a requested size.
- [CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md) — A prototype for a function callback that deallocates a block of memory.
- [CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md) — A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md) — A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md) — A prototype for a function callback that releases the given data.
- [CFAllocatorRetainCallBack](cfallocatorretaincallback.md) — A prototype for a function callback that retains the given data.
