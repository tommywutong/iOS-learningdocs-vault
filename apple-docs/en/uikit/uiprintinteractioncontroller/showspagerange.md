---
title: showsPageRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+（10.0 起废弃）, iPadOS 4.2+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiprintinteractioncontroller/showspagerange
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/showspagerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/showspagerange.json'
content_hash: 'sha256:2e8ce8333d7ab891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# showsPageRange

<sub>Instance Property</sub>

A Boolean value that determines whether the printing options include a page-range control.

> [!warning] Deprecated
> The print interaction controller always shows the page range because a person can remove pages from the print preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var showsPageRange: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). If you assign printable content to the [printingItems](printingitems.md) property, the page-range control is not shown, even if `showPageRange` is [true](../../swift/true.md). In other cases, the number of pages to print must be greater than 1 form the page-range control to appear.

## See Also

### Accessing print-job information

- [printInfo](printinfo.md) — An object that encapsulates information about the print job.
- [printPaper](printpaper.md) — An object that represents the paper size and printing area for the print job.
- [showsNumberOfCopies](showsnumberofcopies.md) — A Boolean value that determines whether the printing options include the number of copies.
- [showsPaperSelectionForLoadedPapers](showspaperselectionforloadedpapers.md) — A Boolean value that determines whether the paper selection menu displays.
- [showsPaperOrientation](showspaperorientation.md) — A Boolean value that indicates whether the printing options include the paper-orientation control.
