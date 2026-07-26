---
title: NSMapTableWeakMemory
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptableweakmemory
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptableweakmemory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptableweakmemory.json'
content_hash: 'sha256:1d86a83ed1cddfed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapTableWeakMemory

<sub>Global Variable</sub>

Equivalent to [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSMapTableWeakMemory: NSPointerFunctions.Options { get }
```

## See Also

### Memory Options

- [NSPointerFunctionsMachVirtualMemory](nspointerfunctions/options/machvirtualmemory.md) — Use Mach memory.
- [NSPointerFunctionsMallocMemory](nspointerfunctions/options/mallocmemory.md) — Use `free()` on removal, `calloc()` on copy in.
- [NSPointerFunctionsOpaqueMemory](nspointerfunctions/options/opaquememory.md) — Take no action when pointers are deleted.
- [NSPointerFunctionsStrongMemory](nspointerfunctions/options/strongmemory.md) — Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md) — Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [NSMapTableStrongMemory](nsmaptablestrongmemory.md) — Equivalent to [NSPointerFunctionsStrongMemory](nspointerfunctions/options/strongmemory.md).
