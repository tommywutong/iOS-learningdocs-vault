---
title: userInfo
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimutableapplicationshortcutitem/userinfo
source_url: 'https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableapplicationshortcutitem/userinfo.json'
content_hash: 'sha256:c129b1f23c6a6102'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableApplicationShortcutItem](../uimutableapplicationshortcutitem.md)

# userInfo

<sub>Instance Property</sub>

Optional, app-specific information that you can provide for use when your app performs the Home Screen dynamic mutable quick action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var userInfo: [String : any NSSecureCoding]? { get set }
```

## Discussion

The keys and values in this property’s dictionary must conform to the [NSSecureCoding](../../foundation/nssecurecoding.md) protocol, and must be property-list-encodable. If they aren’t, the system raises a runtime exception when initializing the quick action. For information about property-list-encodable data, see [Serializing Property Lists](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/serializing.html#//apple_ref/doc/uid/20000952) in [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) and see [PropertyListSerialization](../../foundation/propertylistserialization.md).

## See Also

### Inspecting a Home Screen dynamic mutable quick action

- [localizedTitle](localizedtitle.md) — The required, user-visible title for the Home Screen dynamic mutable quick action.
- [localizedSubtitle](localizedsubtitle.md) — The optional, user-visible subtitle for the Home Screen dynamic mutable quick action.
- [type](type.md) — A required, app-specific string that you can employ to identify the type of quick action to perform.
- [icon](icon.md) — The optional icon for the Home Screen dynamic mutable quick action.
