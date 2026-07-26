---
title: paginationMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（12.0 起废弃）, iPadOS 7.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/paginationmode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/paginationmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/paginationmode-swift.property.json'
content_hash: 'sha256:3ecba54a9456105e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# paginationMode

<sub>Instance Property</sub>

The layout of content in the web view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var paginationMode: UIWebView.PaginationMode { get set }
```

## Discussion

This property determines whether content in the web view is broken up into pages that fill the view one screen at a time, or shown as one long scrolling view. If set to a paginated form, this property toggles a paginated layout on the content, causing the web view to use the values of [pageLength](pagelength.md) and [gapBetweenPages](gapbetweenpages.md) to relayout its content.

See [PaginationMode](paginationmode-swift.enum.md) for possible values. The default value is [UIWebPaginationModeUnpaginated](paginationmode-swift.enum/unpaginated.md).

## See Also

### Managing pages

- [gapBetweenPages](gapbetweenpages.md) — The size of the gap, in points, between pages. _(deprecated)_
- [pageCount](pagecount.md) — The number of pages produced by the layout of the web view. _(deprecated)_
- [pageLength](pagelength.md) — The size of each page, in points, in the direction that the pages flow. _(deprecated)_
- [paginationBreakingMode](paginationbreakingmode-swift.property.md) — The manner in which column- or page-breaking occurs. _(deprecated)_
