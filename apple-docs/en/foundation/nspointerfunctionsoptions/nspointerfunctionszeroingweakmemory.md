---
title: NSPointerFunctionsZeroingWeakMemory
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [macOS 10.5+（10.8 起废弃）]
languages: [occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.json'
content_hash: 'sha256:b36390a113044ad7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Options](../nspointerfunctions/options.md)

# NSPointerFunctionsZeroingWeakMemory

<sub>Enumeration Case</sub>

Use weak read and write barriers; use garbage-collected memory on copyIn.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSPointerFunctionsZeroingWeakMemory
```

## Discussion

If you do not use garbage collection, for object personalities, it will hold a non-retained object pointer.

## See Also

### Memory Options

- [NSPointerFunctionsMachVirtualMemory](../nspointerfunctions/options/machvirtualmemory.md) — Use Mach memory.
- [NSPointerFunctionsMallocMemory](../nspointerfunctions/options/mallocmemory.md) — Use `free()` on removal, `calloc()` on copy in.
- [NSPointerFunctionsOpaqueMemory](../nspointerfunctions/options/opaquememory.md) — Take no action when pointers are deleted.
- [NSPointerFunctionsStrongMemory](../nspointerfunctions/options/strongmemory.md) — Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [NSPointerFunctionsWeakMemory](../nspointerfunctions/options/weakmemory.md) — Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [NSMapTableStrongMemory](../nsmaptablestrongmemory.md) — Equivalent to [NSPointerFunctionsStrongMemory](../nspointerfunctions/options/strongmemory.md).
- [NSMapTableWeakMemory](../nsmaptableweakmemory.md) — Equivalent to [NSPointerFunctionsWeakMemory](../nspointerfunctions/options/weakmemory.md).
- [NSMapTableZeroingWeakMemory](../nsmaptablezeroingweakmemory.md) — Equivalent to [NSPointerFunctionsZeroingWeakMemory](nspointerfunctionszeroingweakmemory.md). _(deprecated)_
