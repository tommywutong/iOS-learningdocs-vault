---
title: 'value(atX:as:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/value(atx:as:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/value(atx:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/value%28atx%3Aas%3A%29.json'
content_hash: 'sha256:302d6fc00e9c766e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# value(atX:as:)

<sub>Instance Method</sub>

Returns the data value at the given x position, or `nil` if the position does not correspond to a valid X value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value<P>(atX position: CGFloat, as: P.Type = P.self) -> P? where P : Plottable
```

## Parameters

- `position` — The position at which to obtain the x data value. It should be relative to the plot.

## Return Value

The data value at the given position.
