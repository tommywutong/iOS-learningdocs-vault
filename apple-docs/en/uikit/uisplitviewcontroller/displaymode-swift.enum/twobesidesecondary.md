---
title: UISplitViewController.DisplayMode.twoBesideSecondary
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twobesidesecondary
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twobesidesecondary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twobesidesecondary.json'
content_hash: 'sha256:16217377fd2bcb56'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [DisplayMode](../displaymode-swift.enum.md)

# UISplitViewController.DisplayMode.twoBesideSecondary

<sub>Case</sub>

Two sidebars appear side-by-side with the secondary view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case twoBesideSecondary
```

## Discussion

This display mode is only available for [UISplitViewControllerStyleTripleColumn](../style-swift.enum/triplecolumn.md) interfaces.

This display mode shows both sidebars tiled next to the secondary view controller. The primary view controller is displayed on the side specified by [primaryEdge](../primaryedge-swift.property.md), followed by the supplementary view controller, and finally the secondary view controller. The secondary view controller’s view is fully interactive.

This display mode is available for the [UISplitViewControllerSplitBehaviorTile](../splitbehavior-swift.enum/tile.md) split behavior.

## See Also

### Constants

- [UISplitViewControllerDisplayModeAutomatic](automatic.md) — The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewControllerDisplayModeSecondaryOnly](secondaryonly.md) — Only the secondary view controller is shown onscreen.
- [UISplitViewControllerDisplayModeOneBesideSecondary](onebesidesecondary.md) — One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeOneOverSecondary](oneoversecondary.md) — One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoOverSecondary](twooversecondary.md) — Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoDisplaceSecondary](twodisplacesecondary.md) — Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
