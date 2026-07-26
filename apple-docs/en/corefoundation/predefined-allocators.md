---
title: Predefined Allocators
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/predefined-allocators
source_url: 'https://developer.apple.com/documentation/corefoundation/predefined-allocators'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/predefined-allocators.json'
content_hash: 'sha256:43b3979993830715'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFAllocator](cfallocator.md)

# Predefined Allocators

<sub>API Collection</sub>

CFAllocator provides the following predefined allocators. In general, you should use `kCFAllocatorDefault` unless one of the special circumstances exist below.

## Topics

### Constants

- [kCFAllocatorDefault](kcfallocatordefault.md) — This is a synonym for `NULL`.
- [kCFAllocatorSystemDefault](kcfallocatorsystemdefault.md) — Default system allocator.
- [kCFAllocatorMalloc](kcfallocatormalloc.md) — This allocator uses `malloc()`, `realloc()`, and `free()`.
- [kCFAllocatorMallocZone](kcfallocatormalloczone.md) — This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.
- [kCFAllocatorNull](kcfallocatornull.md) — This allocator does nothing—it allocates no memory.
- [kCFAllocatorUseContext](kcfallocatorusecontext.md) — Special allocator argument to [CFAllocatorCreate](<cfallocatorcreate(____).md>)—it uses the functions given in the context to allocate the allocator.
