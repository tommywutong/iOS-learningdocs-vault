---
title: icon
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplicationshortcutitem/icon
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/icon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcutitem/icon.json'
content_hash: 'sha256:80315804ad293ec2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationShortcutItem](../uiapplicationshortcutitem.md)

# icon

<sub>Instance Property</sub>

The optional icon for the Home Screen dynamic quick action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var icon: UIApplicationShortcutIcon? { get }
```

## Discussion

Quick action icons are template (alpha-channel-only) images that you typically provide as part of an asset catalog. For more information, see [UIApplicationShortcutIcon](../uiapplicationshortcuticon.md).

## See Also

### Inspecting a Home Screen dynamic quick action

- [localizedTitle](localizedtitle.md) — The required, user-visible title for the Home Screen dynamic quick action.
- [localizedSubtitle](localizedsubtitle.md) — The optional, user-visible subtitle for the Home Screen dynamic quick action.
- [type](type.md) — A required, app-specific string that you employ to identify the type of quick action to perform.
- [userInfo](userinfo.md) — Optional, app-specific information that you can provide for use when your app performs the Home screen quick action.
