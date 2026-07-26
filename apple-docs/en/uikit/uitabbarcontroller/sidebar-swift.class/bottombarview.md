---
title: bottomBarView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/sidebar-swift.class/bottombarview
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/bottombarview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/bottombarview.json'
content_hash: 'sha256:6235ba4ede42afa8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBarController](../../uitabbarcontroller.md) · [Sidebar](../sidebar-swift.class.md)

# bottomBarView

<sub>Instance Property</sub>

A view to display at the bottom of the sidebar, like a UIToolbar. The width of this view will be managed by the sidebar itself, and its height will be set to the value it returns from `systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:` Default is nil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var bottomBarView: UIView? { get set }
```

## See Also

### Headers and footers

- [footerContentConfiguration](footercontentconfiguration.md)
- [headerContentConfiguration](headercontentconfiguration.md)
