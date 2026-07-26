---
title: types
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationsettings/types
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationsettings/types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationsettings/types.json'
content_hash: 'sha256:5488515dcafdfd35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserNotificationSettings](../uiusernotificationsettings.md)

# types

<sub>Instance Property</sub>

A bitmask of the notification types that your app is allowed to use.

> [!warning] Deprecated
> For more information, see [UIUserNotificationSettings](../uiusernotificationsettings.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var types: UIUserNotificationType { get }
```

## Discussion

When you create a new settings object, this property contains all of the types you specified. After you register your request with the app, the app provides you with a new settings object that contains only the types that your app is allowed to use.

## See Also

### Related Documentation

- [UIUserNotificationSettings](../uiusernotificationsettings.md) — The types of notifications that can be displayed to the user by your app. _(deprecated)_

### Getting the configured settings

- [categories](categories.md) — The app’s registered groups of actions. _(deprecated)_
