---
title: NSMapTableZeroingWeakMemory
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.5+（10.8 起废弃）]
languages: [occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmaptablezeroingweakmemory
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptablezeroingweakmemory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptablezeroingweakmemory.json'
content_hash: 'sha256:f2f0729017521ecf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapTableZeroingWeakMemory

<sub>Global Variable</sub>

Equivalent to [NSPointerFunctionsZeroingWeakMemory](nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static const NSPointerFunctionsOptions NSMapTableZeroingWeakMemory;
```

## See Also

### Memory Options

- [NSPointerFunctionsMachVirtualMemory](nspointerfunctions/options/machvirtualmemory.md) — Use Mach memory.
- [NSPointerFunctionsMallocMemory](nspointerfunctions/options/mallocmemory.md) — Use `free()` on removal, `calloc()` on copy in.
- [NSPointerFunctionsOpaqueMemory](nspointerfunctions/options/opaquememory.md) — Take no action when pointers are deleted.
- [NSPointerFunctionsStrongMemory](nspointerfunctions/options/strongmemory.md) — Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md) — Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [NSPointerFunctionsZeroingWeakMemory](nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md) — Use weak read and write barriers; use garbage-collected memory on copyIn. _(deprecated)_
- [NSMapTableStrongMemory](nsmaptablestrongmemory.md) — Equivalent to [NSPointerFunctionsStrongMemory](nspointerfunctions/options/strongmemory.md).
- [NSMapTableWeakMemory](nsmaptableweakmemory.md) — Equivalent to [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md).
