---
title: UISplitViewController.DisplayMode.secondaryOnly
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/secondaryonly
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/secondaryonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/secondaryonly.json'
content_hash: 'sha256:c404fa2e4828316f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [DisplayMode](../displaymode-swift.enum.md)

# UISplitViewController.DisplayMode.secondaryOnly

<sub>Case</sub>

Only the secondary view controller is shown onscreen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case secondaryOnly
```

## Discussion

The primary and supplementary view controllers are offscreen.

This display mode is available for any split behavior.

## See Also

### Constants

- [UISplitViewControllerDisplayModeAutomatic](automatic.md) — The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewControllerDisplayModeOneBesideSecondary](onebesidesecondary.md) — One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeOneOverSecondary](oneoversecondary.md) — One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoBesideSecondary](twobesidesecondary.md) — Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeTwoOverSecondary](twooversecondary.md) — Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoDisplaceSecondary](twodisplacesecondary.md) — Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
