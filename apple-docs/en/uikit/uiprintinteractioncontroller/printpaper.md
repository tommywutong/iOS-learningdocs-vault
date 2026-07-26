---
title: printPaper
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/printpaper
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printpaper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/printpaper.json'
content_hash: 'sha256:413be2f3a58a1d82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# printPaper

<sub>Instance Property</sub>

An object that represents the paper size and printing area for the print job.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printPaper: UIPrintPaper? { get }
```

## Discussion

`UIPrintInteractionController` sets this property immediately after the user selects a printer and before it calls the delegate’s [- printInteractionControllerWillStartJob:](<../uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(__).md>) method. If its delegate implements the [- printInteractionController:choosePaper:](<../uiprintinteractioncontrollerdelegate/printinteractioncontroller(__choosepaper_).md>) method of the `UIPrintInteractionControllerDelegate` protocol, it can return the [UIPrintPaper](../uiprintpaper.md) object to assign to this property. Otherwise, UIKit assigns an object with a default paper size and printing rectangle that is based on the output type and the capabilities of the destination printer. This object is released when the print job finishes.

## See Also

### Accessing print-job information

- [printInfo](printinfo.md) — An object that encapsulates information about the print job.
- [showsNumberOfCopies](showsnumberofcopies.md) — A Boolean value that determines whether the printing options include the number of copies.
- [showsPaperSelectionForLoadedPapers](showspaperselectionforloadedpapers.md) — A Boolean value that determines whether the paper selection menu displays.
- [showsPaperOrientation](showspaperorientation.md) — A Boolean value that indicates whether the printing options include the paper-orientation control.
- [showsPageRange](showspagerange.md) — A Boolean value that determines whether the printing options include a page-range control. _(deprecated)_
