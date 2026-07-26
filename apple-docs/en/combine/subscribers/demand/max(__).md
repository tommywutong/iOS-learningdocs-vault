---
title: 'max(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscribers/demand/max(_:)'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/demand/max(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/demand/max%28_%3A%29.json'
content_hash: 'sha256:fa206e7a9aebca8a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Demand](../demand.md)

# max(_:)

<sub>Type Method</sub>

Creates a demand for the given maximum number of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func max(_ value: Int) -> Subscribers.Demand
```

## Parameters

- `value` — The maximum number of elements. Providing a negative value for this parameter results in a fatal error.

## Discussion

The publisher is free to send fewer than the requested maximum number of elements.
