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
doc_path: /documentation/metal/mtlcounter/name
source_url: 'https://developer.apple.com/documentation/metal/mtlcounter/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounter/name.json'
content_hash: 'sha256:d658c49d582e1eac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounter](../mtlcounter.md)

# name

<sub>Instance Property</sub>

The name of a GPU’s counter instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var name: String { get }
```

## Discussion

The property typically matches one of the common counter names that [MTLCommonCounter](../mtlcommoncounter.md) defines (see [Confirming which counters and counter sets a GPU supports](../confirming-which-counters-and-counter-sets-a-gpu-supports.md)).
