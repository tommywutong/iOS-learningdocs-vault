---
title: 'reconfigureItem(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontroller/sidebar-swift.class/reconfigureitem(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/reconfigureitem(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/reconfigureitem%28for%3A%29.json'
content_hash: 'sha256:f59962778160869e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBarController](../../uitabbarcontroller.md) · [Sidebar](../sidebar-swift.class.md)

# reconfigureItem(for:)

<sub>Instance Method</sub>

Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func reconfigureItem(for tab: UITab)
```

## See Also

### Managing customization

- [hidden](ishidden.md) — Determines if the sidebar is currently hidden.
- [preferredLayout](preferredlayout.md) — The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`
- [Layout](layout.md)
