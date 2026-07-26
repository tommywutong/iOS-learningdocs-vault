---
title: 'symmetricLog(slopeAtZero:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/scaletype/symmetriclog(slopeatzero:)'
source_url: 'https://developer.apple.com/documentation/charts/scaletype/symmetriclog(slopeatzero:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/scaletype/symmetriclog%28slopeatzero%3A%29.json'
content_hash: 'sha256:9917645031c9b2fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ScaleType](../scaletype.md)

# symmetricLog(slopeAtZero:)

<sub>Type Method</sub>

A number scale where each range value y can be expressed as a symmetric log function of the domain value x, with `y = a * sign(x) * log(1 + |x * slopeAtZero|) + b`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func symmetricLog(slopeAtZero: Double) -> ScaleType
```

## Parameters

- `slopeAtZero` — A positive constant that controls the slope of the symmetric log function at zero.
