---
title: isAvailable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/sidebar-swift.class/isavailable
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/isavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/isavailable.json'
content_hash: 'sha256:6f59251d65e15c9b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBarController](../../uitabbarcontroller.md) · [Sidebar](../sidebar-swift.class.md)

# isAvailable

<sub>Instance Property</sub>

Indicates when the tab sidebar is available to be displayed in the current context. When available, the sidebar is either visible, or can become visible depending on `isHidden`. Use this property to gate behaviors or UI that is dependent on the availability of the sidebar (like child tabs, or landing pages for groups).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isAvailable: Bool { get }
```

## Discussion

Implement the delegate method `tabBarController:sidebarAvailabilityDidChange:` to be notified when the value of this property changes.
