---
title: kCFAllocatorDefault
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfallocatordefault
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfallocatordefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfallocatordefault.json'
content_hash: 'sha256:3c4e404f84da3def'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFAllocatorDefault

<sub>Global Variable</sub>

This is a synonym for `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFAllocatorDefault: CFAllocator!
```

## See Also

### Constants

- [kCFAllocatorSystemDefault](kcfallocatorsystemdefault.md) — Default system allocator.
- [kCFAllocatorMalloc](kcfallocatormalloc.md) — This allocator uses `malloc()`, `realloc()`, and `free()`.
- [kCFAllocatorMallocZone](kcfallocatormalloczone.md) — This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.
- [kCFAllocatorNull](kcfallocatornull.md) — This allocator does nothing—it allocates no memory.
- [kCFAllocatorUseContext](kcfallocatorusecontext.md) — Special allocator argument to [CFAllocatorCreate](<cfallocatorcreate(____).md>)—it uses the functions given in the context to allocate the allocator.
