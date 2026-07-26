---
title: 'angle(at:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/angle(at:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/angle(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/angle%28at%3A%29.json'
content_hash: 'sha256:f3b4b17f3a24d62b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# angle(at:)

<sub>Instance Method</sub>

Returns the angle relative to the plot area center, where the 12 o’clock position is interpreted as zero degrees, increasing clockwise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func angle(at position: CGPoint) -> Angle
```

## Parameters

- `position` — The position at which to obtain the data value. It should be relative to the plot.

## Return Value

The angle relative to the plot area center.
