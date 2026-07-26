---
title: paperRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintpagerenderer/paperrect
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/paperrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/paperrect.json'
content_hash: 'sha256:796807c411addf5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# paperRect

<sub>Instance Property</sub>

The size of the paper for printing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var paperRect: CGRect { get }
```

## Discussion

The value of this property is a rectangle that defines the size of paper chosen for the print job. The origin is always (0,0).

## See Also

### Related Documentation

- [printPaper](../uiprintinteractioncontroller/printpaper.md) — An object that represents the paper size and printing area for the print job.

### Accessing information about the print job

- [numberOfPages](numberofpages.md) — The number of pages to render.
- [printableRect](printablerect.md) — The area in which printing can occur.
