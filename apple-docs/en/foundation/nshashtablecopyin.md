---
title: NSHashTableCopyIn
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtablecopyin
source_url: 'https://developer.apple.com/documentation/foundation/nshashtablecopyin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtablecopyin.json'
content_hash: 'sha256:1e8a3b83dd5fb412'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHashTableCopyIn

<sub>Global Variable</sub>

Equal to [NSPointerFunctionsCopyIn](nspointerfunctions/options/copyin.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSHashTableCopyIn: NSPointerFunctions.Options { get }
```

## See Also

### Constants

- [NSHashTableStrongMemory](nshashtablestrongmemory.md) — Equal to [NSPointerFunctionsStrongMemory](nspointerfunctions/options/strongmemory.md).
- [NSHashTableObjectPointerPersonality](nshashtableobjectpointerpersonality.md) — Equal to [NSPointerFunctionsObjectPointerPersonality](nspointerfunctions/options/objectpointerpersonality.md).
- [NSHashTableWeakMemory](nshashtableweakmemory.md) — Equal to [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md). Uses weak read and write barriers appropriate for ARC or GC. Using [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md) object references will turn to `NULL` on last release.
