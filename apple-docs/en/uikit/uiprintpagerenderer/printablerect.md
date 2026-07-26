---
title: printableRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintpagerenderer/printablerect
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/printablerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/printablerect.json'
content_hash: 'sha256:fd473b7759227061'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# printableRect

<sub>Instance Property</sub>

The area in which printing can occur.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printableRect: CGRect { get }
```

## Discussion

The value of this property is a rectangle that defines the area in which the printer can print content. Sometimes this is referred to as the imageable area of the paper.

## See Also

### Related Documentation

- [printPaper](../uiprintinteractioncontroller/printpaper.md) — An object that represents the paper size and printing area for the print job.

### Accessing information about the print job

- [numberOfPages](numberofpages.md) — The number of pages to render.
- [paperRect](paperrect.md) — The size of the paper for printing.
