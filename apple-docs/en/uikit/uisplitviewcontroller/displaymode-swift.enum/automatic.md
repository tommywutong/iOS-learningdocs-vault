---
title: UISplitViewController.DisplayMode.automatic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/automatic
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/automatic.json'
content_hash: 'sha256:bd47264a9beff733'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISplitViewController](../../uisplitviewcontroller.md) · [DisplayMode](../displaymode-swift.enum.md)

# UISplitViewController.DisplayMode.automatic

<sub>Case</sub>

The split view controller automatically decides the most appropriate display mode based on the device and the current app size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case automatic
```

## Discussion

This constant represents the default value of the [preferredDisplayMode](../preferreddisplaymode.md) property. Although you can assign the property this constant as its value, the [displayMode](../displaymode-swift.property.md) property never reports it.

## See Also

### Constants

- [UISplitViewControllerDisplayModeSecondaryOnly](secondaryonly.md) — Only the secondary view controller is shown onscreen.
- [UISplitViewControllerDisplayModeOneBesideSecondary](onebesidesecondary.md) — One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeOneOverSecondary](oneoversecondary.md) — One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoBesideSecondary](twobesidesecondary.md) — Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewControllerDisplayModeTwoOverSecondary](twooversecondary.md) — Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerDisplayModeTwoDisplaceSecondary](twodisplacesecondary.md) — Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
