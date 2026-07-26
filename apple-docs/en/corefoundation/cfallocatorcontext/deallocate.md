---
title: deallocate
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorcontext/deallocate
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/deallocate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorcontext/deallocate.json'
content_hash: 'sha256:f31bc4659c78da37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFAllocatorContext](../cfallocatorcontext.md)

# deallocate

<sub>Instance Property</sub>

A prototype for a function callback that deallocates a given block of memory. In implementing this function, make the block of memory pointed to by `ptr` available for subsequent reuse by the allocator but unavailable for continued use by the program. The `ptr` parameter cannot be `NULL` and if the `ptr` parameter is not a block of memory that has been previously allocated by the allocator, the results are undefined; abnormal program termination can occur. You can set this callback to `NULL`, in which case the [CFAllocatorDeallocate](<../cfallocatordeallocate(____).md>) function has no effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var deallocate: CFAllocatorDeallocateCallBack!
```
