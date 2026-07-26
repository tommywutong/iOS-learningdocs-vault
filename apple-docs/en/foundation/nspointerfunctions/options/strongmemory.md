---
title: strongMemory
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/options/strongmemory
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/options/strongmemory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/options/strongmemory.json'
content_hash: 'sha256:a37950b6dfa95291'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSPointerFunctions](../../nspointerfunctions.md) · [Options](../options.md)

# strongMemory

<sub>Type Property</sub>

Use strong write-barriers to backing store; use garbage-collected memory on copy-in.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var strongMemory: NSPointerFunctions.Options { get }
```

## Discussion

This is the default memory value.

As a special case, if you do not use garbage collection and specify this value in conjunction with [NSPointerFunctionsObjectPersonality](objectpersonality.md) or [NSPointerFunctionsObjectPointerPersonality](objectpointerpersonality.md) then the `NSPointerFunctions` object uses `retain` and `release`.

If you do not use garbage collection, and specify this value in conjunction with a valid non-object personality, it is the same as specifying [NSPointerFunctionsMallocMemory](mallocmemory.md).

## See Also

### Memory Options

- [NSPointerFunctionsMachVirtualMemory](machvirtualmemory.md) — Use Mach memory.
- [NSPointerFunctionsMallocMemory](mallocmemory.md) — Use `free()` on removal, `calloc()` on copy in.
- [NSPointerFunctionsOpaqueMemory](opaquememory.md) — Take no action when pointers are deleted.
- [NSPointerFunctionsWeakMemory](weakmemory.md) — Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [NSMapTableStrongMemory](../../nsmaptablestrongmemory.md) — Equivalent to [NSPointerFunctionsStrongMemory](strongmemory.md).
- [NSMapTableWeakMemory](../../nsmaptableweakmemory.md) — Equivalent to [NSPointerFunctionsWeakMemory](weakmemory.md).
