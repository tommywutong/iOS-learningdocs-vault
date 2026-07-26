---
title: 'value(atY:as:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/value(aty:as:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/value(aty:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/value%28aty%3Aas%3A%29.json'
content_hash: 'sha256:2760c27296f63eb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# value(atY:as:)

<sub>Instance Method</sub>

Returns the data value at the given y position, or `nil` if the position does not correspond to a valid Y value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value<P>(atY position: CGFloat, as: P.Type = P.self) -> P? where P : Plottable
```

## Parameters

- `position` — The position at which to obtain the y data value. It should be relative to the plot.

## Return Value

The data value at the given position.
