---
title: preferredPlacement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/sidebar-swift.class/preferredplacement
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/preferredplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/preferredplacement.json'
content_hash: 'sha256:dabbcaa281c0a829'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBarController](../../uitabbarcontroller.md) · [Sidebar](../sidebar-swift.class.md)

# preferredPlacement

<sub>Instance Property</sub>

The preferred placement for the tab bar controller when the sidebar and tab bar are mutually exclusive, and only one placement can be displayed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredPlacement: UITabBarController.Sidebar.Placement { get set }
```

## Discussion

When set to `UITabBarControllerSidebarPlacementAutomatic`, the system resolves to the platform default. On iOS, this resolves to showing the tab bar by default. This property has no effect on platforms where multiple placements are supported, like on iPadOS, where the sidebar can be minimized into the top tab bar.

Default is `UITabBarControllerSidebarPlacementAutomatic`.
