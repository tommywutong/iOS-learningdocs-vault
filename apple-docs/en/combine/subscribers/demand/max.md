---
title: max
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscribers/demand/max
source_url: 'https://developer.apple.com/documentation/combine/subscribers/demand/max'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/demand/max.json'
content_hash: 'sha256:f1dcd46361395610'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Demand](../demand.md)

# max

<sub>Instance Property</sub>

The number of requested values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var max: Int? { get }
```

## Discussion

The value is `nil` if the demand is [unlimited](unlimited.md).
