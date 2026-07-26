---
title: NSHashTableObjectPointerPersonality
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtableobjectpointerpersonality
source_url: 'https://developer.apple.com/documentation/foundation/nshashtableobjectpointerpersonality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtableobjectpointerpersonality.json'
content_hash: 'sha256:9482333ddfd3d913'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHashTableObjectPointerPersonality

<sub>Global Variable</sub>

Equal to [NSPointerFunctionsObjectPointerPersonality](nspointerfunctions/options/objectpointerpersonality.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSHashTableObjectPointerPersonality: NSPointerFunctions.Options { get }
```

## See Also

### Constants

- [NSHashTableStrongMemory](nshashtablestrongmemory.md) — Equal to [NSPointerFunctionsStrongMemory](nspointerfunctions/options/strongmemory.md).
- [NSHashTableCopyIn](nshashtablecopyin.md) — Equal to [NSPointerFunctionsCopyIn](nspointerfunctions/options/copyin.md).
- [NSHashTableWeakMemory](nshashtableweakmemory.md) — Equal to [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md). Uses weak read and write barriers appropriate for ARC or GC. Using [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md) object references will turn to `NULL` on last release.
