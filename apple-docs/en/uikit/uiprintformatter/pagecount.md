---
title: pageCount
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintformatter/pagecount
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/pagecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/pagecount.json'
content_hash: 'sha256:407c9e63536a617b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# pageCount

<sub>Instance Property</sub>

The number of pages to print.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var pageCount: Int { get }
```

## Discussion

`UIPrintFormatter` calculates this value based on the layout metrics and content.

## See Also

### Managing pagination

- [startPage](startpage.md) — The index of the first page that the print formatter lays out.
