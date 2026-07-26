---
title: 'value(at:as:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/value(at:as:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/value(at:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/value%28at%3Aas%3A%29.json'
content_hash: 'sha256:9aab4b34f784433f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# value(at:as:)

<sub>Instance Method</sub>

Returns the data values at the given position, or `nil` if the position does not correspond to a valid Y value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value<X, Y>(at position: CGPoint, as: (X, Y).Type = (X, Y).self) -> (X, Y)? where X : Plottable, Y : Plottable
```

## Parameters

- `position` — The position at which to obtain the data values. It should be relative to the plot.

## Return Value

A tuple of the x and y data values at the given position.
