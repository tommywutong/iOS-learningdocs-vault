---
title: UISplitViewController.DisplayMode.oneBesideSecondary
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.json'
content_hash: 'sha256:7f55ad7cb4617156'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [DisplayMode](../displaymode-swift.enum.md)

# UISplitViewController.DisplayMode.oneBesideSecondary

<sub>Case</sub>

One sidebar appears side-by-side with the secondary view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case oneBesideSecondary
```

## Discussion

This display mode shows one sidebar tiled next to the secondary view controller. The sidebar shown is the primary column for [UISplitViewControllerStyleDoubleColumn](../style-swift.enum/doublecolumn.md) interfaces and the supplementary column for [UISplitViewControllerStyleTripleColumn](../style-swift.enum/triplecolumn.md) interfaces. The sidebar is displayed on the side specified by [primaryEdge](../primaryedge-swift.property.md), followed by the secondary view controller. The secondary view controller’s view is fully interactive.

This display mode is available for the [UISplitViewControllerSplitBehaviorTile](../splitbehavior-swift.enum/tile.md) and [UISplitViewControllerSplitBehaviorDisplace](../splitbehavior-swift.enum/displace.md) split behaviors.

## See Also

### Constants

- [UISplitViewControllerDisplayModeAutomatic](automatic.md) — The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewControllerDisplayModeSecondaryOnly](secondaryonly.md) — Only the secondary view controller is shown onscreen.
- [UISplitViewControllerDisplayModeOneOverSecondary](oneoversecondary.md) — One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoBesideSecondary](twobesidesecondary.md) — Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeTwoOverSecondary](twooversecondary.md) — Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoDisplaceSecondary](twodisplacesecondary.md) — Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
