---
title: 'cardinal(tension:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/interpolationmethod/cardinal(tension:)'
source_url: 'https://developer.apple.com/documentation/charts/interpolationmethod/cardinal(tension:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/interpolationmethod/cardinal%28tension%3A%29.json'
content_hash: 'sha256:4e3a9ee4b01b93c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [InterpolationMethod](../interpolationmethod.md)

# cardinal(tension:)

<sub>Type Method</sub>

Interpolate data points with cardinal spline, using the given tension parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func cardinal(tension: CGFloat) -> InterpolationMethod
```

## Parameters

- `tension` — A parameter that controls the length of tangents in the cardinal spline.
