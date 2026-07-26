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
doc_path: /documentation/uikit/uiapplicationshortcutitem/userinfo
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcutitem/userinfo.json'
content_hash: 'sha256:e776f9a92be97e1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationShortcutItem](../uiapplicationshortcutitem.md)

# userInfo

<sub>Instance Property</sub>

Optional, app-specific information that you can provide for use when your app performs the Home screen quick action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var userInfo: [String : any NSSecureCoding]? { get }
```

## Discussion

The keys and values in this property’s dictionary must conform to the [NSSecureCoding](../../foundation/nssecurecoding.md) protocol, and must be property-list-encodable. If they aren’t, the system raises a runtime exception when initializing the quick action. For information about property-list-encodable data, see [Serializing Property Lists](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/serializing.html#//apple_ref/doc/uid/20000952) in [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) and see [PropertyListSerialization](../../foundation/propertylistserialization.md).

## See Also

### Inspecting a Home Screen dynamic quick action

- [localizedTitle](localizedtitle.md) — The required, user-visible title for the Home Screen dynamic quick action.
- [localizedSubtitle](localizedsubtitle.md) — The optional, user-visible subtitle for the Home Screen dynamic quick action.
- [type](type.md) — A required, app-specific string that you employ to identify the type of quick action to perform.
- [icon](icon.md) — The optional icon for the Home Screen dynamic quick action.
