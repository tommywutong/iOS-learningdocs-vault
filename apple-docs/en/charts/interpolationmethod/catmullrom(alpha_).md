---
title: 'catmullRom(alpha:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/interpolationmethod/catmullrom(alpha:)'
source_url: 'https://developer.apple.com/documentation/charts/interpolationmethod/catmullrom(alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/interpolationmethod/catmullrom%28alpha%3A%29.json'
content_hash: 'sha256:74b8333c72e118b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [InterpolationMethod](../interpolationmethod.md)

# catmullRom(alpha:)

<sub>Type Method</sub>

Interpolate data points with Catmull-Rom spline, using the given alpha parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func catmullRom(alpha: CGFloat) -> InterpolationMethod
```

## Parameters

- `alpha` — A parameter for the Catmull-Rom spline. Use 0 for a uniform spline, 0.5 for the centripetal spline, and 1.0 for the chordal spline.
