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
doc_path: /documentation/uikit/uiprintpaper/printablerect
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpaper/printablerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpaper/printablerect.json'
content_hash: 'sha256:425151fdd3c3e877'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPaper](../uiprintpaper.md)

# printableRect

<sub>Instance Property</sub>

The rectangle that represents the portion of the paper that can be imaged upon.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printableRect: CGRect { get }
```

## Discussion

Typically, UIKit passes this value into the last argument of the [UIPrintPageRenderer](../uiprintpagerenderer.md) method [- drawPageAtIndex:inRect:](<../uiprintpagerenderer/drawpage(at_in_).md>).

## See Also

### Getting the paper size and the printing area

- [paperSize](papersize.md) — The size of the sheet to use for printing.
