---
title: 'compositingLayer(style:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/compositinglayer(style:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/compositinglayer(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/compositinglayer%28style%3A%29.json'
content_hash: 'sha256:b6b95686c99bb64f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# compositingLayer(style:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func compositingLayer<V>(style: (PlaceholderContentView<Self>) -> V) -> some ChartContent where V : View

```

## See Also

### Layering chart content

- [compositingLayer()](<compositinglayer().md>)
- [zIndex(_:)](<zindex(__).md>) — Controls the display order of overlapping chart content.
