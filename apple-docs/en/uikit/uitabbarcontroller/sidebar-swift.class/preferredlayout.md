---
title: preferredLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/sidebar-swift.class/preferredlayout
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/preferredlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/preferredlayout.json'
content_hash: 'sha256:567768d73a8b2a69'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBarController](../../uitabbarcontroller.md) · [Sidebar](../sidebar-swift.class.md)

# preferredLayout

<sub>Instance Property</sub>

The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredLayout: UITabBarController.Sidebar.Layout { get set }
```

## See Also

### Managing customization

- [hidden](ishidden.md) — Determines if the sidebar is currently hidden.
- [Layout](layout.md)
- [- reconfigureItemForTab:](<reconfigureitem(for_).md>) — Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.
