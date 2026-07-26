---
title: numberOfPages
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintpagerenderer/numberofpages
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/numberofpages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/numberofpages.json'
content_hash: 'sha256:a6e77094d7be1a40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# numberOfPages

<sub>Instance Property</sub>

The number of pages to render.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var numberOfPages: Int { get }
```

## Discussion

By default, returns the number of pages as calculated by UIKit if the receiver uses print formatters. If the page renderer uses no print formatters, the returned value is zero. If your page renderer is doing any custom drawing except for headers and footers, it must override this method.

This method is called at any point when UIKit needs the number of pages. If an application requests the page range control, it’s called early on. It can also be called when the selected printer or duplex mode changes. Otherwise, it is called when the print job starts.

If print formatters aren’t used to compute the page count, the page renderer can override this method to calculate and return the number of pages. The computation can take into account the current [printableRect](printablerect.md) value for each page, any implicit margins, and the content to be drawn when laid out within these boundaries.

## See Also

### Related Documentation

- [pageCount](../uiprintformatter/pagecount.md) — The number of pages to print.

### Accessing information about the print job

- [paperRect](paperrect.md) — The size of the paper for printing.
- [printableRect](printablerect.md) — The area in which printing can occur.
