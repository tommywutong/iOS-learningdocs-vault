---
title: kCFAllocatorUseContext
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfallocatorusecontext
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfallocatorusecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfallocatorusecontext.json'
content_hash: 'sha256:16a3dd7917e9c85c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFAllocatorUseContext

<sub>Global Variable</sub>

Special allocator argument to [CFAllocatorCreate](<cfallocatorcreate(____).md>)—it uses the functions given in the context to allocate the allocator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFAllocatorUseContext: CFAllocator!
```

## See Also

### Constants

- [kCFAllocatorDefault](kcfallocatordefault.md) — This is a synonym for `NULL`.
- [kCFAllocatorSystemDefault](kcfallocatorsystemdefault.md) — Default system allocator.
- [kCFAllocatorMalloc](kcfallocatormalloc.md) — This allocator uses `malloc()`, `realloc()`, and `free()`.
- [kCFAllocatorMallocZone](kcfallocatormalloczone.md) — This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.
- [kCFAllocatorNull](kcfallocatornull.md) — This allocator does nothing—it allocates no memory.
