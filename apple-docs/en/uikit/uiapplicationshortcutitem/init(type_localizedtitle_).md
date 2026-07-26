---
title: 'init(type:localizedTitle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationshortcutitem/init(type:localizedtitle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/init(type:localizedtitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcutitem/init%28type%3Alocalizedtitle%3A%29.json'
content_hash: 'sha256:f52a37e58415c0dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationShortcutItem](../uiapplicationshortcutitem.md)

# init(type:localizedTitle:)

<sub>Initializer</sub>

Creates an immutable Home Screen dynamic quick action with a user-visible title and no icon.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(type: String, localizedTitle: String)
```

## Parameters

- `type` — The required, app-defined type of the Home Screen quick action.

- `localizedTitle` — The required, user-visible title of the Home Screen quick action.

## Return Value

An immutable Home Screen dynamic quick action with a user-visible title and no icon.

## See Also

### Creating a Home Screen dynamic quick action

- [- initWithType:localizedTitle:localizedSubtitle:icon:userInfo:](<init(type_localizedtitle_localizedsubtitle_icon_userinfo_).md>) — Creates an immutable Home Screen dynamic quick action with user-visible title, icon, and user info dictionary.
