---
title: 'tabBarController(_:sidebar:leadingSwipeActionsConfigurationFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:leadingswipeactionsconfigurationfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:leadingswipeactionsconfigurationfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller%28_%3Asidebar%3Aleadingswipeactionsconfigurationfor%3A%29.json'
content_hash: 'sha256:796fec6f85ccedd1'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UITabBarController](../../../uitabbarcontroller.md) · [Sidebar](../../sidebar-swift.class.md) · [Delegate](../delegate-swift.protocol.md)

# tabBarController(_:sidebar:leadingSwipeActionsConfigurationFor:)

<sub>Instance Method</sub>

Called when the sidebar is about to show leading swipe actions for the specified `tab`. Return either a concrete `UISwipeActionsConfiguration` or nil if the tab does not show swipe actions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, leadingSwipeActionsConfigurationFor tab: UITab) -> UISwipeActionsConfiguration?
```
