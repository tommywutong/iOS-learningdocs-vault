---
title: 'alignsMarkStylesWithPlotArea(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/alignsmarkstyleswithplotarea(_:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/alignsmarkstyleswithplotarea(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/alignsmarkstyleswithplotarea%28_%3A%29.json'
content_hash: 'sha256:263c09ac9b60754a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# alignsMarkStylesWithPlotArea(_:)

<sub>Instance Method</sub>

Aligns this item’s styles with the chart’s plot area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func alignsMarkStylesWithPlotArea(_ aligns: Bool = true) -> some ChartContent

```

## Parameters

- `aligns` — A Boolean value that indicates whether to align this item’s styles with the plotting area.

## Discussion

Marks map unit-point coordinates within the plot area’s bounds.

## See Also

### Positioning marks

- [offset(_:)](<offset(__).md>) — Applies an offset that you specify as a size to the chart content.
- [offset(x:y:)](<offset(x_y_).md>) — Applies a vertical and horizontal offset to the chart content.
- [offset(x:yStart:yEnd:)](<offset(x_ystart_yend_).md>) — Applies an offset to the chart content.
- [offset(xStart:xEnd:y:)](<offset(xstart_xend_y_).md>) — Applies an offset to the chart content.
- [offset(xStart:xEnd:yStart:yEnd:)](<offset(xstart_xend_ystart_yend_).md>) — Applies an offset to the chart content.
