---
title: footerContentConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontrollersidebar/footercontentconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollersidebar/footercontentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollersidebar/footercontentconfiguration.json'
content_hash: 'sha256:810ac6af5a4d38cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [Sidebar](../uitabbarcontroller/sidebar-swift.class.md)

# footerContentConfiguration

<sub>Instance Property</sub>

Content configuration for an optional header to display in the sidebar. The footer is displayed below all tab content in the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) id<UIContentConfiguration> footerContentConfiguration;
```

## See Also

### Headers and footers

- [bottomBarView](../uitabbarcontroller/sidebar-swift.class/bottombarview.md) — A view to display at the bottom of the sidebar, like a UIToolbar. The width of this view will be managed by the sidebar itself, and its height will be set to the value it returns from `systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:` Default is nil.
- [headerContentConfiguration](headercontentconfiguration.md) — Content configuration for an optional header to display in the sidebar. The header is displayed above all tab content in the sidebar.
