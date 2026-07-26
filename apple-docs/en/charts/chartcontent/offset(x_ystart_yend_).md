---
title: 'offset(x:yStart:yEnd:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/offset(x:ystart:yend:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/offset(x:ystart:yend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/offset%28x%3Aystart%3Ayend%3A%29.json'
content_hash: 'sha256:44cc2616b82e4495'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# offset(x:yStart:yEnd:)

<sub>Instance Method</sub>

Applies an offset to the chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func offset(x: CGFloat = 0, yStart: CGFloat = 0, yEnd: CGFloat = 0) -> some ChartContent

```

## Parameters

- `x` — The horizontal offset in screen coordinates.

- `yStart` — The starting vertical offset in screen coordinates.

- `yEnd` — The ending vertical offset in screen coordinates.

## Discussion

The `yStart` and `yEnd` offset values apply only to marks that have such properties, like bar marks and line segment marks.

## See Also

### Positioning marks

- [offset(_:)](<offset(__).md>) — Applies an offset that you specify as a size to the chart content.
- [offset(x:y:)](<offset(x_y_).md>) — Applies a vertical and horizontal offset to the chart content.
- [offset(xStart:xEnd:y:)](<offset(xstart_xend_y_).md>) — Applies an offset to the chart content.
- [offset(xStart:xEnd:yStart:yEnd:)](<offset(xstart_xend_ystart_yend_).md>) — Applies an offset to the chart content.
- [alignsMarkStylesWithPlotArea(_:)](<alignsmarkstyleswithplotarea(__).md>) — Aligns this item’s styles with the chart’s plot area.
