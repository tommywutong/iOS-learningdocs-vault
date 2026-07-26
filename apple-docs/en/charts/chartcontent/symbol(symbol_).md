---
title: 'symbol(symbol:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/symbol(symbol:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/symbol(symbol:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/symbol%28symbol%3A%29.json'
content_hash: 'sha256:7f308591963f49bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# symbol(symbol:)

<sub>Instance Method</sub>

Sets a SwiftUI view to use as the symbol for the chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func symbol<V>(@ViewBuilder symbol: () -> V) -> some ChartContent where V : View

```

## Parameters

- `symbol` — The view to use as the plotting symbol.

## See Also

### Setting symbol appearance

- [symbol(_:)](<symbol(__).md>) — Sets a plotting symbol type for the chart content.
- [symbolSize(_:)](<symbolsize(__)-7s0vk.md>) — Sets the plotting symbol size for the chart content.
- [symbolSize(_:)](<symbolsize(__)-8dtyt.md>) — Sets the plotting symbol size for the chart content according to a perceived area.
