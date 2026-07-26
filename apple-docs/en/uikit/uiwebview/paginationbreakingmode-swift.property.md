---
title: paginationBreakingMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（12.0 起废弃）, iPadOS 7.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/paginationbreakingmode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/paginationbreakingmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/paginationbreakingmode-swift.property.json'
content_hash: 'sha256:29c7af5b2bdfff08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# paginationBreakingMode

<sub>Instance Property</sub>

The manner in which column- or page-breaking occurs.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var paginationBreakingMode: UIWebView.PaginationBreakingMode { get set }
```

## Discussion

This property determines whether certain CSS properties regarding column- and page-breaking are honored or ignored. When this property is set to [UIWebPaginationBreakingModeColumn](paginationbreakingmode-swift.enum/column.md), the content respects the CSS properties related to column-breaking in place of page-breaking.

See [PaginationBreakingMode](paginationbreakingmode-swift.enum.md) for possible values. The default value is [UIWebPaginationBreakingModePage](paginationbreakingmode-swift.enum/page.md).

## See Also

### Managing pages

- [gapBetweenPages](gapbetweenpages.md) — The size of the gap, in points, between pages. _(deprecated)_
- [pageCount](pagecount.md) — The number of pages produced by the layout of the web view. _(deprecated)_
- [pageLength](pagelength.md) — The size of each page, in points, in the direction that the pages flow. _(deprecated)_
- [paginationMode](paginationmode-swift.property.md) — The layout of content in the web view. _(deprecated)_
