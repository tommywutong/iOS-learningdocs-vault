---
title: UISplitViewController.DisplayMode.twoDisplaceSecondary
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary.json'
content_hash: 'sha256:72f2cc32b14517a9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [DisplayMode](../displaymode-swift.enum.md)

# UISplitViewController.DisplayMode.twoDisplaceSecondary

<sub>Case</sub>

Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case twoDisplaceSecondary
```

## Discussion

This display mode is only available for [UISplitViewControllerStyleTripleColumn](../style-swift.enum/triplecolumn.md) interfaces.

This display mode shows both sidebars, which partially displace the secondary view controller offscreen to make space for the primary column. The secondary view controller is dimmed out, preventing interaction with its view. Touching the dimmed view or using a gesture returns the interface to the [UISplitViewControllerDisplayModeOneBesideSecondary](onebesidesecondary.md) display mode.

This display mode is available for the [UISplitViewControllerSplitBehaviorDisplace](../splitbehavior-swift.enum/displace.md) split behavior.

## See Also

### Constants

- [UISplitViewControllerDisplayModeAutomatic](automatic.md) — The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewControllerDisplayModeSecondaryOnly](secondaryonly.md) — Only the secondary view controller is shown onscreen.
- [UISplitViewControllerDisplayModeOneBesideSecondary](onebesidesecondary.md) — One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeOneOverSecondary](oneoversecondary.md) — One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoBesideSecondary](twobesidesecondary.md) — Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeTwoOverSecondary](twooversecondary.md) — Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
