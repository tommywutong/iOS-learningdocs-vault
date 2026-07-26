---
title: kCFAllocatorSystemDefault
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfallocatorsystemdefault
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfallocatorsystemdefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfallocatorsystemdefault.json'
content_hash: 'sha256:a93f97544ea9c647'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFAllocatorSystemDefault

<sub>Global Variable</sub>

Default system allocator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFAllocatorSystemDefault: CFAllocator!
```

## Discussion

You rarely need to use this.

## See Also

### Constants

- [kCFAllocatorDefault](kcfallocatordefault.md) — This is a synonym for `NULL`.
- [kCFAllocatorMalloc](kcfallocatormalloc.md) — This allocator uses `malloc()`, `realloc()`, and `free()`.
- [kCFAllocatorMallocZone](kcfallocatormalloczone.md) — This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.
- [kCFAllocatorNull](kcfallocatornull.md) — This allocator does nothing—it allocates no memory.
- [kCFAllocatorUseContext](kcfallocatorusecontext.md) — Special allocator argument to [CFAllocatorCreate](<cfallocatorcreate(____).md>)—it uses the functions given in the context to allocate the allocator.
