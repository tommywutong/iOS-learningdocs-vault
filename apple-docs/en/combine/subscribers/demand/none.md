---
title: none
framework: Combine
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscribers/demand/none
source_url: 'https://developer.apple.com/documentation/combine/subscribers/demand/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/demand/none.json'
content_hash: 'sha256:b822d43761213df2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Demand](../demand.md)

# none

<sub>Type Property</sub>

A request for no elements from the publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let none: Subscribers.Demand
```

## Discussion

This is equivalent to `Demand.max(0)`.

## See Also

### Using special demands

- [unlimited](unlimited.md) — A request for as many values as the publisher can produce.
