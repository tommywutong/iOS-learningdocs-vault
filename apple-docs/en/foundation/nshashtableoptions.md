---
title: NSHashTableOptions
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtableoptions
source_url: 'https://developer.apple.com/documentation/foundation/nshashtableoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtableoptions.json'
content_hash: 'sha256:ed90b752b07c03e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHashTableOptions

<sub>Type Alias</sub>

Components in a bit-field to specify the behavior of elements in an [NSHashTable](nshashtable.md) object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias NSHashTableOptions = Int
```

## Topics

### Constants

- [NSHashTableStrongMemory](nshashtablestrongmemory.md) — Equal to [NSPointerFunctionsStrongMemory](nspointerfunctions/options/strongmemory.md).
- [NSHashTableCopyIn](nshashtablecopyin.md) — Equal to [NSPointerFunctionsCopyIn](nspointerfunctions/options/copyin.md).
- [NSHashTableObjectPointerPersonality](nshashtableobjectpointerpersonality.md) — Equal to [NSPointerFunctionsObjectPointerPersonality](nspointerfunctions/options/objectpointerpersonality.md).
- [NSHashTableWeakMemory](nshashtableweakmemory.md) — Equal to [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md). Uses weak read and write barriers appropriate for ARC or GC. Using [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md) object references will turn to `NULL` on last release.
