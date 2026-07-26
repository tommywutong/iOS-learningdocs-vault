---
title: NSHashTableStrongMemory
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtablestrongmemory
source_url: 'https://developer.apple.com/documentation/foundation/nshashtablestrongmemory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtablestrongmemory.json'
content_hash: 'sha256:474958f7c2ce897b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHashTableStrongMemory

<sub>Global Variable</sub>

Equal to [NSPointerFunctionsStrongMemory](nspointerfunctions/options/strongmemory.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSHashTableStrongMemory: NSPointerFunctions.Options { get }
```

## See Also

### Constants

- [NSHashTableCopyIn](nshashtablecopyin.md) — Equal to [NSPointerFunctionsCopyIn](nspointerfunctions/options/copyin.md).
- [NSHashTableObjectPointerPersonality](nshashtableobjectpointerpersonality.md) — Equal to [NSPointerFunctionsObjectPointerPersonality](nspointerfunctions/options/objectpointerpersonality.md).
- [NSHashTableWeakMemory](nshashtableweakmemory.md) — Equal to [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md). Uses weak read and write barriers appropriate for ARC or GC. Using [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md) object references will turn to `NULL` on last release.
