---
title: reallocate
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorcontext/reallocate
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/reallocate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorcontext/reallocate.json'
content_hash: 'sha256:08e8d65996be7748'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFAllocatorContext](../cfallocatorcontext.md)

# reallocate

<sub>Instance Property</sub>

A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var reallocate: CFAllocatorReallocateCallBack!
```

## Discussion

When implementing this function, change the size of the block of memory pointed to by `ptr` to the size specified by `newsize` and return the pointer to the larger block of memory. Return `NULL` on any reallocation failure, leaving the old block of memory untouched. Also return `NULL` immediately if any of the following conditions apply:

The `ptr` parameter is `NULL`.

The `newsize` parameter is not greater than 0.

Leave the contents of the old block of memory unchanged up to the lesser of the new or old sizes. If the `ptr` parameter is not a block of memory that has been previously allocated by the allocator, the results are undefined; abnormal program termination can occur. The hint argument is a bitfield that you should currently not use (that is, assign 0). If you set this callback to `NULL` the `CFAllocatorReallocate(_:_:_:_:)` function returns `NULL` in most cases when it attempts to use this allocator.
