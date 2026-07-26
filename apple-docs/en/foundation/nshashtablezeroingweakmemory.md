---
title: NSHashTableZeroingWeakMemory
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.5+（10.8 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nshashtablezeroingweakmemory
source_url: 'https://developer.apple.com/documentation/foundation/nshashtablezeroingweakmemory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtablezeroingweakmemory.json'
content_hash: 'sha256:e08f28334d4c3da0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHashTableZeroingWeakMemory

<sub>Global Variable</sub>

This option has been deprecated. Instead use the `NSHashTableWeakMemory` option. Equal to [NSPointerFunctionsZeroingWeakMemory](nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static const NSPointerFunctionsOptions NSHashTableZeroingWeakMemory;
```

## Discussion

Note that `NSHashTableWeakMemory` is not entirely equivalent to and compatible with the previous option’s behavior: objects must be weak-reference-safe under manual and automatic reference counting; not all objects are.

## See Also

### Constants

- [NSHashTableStrongMemory](nshashtablestrongmemory.md) — Equal to [NSPointerFunctionsStrongMemory](nspointerfunctions/options/strongmemory.md).
- [NSHashTableCopyIn](nshashtablecopyin.md) — Equal to [NSPointerFunctionsCopyIn](nspointerfunctions/options/copyin.md).
- [NSHashTableObjectPointerPersonality](nshashtableobjectpointerpersonality.md) — Equal to [NSPointerFunctionsObjectPointerPersonality](nspointerfunctions/options/objectpointerpersonality.md).
- [NSHashTableWeakMemory](nshashtableweakmemory.md) — Equal to [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md). Uses weak read and write barriers appropriate for ARC or GC. Using [NSPointerFunctionsWeakMemory](nspointerfunctions/options/weakmemory.md) object references will turn to `NULL` on last release.
