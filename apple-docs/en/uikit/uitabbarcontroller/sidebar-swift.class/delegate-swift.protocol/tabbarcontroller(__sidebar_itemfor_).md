---
title: 'tabBarController(_:sidebar:itemFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:itemfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:itemfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller%28_%3Asidebar%3Aitemfor%3A%29.json'
content_hash: 'sha256:1f2fbfdb68ed8b03'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UITabBarController](../../../uitabbarcontroller.md) · [Sidebar](../../sidebar-swift.class.md) · [Delegate](../delegate-swift.protocol.md)

# tabBarController(_:sidebar:itemFor:)

<sub>Instance Method</sub>

Return a `UITabSidebarItem` for the specified item request. When created, the item will be preconfigured to the appropriate defaults for its given content. If this method is not implemented, a default sidebar item will be provided for the request.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, itemFor request: UITabSidebarItem.Request) -> UITabSidebarItem
```
