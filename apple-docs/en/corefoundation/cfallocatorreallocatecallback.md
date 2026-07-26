---
title: CFAllocatorReallocateCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorreallocatecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorreallocatecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorreallocatecallback.json'
content_hash: 'sha256:67aa221a57b61f3c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorReallocateCallBack

<sub>Type Alias</sub>

A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFAllocatorReallocateCallBack = (UnsafeMutableRawPointer?, CFIndex, CFOptionFlags, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?
```

## Parameters

- `ptr` — The block of memory to resize.

- `newsize` — The size of the new allocation.

- `hint` — A bitfield that is currently not used (always set to 0).

- `info` — An untyped pointer to program-defined data.

## Return Value

Pointer to the new block of memory.

## Discussion

In implementing this function, change the size of the block of memory pointed to by `ptr` to the size specified by `newsize` and return the pointer to the larger block of memory. Return NULL on any reallocation failure, leaving the old block of memory untouched. Also return NULL immediately if any of the following conditions if the ptr parameter is NULL or the `newsize` parameter is not greater than 0. Leave the contents of the old block of memory unchanged up to the lesser of the new or old sizes. If the `ptr` parameter is not a block of memory that has been previously allocated by the allocator, the results are undefined; abnormal program termination can occur. The `hint` argument is a bitfield that you should currently not use (that is, assign 0).

## See Also

### Callbacks

- [CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md) — A prototype for a function callback that allocates memory of a requested size.
- [CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md) — A prototype for a function callback that provides a description of the specified data.
- [CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md) — A prototype for a function callback that deallocates a block of memory.
- [CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md) — A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md) — A prototype for a function callback that releases the given data.
- [CFAllocatorRetainCallBack](cfallocatorretaincallback.md) — A prototype for a function callback that retains the given data.
