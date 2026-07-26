---
title: 'position(forY:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/position(fory:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/position(fory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/position%28fory%3A%29.json'
content_hash: 'sha256:d7849c33d4a96588'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# position(forY:)

<sub>Instance Method</sub>

Returns the y position for the given data value, or `nil` if the y scale is unavailable or if the data value is invalid. The returned position is relative to the plot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func position<P>(forY value: P) -> CGFloat? where P : Plottable
```

## Parameters

- `value` — A data value.

## Return Value

The position corresponding to the data value.
