---
title: 'position(forX:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/position(forx:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/position(forx:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/position%28forx%3A%29.json'
content_hash: 'sha256:68ab900bb6e77ce4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# position(forX:)

<sub>Instance Method</sub>

Returns the x position for the given data value, or `nil` if the x scale is unavailable or if the data value is invalid. The returned position is relative to the plot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func position<P>(forX value: P) -> CGFloat? where P : Plottable
```

## Parameters

- `value` — A data value.

## Return Value

The position corresponding to the data value.
