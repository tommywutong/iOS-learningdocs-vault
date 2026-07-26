---
title: 'mask(content:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/mask(content:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/mask(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/mask%28content%3A%29.json'
content_hash: 'sha256:2729d3ef8d5aca90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# mask(content:)

<sub>Instance Method</sub>

Masks chart content using the alpha channel of the specified content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func mask<C>(@ContentBuilder content: () -> C) -> some ChartContent where C : ChartContent

```

## Discussion

Parameter content: The content whose alpha will be applied to this item.

## See Also

### Masking and clipping

- [clipShape(_:style:)](<clipshape(__style_).md>) — Sets a clip shape for the chart content.
