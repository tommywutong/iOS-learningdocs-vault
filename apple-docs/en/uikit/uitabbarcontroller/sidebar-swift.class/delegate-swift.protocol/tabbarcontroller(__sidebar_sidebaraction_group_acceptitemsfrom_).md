---
title: 'tabBarController(_:sidebar:sidebarAction:group:acceptItemsFrom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:sidebaraction:group:acceptitemsfrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:sidebaraction:group:acceptitemsfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller%28_%3Asidebar%3Asidebaraction%3Agroup%3Aacceptitemsfrom%3A%29.json'
content_hash: 'sha256:2d21f37539272f56'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UITabBarController](../../../uitabbarcontroller.md) · [Sidebar](../../sidebar-swift.class.md) · [Delegate](../delegate-swift.protocol.md)

# tabBarController(_:sidebar:sidebarAction:group:acceptItemsFrom:)

<sub>Instance Method</sub>

Receive the drop from into the `sidebarAction` using the specified session. This is only called if the drop operation returned from `tabBarController:sidebar:sidebarAction:operationForAcceptingItemsFromDropSession` is valid for a drop.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, sidebarAction: UIAction, group: UITabGroup, acceptItemsFrom session: any UIDropSession)
```
