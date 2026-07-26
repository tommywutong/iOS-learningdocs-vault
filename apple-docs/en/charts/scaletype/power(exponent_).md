---
title: 'power(exponent:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/scaletype/power(exponent:)'
source_url: 'https://developer.apple.com/documentation/charts/scaletype/power(exponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/scaletype/power%28exponent%3A%29.json'
content_hash: 'sha256:4e2514cd00dd0dc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ScaleType](../scaletype.md)

# power(exponent:)

<sub>Type Method</sub>

A number scale where each range value y can be expressed as a power function of the domain value x, with `y = a * pow(x, exponent) + b`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func power(exponent: Double) -> ScaleType
```

## Parameters

- `exponent` — The exponent of the power function.
