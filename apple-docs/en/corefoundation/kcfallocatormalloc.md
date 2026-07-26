---
title: kCFAllocatorMalloc
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfallocatormalloc
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfallocatormalloc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfallocatormalloc.json'
content_hash: 'sha256:292180aaefa6ff89'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFAllocatorMalloc

<sub>Global Variable</sub>

This allocator uses `malloc()`, `realloc()`, and `free()`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFAllocatorMalloc: CFAllocator!
```

## Discussion

Typically you should not use this allocator, use `kCFAllocatorDefault` instead. This allocator is useful as the `bytesDeallocator` in CFData or `contentsDeallocator` in CFString where the memory was obtained as a result  of `malloc` type functions.

## See Also

### Constants

- [kCFAllocatorDefault](kcfallocatordefault.md) — This is a synonym for `NULL`.
- [kCFAllocatorSystemDefault](kcfallocatorsystemdefault.md) — Default system allocator.
- [kCFAllocatorMallocZone](kcfallocatormalloczone.md) — This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.
- [kCFAllocatorNull](kcfallocatornull.md) — This allocator does nothing—it allocates no memory.
- [kCFAllocatorUseContext](kcfallocatorusecontext.md) — Special allocator argument to [CFAllocatorCreate](<cfallocatorcreate(____).md>)—it uses the functions given in the context to allocate the allocator.
