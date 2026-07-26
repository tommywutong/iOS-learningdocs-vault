---
title: UISplitViewController.DisplayMode.twoOverSecondary
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twooversecondary
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twooversecondary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twooversecondary.json'
content_hash: 'sha256:333214aa3e8d26f6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [DisplayMode](../displaymode-swift.enum.md)

# UISplitViewController.DisplayMode.twoOverSecondary

<sub>Case</sub>

Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case twoOverSecondary
```

## Discussion

This display mode is only available for [UISplitViewControllerStyleTripleColumn](../style-swift.enum/triplecolumn.md) interfaces.

This display mode shows both sidebars layered on top of the secondary view controller, partially obscuring it. The secondary view controller is dimmed out, preventing interaction with its view. Touching the dimmed view dismisses the overlay and returns the interface to the [UISplitViewControllerDisplayModeSecondaryOnly](secondaryonly.md) display mode.

The interactive gesture can move the interface freely through [UISplitViewControllerDisplayModeOneOverSecondary](oneoversecondary.md) to [UISplitViewControllerDisplayModeSecondaryOnly](secondaryonly.md) and back, stopping at any of the display modes depending on the user interaction.

This display mode is available for the [UISplitViewControllerSplitBehaviorOverlay](../splitbehavior-swift.enum/overlay.md) split behavior.

## See Also

### Constants

- [UISplitViewControllerDisplayModeAutomatic](automatic.md) — The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewControllerDisplayModeSecondaryOnly](secondaryonly.md) — Only the secondary view controller is shown onscreen.
- [UISplitViewControllerDisplayModeOneBesideSecondary](onebesidesecondary.md) — One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeOneOverSecondary](oneoversecondary.md) — One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoBesideSecondary](twobesidesecondary.md) — Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeTwoDisplaceSecondary](twodisplacesecondary.md) — Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
