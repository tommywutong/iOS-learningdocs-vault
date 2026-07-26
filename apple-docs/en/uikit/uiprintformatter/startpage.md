---
title: startPage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintformatter/startpage
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/startpage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/startpage.json'
content_hash: 'sha256:8f3fc8a1c7d71092'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# startPage

<sub>Instance Property</sub>

The index of the first page that the print formatter lays out.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var startPage: Int { get set }
```

## Discussion

The value is a zero-based index. You can set the starting page of a print formatter by assigning an index to this property or by passing one as the second argument of the [- addPrintFormatter:startingAtPageAtIndex:](<../uiprintpagerenderer/addprintformatter(__startingatpageat_).md>) method of [UIPrintPageRenderer](../uiprintpagerenderer.md).

## See Also

### Managing pagination

- [pageCount](pagecount.md) — The number of pages to print.
