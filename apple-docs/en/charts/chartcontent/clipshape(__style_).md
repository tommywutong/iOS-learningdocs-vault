---
title: 'clipShape(_:style:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/clipshape(_:style:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/clipshape(_:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/clipshape%28_%3Astyle%3A%29.json'
content_hash: 'sha256:1f5cbb8b2f1192ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# clipShape(_:style:)

<sub>Instance Method</sub>

Sets a clip shape for the chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func clipShape(_ shape: some Shape, style: FillStyle = FillStyle()) -> some ChartContent

```

## Parameters

- `shape` — The clip shape. The shape fills each mark’s frame.

- `style` — The fill to use when rasterizing the shape.

## See Also

### Masking and clipping

- [mask(content:)](<mask(content_).md>) — Masks chart content using the alpha channel of the specified content.
