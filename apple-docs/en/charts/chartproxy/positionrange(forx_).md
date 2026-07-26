---
title: 'positionRange(forX:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/positionrange(forx:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/positionrange(forx:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/positionrange%28forx%3A%29.json'
content_hash: 'sha256:41972a49817a608a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# positionRange(forX:)

<sub>Instance Method</sub>

Returns the range of x position for the given data value, or `nil` if the x scale is unavailable or if the value is invalid. The returned position range is relative to the plot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func positionRange<P>(forX value: P) -> ClosedRange<CGFloat>? where P : Plottable
```

## Parameters

- `value` — The data value.

## Return Value

The position range corresponding to the data value.

## Discussion

For a continuous data value, the returned range is a single point. For a categorical data value, the returned range is the range of positions that correspond to the given category.
