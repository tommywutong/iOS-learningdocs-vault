---
title: kCFAllocatorMallocZone
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfallocatormalloczone
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfallocatormalloczone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfallocatormalloczone.json'
content_hash: 'sha256:c630394ffacd10da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFAllocatorMallocZone

<sub>Global Variable</sub>

This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFAllocatorMallocZone: CFAllocator!
```

## Discussion

You should only use this when an object is safe to be allocated in non-scanned memory.

## See Also

### Constants

- [kCFAllocatorDefault](kcfallocatordefault.md) — This is a synonym for `NULL`.
- [kCFAllocatorSystemDefault](kcfallocatorsystemdefault.md) — Default system allocator.
- [kCFAllocatorMalloc](kcfallocatormalloc.md) — This allocator uses `malloc()`, `realloc()`, and `free()`.
- [kCFAllocatorNull](kcfallocatornull.md) — This allocator does nothing—it allocates no memory.
- [kCFAllocatorUseContext](kcfallocatorusecontext.md) — Special allocator argument to [CFAllocatorCreate](<cfallocatorcreate(____).md>)—it uses the functions given in the context to allocate the allocator.
