---
title: isSidebarDestination
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabgroup/issidebardestination
source_url: 'https://developer.apple.com/documentation/uikit/uitabgroup/issidebardestination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabgroup/issidebardestination.json'
content_hash: 'sha256:d59164ec8ed544d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabGroup](../uitabgroup.md)

# isSidebarDestination

<sub>Instance Property</sub>

Determines if the tab group itself can be selected as a destination in the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isSidebarDestination: Bool { get set }
```

## Discussion

By default, tab groups are not destinations when displayed in the sidebar, and cannot be selected directly by users. When enabled, the tab group becomes a selectable item in the sidebar, and will no longer perform automatic selection for a default child if no child is currently selected. The default value is NO.
