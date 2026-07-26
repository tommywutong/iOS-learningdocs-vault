---
title: UISplitViewController.SplitBehavior.tile
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/tile
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/tile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/tile.json'
content_hash: 'sha256:b92dd5362fe23222'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [SplitBehavior](../splitbehavior-swift.enum.md)

# UISplitViewController.SplitBehavior.tile

<sub>Case</sub>

The sidebars and secondary view controller appear tiled side-by-side.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case tile
```

## Discussion

This split behavior shows one or both sidebars tiled next to the secondary view controller. The secondary view controller’s view is fully interactive.

The possible display modes for this split behavior are:

- [UISplitViewControllerDisplayModeSecondaryOnly](../displaymode-swift.enum/secondaryonly.md)
- [UISplitViewControllerDisplayModeOneBesideSecondary](../displaymode-swift.enum/onebesidesecondary.md)
- [UISplitViewControllerDisplayModeTwoBesideSecondary](../displaymode-swift.enum/twobesidesecondary.md)

If [presentsWithGesture](../presentswithgesture.md) is [true](../../../swift/true.md), the split view controller presents a special bar button item styled as a sidebar toggle icon.

For a double-column split view interface, when a user taps this button, it toggles the current display mode between [UISplitViewControllerDisplayModeSecondaryOnly](../displaymode-swift.enum/secondaryonly.md) and [UISplitViewControllerDisplayModeOneBesideSecondary](../displaymode-swift.enum/onebesidesecondary.md).

For a triple-column split view interface, when a user taps this button, it toggles the current display mode between [UISplitViewControllerDisplayModeOneBesideSecondary](../displaymode-swift.enum/onebesidesecondary.md) and [UISplitViewControllerDisplayModeTwoBesideSecondary](../displaymode-swift.enum/twobesidesecondary.md). The button doesn’t appear in [UISplitViewControllerDisplayModeSecondaryOnly](../displaymode-swift.enum/secondaryonly.md).

## See Also

### Constants

- [UISplitViewControllerSplitBehaviorAutomatic](automatic.md) — The split view controller automatically decides the most appropriate split behavior based on the device and the current app size.
- [UISplitViewControllerSplitBehaviorOverlay](overlay.md) — The sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerSplitBehaviorDisplace](displace.md) — The sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
