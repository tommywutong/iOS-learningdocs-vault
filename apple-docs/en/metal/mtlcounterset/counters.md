---
title: counters
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterset/counters
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterset/counters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterset/counters.json'
content_hash: 'sha256:a68ab8d2a82b9642'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSet](../mtlcounterset.md)

# counters

<sub>Instance Property</sub>

An array of the counter instances a GPU device supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var counters: [any MTLCounter] { get }
```

## Discussion

Check whether a GPU device supports a specific counter by comparing its common name (see [MTLCommonCounter](../mtlcommoncounter.md)) with each element in the property’s array.

> [!important] Important
> Some GPUs may only support some of the counters within a counter set.

For more information, see [Confirming which counters and counter sets a GPU supports](../confirming-which-counters-and-counter-sets-a-gpu-supports.md).
