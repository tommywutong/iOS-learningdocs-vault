---
title: allocate
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorcontext/allocate
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/allocate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorcontext/allocate.json'
content_hash: 'sha256:64dfd8f344ab7bac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFAllocatorContext](../cfallocatorcontext.md)

# allocate

<sub>Instance Property</sub>

A prototype for a function callback that allocates memory of a requested size. In implementing this function, allocate a block of memory of at least `size` bytes and return a pointer to the start of the block. The `hint` argument is a bitfield that you should currently not use (that is, assign 0). The `size` parameter should always be greater than 0. If it is not, or if problems in allocation occur, return `NULL`. This function pointer may not be assigned `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allocate: CFAllocatorAllocateCallBack!
```
