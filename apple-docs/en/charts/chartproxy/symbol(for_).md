---
title: 'symbol(for:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartproxy/symbol(for:)'
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/symbol(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/symbol%28for%3A%29.json'
content_hash: 'sha256:0d98ec1ed74ad450'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# symbol(for:)

<sub>Instance Method</sub>

Returns the symbol for the given data value. Returns `nil` if the symbol scale is unavailable, or the value is invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func symbol<P>(for value: P) -> AnyChartSymbolShape? where P : Plottable
```

## Parameters

- `value` — The data value.

## Return Value

The symbol corresponding to the data value, or `nil` if the data value is incompatible with the chart.
