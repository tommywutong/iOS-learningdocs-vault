---
title: 'tabBarController(_:sidebarVisibilityWillChange:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebarvisibilitywillchange:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebarvisibilitywillchange:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller%28_%3Asidebarvisibilitywillchange%3Aanimator%3A%29.json'
content_hash: 'sha256:34aa7f3ae6a9c84b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UITabBarController](../../../uitabbarcontroller.md) · [Sidebar](../../sidebar-swift.class.md) · [Delegate](../delegate-swift.protocol.md)

# tabBarController(_:sidebarVisibilityWillChange:animator:)

<sub>Instance Method</sub>

Notifies the delegate when the visibility of the sidebar is about to change when `sidebar.isHidden` changes. Add animations to the animator to run alongside the visibility update. Alongside animations and completions will run immediately if the sidebar visibility is changed without animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebarVisibilityWillChange sidebar: UITabBarController.Sidebar, animator: any UITabBarController.Sidebar.Animating)
```
