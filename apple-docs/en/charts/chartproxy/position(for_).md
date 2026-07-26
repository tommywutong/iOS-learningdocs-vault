---
title: 'position(for:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/position(for:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/position(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/position%28for%3A%29.json'
content_hash: 'sha256:1f07a44bb2a4242d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# position(for:)

<sub>Instance Method</sub>

Returns the x and y positions as a `CGPoint` for the given data values, or `nil` if either the X or the y scale is unavailable or if any data value is invalid. The returned position is relative to the plot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func position<X, Y>(for point: (x: X, y: Y)) -> CGPoint? where X : Plottable, Y : Plottable
```

## Parameters

- `point` — A tuple of x and y data values.

## Return Value

The position corresponding to the data values.
