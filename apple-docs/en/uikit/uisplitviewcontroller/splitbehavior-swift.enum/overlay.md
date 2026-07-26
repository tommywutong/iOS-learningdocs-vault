---
title: UISplitViewController.SplitBehavior.overlay
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/overlay
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/overlay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/overlay.json'
content_hash: 'sha256:cd472e8e093f564a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [SplitBehavior](../splitbehavior-swift.enum.md)

# UISplitViewController.SplitBehavior.overlay

<sub>Case</sub>

The sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case overlay
```

## Discussion

This split behavior shows one or both sidebars layered on top of the secondary view controller, partially obscuring it. The secondary view controller is dimmed out, preventing interaction with its view.

The possible display modes for this split behavior are:

- [UISplitViewControllerDisplayModeSecondaryOnly](../displaymode-swift.enum/secondaryonly.md)
- [UISplitViewControllerDisplayModeOneOverSecondary](../displaymode-swift.enum/oneoversecondary.md)
- [UISplitViewControllerDisplayModeTwoOverSecondary](../displaymode-swift.enum/twooversecondary.md)

If the current display mode is not [UISplitViewControllerDisplayModeTwoOverSecondary](../displaymode-swift.enum/twooversecondary.md) and [presentsWithGesture](../presentswithgesture.md) is [true](../../../swift/true.md), the split view controller presents a special bar button item styled as a back-chevron icon. When a user taps this button, it changes the current display mode from [UISplitViewControllerDisplayModeSecondaryOnly](../displaymode-swift.enum/secondaryonly.md) to [UISplitViewControllerDisplayModeOneOverSecondary](../displaymode-swift.enum/oneoversecondary.md), and from [UISplitViewControllerDisplayModeOneOverSecondary](../displaymode-swift.enum/oneoversecondary.md) to [UISplitViewControllerDisplayModeTwoOverSecondary](../displaymode-swift.enum/twooversecondary.md).

## See Also

### Constants

- [UISplitViewControllerSplitBehaviorAutomatic](automatic.md) — The split view controller automatically decides the most appropriate split behavior based on the device and the current app size.
- [UISplitViewControllerSplitBehaviorTile](tile.md) — The sidebars and secondary view controller appear tiled side-by-side.
- [UISplitViewControllerSplitBehaviorDisplace](displace.md) — The sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
