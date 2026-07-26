---
title: 'foregroundStyle(for:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/foregroundstyle(for:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/foregroundstyle(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/foregroundstyle%28for%3A%29.json'
content_hash: 'sha256:1de1d56b7c85712c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# foregroundStyle(for:)

<sub>Instance Method</sub>

Returns the foreground style for the given data value. Returns `nil` if the foreground style scale is unavailable, or the value is invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func foregroundStyle<P>(for value: P) -> AnyShapeStyle? where P : Plottable
```

## Parameters

- `value` — The data value.

## Return Value

The foreground style corresponding to the data value, or `nil` if the data value is incompatible with the chart.
