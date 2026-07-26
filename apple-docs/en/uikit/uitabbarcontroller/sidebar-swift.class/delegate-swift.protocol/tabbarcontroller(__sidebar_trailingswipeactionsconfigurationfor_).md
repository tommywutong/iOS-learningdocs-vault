---
title: 'tabBarController(_:sidebar:trailingSwipeActionsConfigurationFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:trailingswipeactionsconfigurationfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:trailingswipeactionsconfigurationfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller%28_%3Asidebar%3Atrailingswipeactionsconfigurationfor%3A%29.json'
content_hash: 'sha256:d867928cbffe7fa8'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UITabBarController](../../../uitabbarcontroller.md) · [Sidebar](../../sidebar-swift.class.md) · [Delegate](../delegate-swift.protocol.md)

# tabBarController(_:sidebar:trailingSwipeActionsConfigurationFor:)

<sub>Instance Method</sub>

Called when the sidebar is about to show trailing swipe actions for a particular tab. Return either a UISwipeActionsConfiguration object or nil if this tab does not show swipe actions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, trailingSwipeActionsConfigurationFor tab: UITab) -> UISwipeActionsConfiguration?
```
