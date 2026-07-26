---
title: pageLength
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（12.0 起废弃）, iPadOS 7.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/pagelength
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/pagelength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/pagelength.json'
content_hash: 'sha256:e0c2c636b6c2637d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# pageLength

<sub>Instance Property</sub>

The size of each page, in points, in the direction that the pages flow.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var pageLength: CGFloat { get set }
```

## Discussion

When [paginationMode](paginationmode-swift.property.md) is right to left or left to right, this property represents the width of each page. When [paginationMode](paginationmode-swift.property.md) is top to bottom or bottom to top, this property represents the height of each page.

The default value is `0`, which means the layout uses the size of the viewport to determine the dimensions of the page. Adjusting the value of this property causes a relayout.

## See Also

### Managing pages

- [gapBetweenPages](gapbetweenpages.md) — The size of the gap, in points, between pages. _(deprecated)_
- [pageCount](pagecount.md) — The number of pages produced by the layout of the web view. _(deprecated)_
- [paginationBreakingMode](paginationbreakingmode-swift.property.md) — The manner in which column- or page-breaking occurs. _(deprecated)_
- [paginationMode](paginationmode-swift.property.md) — The layout of content in the web view. _(deprecated)_
