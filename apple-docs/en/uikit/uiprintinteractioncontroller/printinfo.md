---
title: printInfo
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/printinfo
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/printinfo.json'
content_hash: 'sha256:7cdcf07ba8d5e1aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# printInfo

<sub>Instance Property</sub>

An object that encapsulates information about the print job.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printInfo: UIPrintInfo? { get set }
```

## Discussion

An instance of [UIPrintInfo](../uiprintinfo.md) includes properties such as the print-job name, the printer identifier, the orientation of the printed content, the duplex mode, and the kind of content (general, photo, or grayscale). If you do not assign an instance of [UIPrintInfo](../uiprintinfo.md) to this property, the UIKit printing system assumes defaults for many of these properties. Users can modify the selected printer and the duplex mode (if available on the printer). Once the printing options are presented, any changes to the `UIPrintInfo` object referenced by this property are ignored. The object is released when printing completes.

## See Also

### Accessing print-job information

- [printPaper](printpaper.md) — An object that represents the paper size and printing area for the print job.
- [showsNumberOfCopies](showsnumberofcopies.md) — A Boolean value that determines whether the printing options include the number of copies.
- [showsPaperSelectionForLoadedPapers](showspaperselectionforloadedpapers.md) — A Boolean value that determines whether the paper selection menu displays.
- [showsPaperOrientation](showspaperorientation.md) — A Boolean value that indicates whether the printing options include the paper-orientation control.
- [showsPageRange](showspagerange.md) — A Boolean value that determines whether the printing options include a page-range control. _(deprecated)_
