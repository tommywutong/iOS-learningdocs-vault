---
title: NSCollectorDisabledOption
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscollectordisabledoption
source_url: 'https://developer.apple.com/documentation/foundation/nscollectordisabledoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscollectordisabledoption.json'
content_hash: 'sha256:cdbf6f833796e45f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCollectorDisabledOption

<sub>Global Variable</sub>

Specifies that the block is retained, and therefore ineligible for collection. Specifying this option is equivalent to invoking [disableCollectorForPointer:](nsgarbagecollector/disablecollectorforpointer_.md) with the returned block as the argument.

<sub>macOS</sub>

```swift
var NSCollectorDisabledOption: Int { get }
```

## See Also

### Constants

- [NSScannedOption](nsscannedoption.md) — Specifies allocation of scanned memory.
