---
title: isCollapsedByDefault
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 26.1+, visionOS 26.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabgroup/iscollapsedbydefault
source_url: 'https://developer.apple.com/documentation/uikit/uitabgroup/iscollapsedbydefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabgroup/iscollapsedbydefault.json'
content_hash: 'sha256:2ba93841fb76a215'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabGroup](../uitabgroup.md)

# isCollapsedByDefault

<sub>Instance Property</sub>

Whether the group is initially displayed in a collapsed state in the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isCollapsedByDefault: Bool { get set }
```

## Discussion

When true, the group renders collapsed the first time it appears in the sidebar. The user can expand the group manually, and any subsequent user interactions or customization changes take precedence over this default.

This property has no effect in contexts where groups are not collapsible, such as when `sidebarAppearance == .inline`.

Default is `NO`.
