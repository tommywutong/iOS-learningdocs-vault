---
title: UISplitViewController.SplitBehavior.displace
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/displace
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/displace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/displace.json'
content_hash: 'sha256:1e48a14043c17e6e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [SplitBehavior](../splitbehavior-swift.enum.md)

# UISplitViewController.SplitBehavior.displace

<sub>Case</sub>

The sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case displace
```

## Discussion

This split behavior shows one or both sidebars tiled next to the secondary view controller. If both sidebars are visible, they partially displace the secondary view controller offscreen to make space for the primary column. The secondary view controller is dimmed out, preventing interaction with its view.

The possible display modes for this split behavior are:

- [UISplitViewControllerDisplayModeSecondaryOnly](../displaymode-swift.enum/secondaryonly.md)
- [UISplitViewControllerDisplayModeOneBesideSecondary](../displaymode-swift.enum/onebesidesecondary.md)
- [UISplitViewControllerDisplayModeTwoDisplaceSecondary](../displaymode-swift.enum/twodisplacesecondary.md)

If the current display mode is [UISplitViewControllerDisplayModeOneBesideSecondary](../displaymode-swift.enum/onebesidesecondary.md) and [presentsWithGesture](../presentswithgesture.md) is [true](../../../swift/true.md), the split view controller presents a special bar button item styled as a back-chevron icon. When a user taps this button, it changes the current display mode to [UISplitViewControllerDisplayModeTwoDisplaceSecondary](../displaymode-swift.enum/twodisplacesecondary.md).

## See Also

### Constants

- [UISplitViewControllerSplitBehaviorAutomatic](automatic.md) — The split view controller automatically decides the most appropriate split behavior based on the device and the current app size.
- [UISplitViewControllerSplitBehaviorTile](tile.md) — The sidebars and secondary view controller appear tiled side-by-side.
- [UISplitViewControllerSplitBehaviorOverlay](overlay.md) — The sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
