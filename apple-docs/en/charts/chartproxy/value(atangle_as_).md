---
title: 'value(atAngle:as:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/value(atangle:as:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/value(atangle:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/value%28atangle%3Aas%3A%29.json'
content_hash: 'sha256:04cf662fa293c2ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# value(atAngle:as:)

<sub>Instance Method</sub>

Returns the data value at the given angle, or `nil` if the angle does not correspond to a valid data value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value<P>(atAngle angle: Angle, as: P.Type = P.self) -> P? where P : Plottable
```

## Parameters

- `angle` — The angle, relative to the plot center, where the 12 o’clock position is interpreted as zero degrees, increasing clockwise.

## Return Value

The data value at the given position.
