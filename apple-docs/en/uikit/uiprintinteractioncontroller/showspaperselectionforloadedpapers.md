---
title: showsPaperSelectionForLoadedPapers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/showspaperselectionforloadedpapers
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/showspaperselectionforloadedpapers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/showspaperselectionforloadedpapers.json'
content_hash: 'sha256:a20a2ab8cbd01c80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# showsPaperSelectionForLoadedPapers

<sub>Instance Property</sub>

A Boolean value that determines whether the paper selection menu displays.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var showsPaperSelectionForLoadedPapers: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). Setting the value to [true](../../swift/true.md) enables a paper selection menu on printers that support different types of paper and have more than one paper type loaded. On printers where only one paper type is available, no paper selection menu is displayed, regardless of the value of this property.

## See Also

### Accessing print-job information

- [printInfo](printinfo.md) — An object that encapsulates information about the print job.
- [printPaper](printpaper.md) — An object that represents the paper size and printing area for the print job.
- [showsNumberOfCopies](showsnumberofcopies.md) — A Boolean value that determines whether the printing options include the number of copies.
- [showsPaperOrientation](showspaperorientation.md) — A Boolean value that indicates whether the printing options include the paper-orientation control.
- [showsPageRange](showspagerange.md) — A Boolean value that determines whether the printing options include a page-range control. _(deprecated)_
