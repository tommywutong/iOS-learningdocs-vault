---
title: UITabBarController.Sidebar.Layout.overlap
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/sidebar-swift.class/layout/overlap
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/layout/overlap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/layout/overlap.json'
content_hash: 'sha256:6e2c1260f7dd6241'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UITabBarController](../../../uitabbarcontroller.md) · [Sidebar](../../sidebar-swift.class.md) · [Layout](../layout.md)

# UITabBarController.Sidebar.Layout.overlap

<sub>Case</sub>

When the sidebar is displayed, it will overlap the selected view controller, allowing the selected view controller to render underneath the sidebar. Anchor the view’s content to the `layoutMarginsGuide` or `safeAreaLayoutGuide` to avoid being occluded by the sidebar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case overlap
```
