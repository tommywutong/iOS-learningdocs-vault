---
title: 'symbol(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/symbol(_:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/symbol(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/symbol%28_%3A%29.json'
content_hash: 'sha256:505e1d424596584f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# symbol(_:)

<sub>Instance Method</sub>

Sets a plotting symbol type for the chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func symbol<S>(_ symbol: S) -> some ChartContent where S : ChartSymbolShape

```

## Parameters

- `symbol` — The symbol.

## See Also

### Setting symbol appearance

- [symbol(symbol:)](<symbol(symbol_).md>) — Sets a SwiftUI view to use as the symbol for the chart content.
- [symbolSize(_:)](<symbolsize(__)-7s0vk.md>) — Sets the plotting symbol size for the chart content.
- [symbolSize(_:)](<symbolsize(__)-8dtyt.md>) — Sets the plotting symbol size for the chart content according to a perceived area.
