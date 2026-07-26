---
title: 'init(type:localizedTitle:localizedSubtitle:icon:userInfo:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationshortcutitem/init(type:localizedtitle:localizedsubtitle:icon:userinfo:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/init(type:localizedtitle:localizedsubtitle:icon:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcutitem/init%28type%3Alocalizedtitle%3Alocalizedsubtitle%3Aicon%3Auserinfo%3A%29.json'
content_hash: 'sha256:d1b4417325b08130'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationShortcutItem](../uiapplicationshortcutitem.md)

# init(type:localizedTitle:localizedSubtitle:icon:userInfo:)

<sub>Initializer</sub>

Creates an immutable Home Screen dynamic quick action with user-visible title, icon, and user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(type: String, localizedTitle: String, localizedSubtitle: String?, icon: UIApplicationShortcutIcon?, userInfo: [String : any NSSecureCoding]? = nil)
```

## Parameters

- `type` — The required, app-defined type of the Home Screen quick action.

- `localizedTitle` — The required, user-visible title of the Home Screen quick action.

- `localizedSubtitle` — The optional, user-visible subtitle of the Home Screen quick action.

- `icon` — The optional icon for the Home Screen quick action.

- `userInfo` — App-defined information about the Home Screen quick action, to be used by your app to implement the action. > [!important] Important > This method throws an exception if the value of this parameter isn’t property-list-encodable. For more information, see [Serializing Property Lists](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/serializing.html#//apple_ref/doc/uid/20000952) in [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) and see [PropertyListSerialization](../../foundation/propertylistserialization.md). One common, important use for this dictionary is to specify the version of your app. If a user installs an update for your app but hasn’t yet launched the update, pressing your Home Screen icon shows the dynamic quick actions for the previously-installed version. Including the app version in the `userInfo` dictionary lets you gracefully handle this scenario.

## Return Value

An immutable Home Screen dynamic quick action item with a user-visible title, optional subtitle, optional icon, and optional user info dictionary.

## See Also

### Creating a Home Screen dynamic quick action

- [- initWithType:localizedTitle:](<init(type_localizedtitle_).md>) — Creates an immutable Home Screen dynamic quick action with a user-visible title and no icon.
