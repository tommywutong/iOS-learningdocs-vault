---
title: name
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterset/name
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterset/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterset/name.json'
content_hash: 'sha256:c9193948b68cd9f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSet](../mtlcounterset.md)

# name

<sub>Instance Property</sub>

The name of the GPU’s counter set instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var name: String { get }
```

## Discussion

The property typically matches one of the common counter set names that [MTLCommonCounterSet](../mtlcommoncounterset.md) defines (see [Confirming which counters and counter sets a GPU supports](../confirming-which-counters-and-counter-sets-a-gpu-supports.md)).
