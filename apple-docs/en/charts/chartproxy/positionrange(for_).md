---
title: 'positionRange(for:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/positionrange(for:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/positionrange(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/positionrange%28for%3A%29.json'
content_hash: 'sha256:81acb390f3dead72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# positionRange(for:)

<sub>Instance Method</sub>

Returns the range of x and y positions for the given pair of data values, or `nil` if the y scale is unavailable or if the value is invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func positionRange<X, Y>(for point: (x: X, y: Y)) -> CGRect? where X : Plottable, Y : Plottable
```

## Return Value

The position range corresponding to the data values.

## Discussion

For a continuous data value, the returned range is a single point. For a categorical data value, the returned range is the range of positions that correspond to the given category.
