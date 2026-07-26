---
title: 'zIndex(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/zindex(_:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/zindex(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/zindex%28_%3A%29.json'
content_hash: 'sha256:bc92dd4c2f80eccb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# zIndex(_:)

<sub>Instance Method</sub>

Controls the display order of overlapping chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func zIndex(_ value: Double) -> some ChartContent

```

## Parameters

- `value` — A relative front-to-back ordering for this view; the default is `0`.

## See Also

### Layering chart content

- [compositingLayer()](<compositinglayer().md>)
- [compositingLayer(style:)](<compositinglayer(style_).md>)
