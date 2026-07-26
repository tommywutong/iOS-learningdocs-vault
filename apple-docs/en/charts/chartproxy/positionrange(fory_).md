---
title: 'positionRange(forY:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/positionrange(fory:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/positionrange(fory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/positionrange%28fory%3A%29.json'
content_hash: 'sha256:9ddfd421f47eeb6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# positionRange(forY:)

<sub>Instance Method</sub>

Returns the range of y position for the given data value, or `nil` if the x scale is unavailable or if the value is invalid. The returned position range is relative to the plot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func positionRange<P>(forY value: P) -> ClosedRange<CGFloat>? where P : Plottable
```

## Parameters

- `value` — The data value.

## Return Value

The position range corresponding to the data value.

## Discussion

For a continuous data value, the returned range is a single point. For a categorical data value, the returned range is the range of positions that correspond to the given category.
