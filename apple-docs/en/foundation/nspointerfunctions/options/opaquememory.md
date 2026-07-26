---
title: opaqueMemory
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/options/opaquememory
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/options/opaquememory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/options/opaquememory.json'
content_hash: 'sha256:0b78b0472b4ca151'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSPointerFunctions](../../nspointerfunctions.md) · [Options](../options.md)

# opaqueMemory

<sub>Type Property</sub>

Take no action when pointers are deleted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var opaqueMemory: NSPointerFunctions.Options { get }
```

## Discussion

This is usually the preferred memory option for holding arbitrary pointers.

This is essentially a no-op relinquish function; the acquire function is only used for copy-in operations.  This option is unlikely a to be a good choice for objects.

## See Also

### Memory Options

- [NSPointerFunctionsMachVirtualMemory](machvirtualmemory.md) — Use Mach memory.
- [NSPointerFunctionsMallocMemory](mallocmemory.md) — Use `free()` on removal, `calloc()` on copy in.
- [NSPointerFunctionsStrongMemory](strongmemory.md) — Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [NSPointerFunctionsWeakMemory](weakmemory.md) — Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [NSMapTableStrongMemory](../../nsmaptablestrongmemory.md) — Equivalent to [NSPointerFunctionsStrongMemory](strongmemory.md).
- [NSMapTableWeakMemory](../../nsmaptableweakmemory.md) — Equivalent to [NSPointerFunctionsWeakMemory](weakmemory.md).
