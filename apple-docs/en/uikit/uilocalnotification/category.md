---
title: category
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/category
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/category'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/category.json'
content_hash: 'sha256:1e7fded683c69f9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# category

<sub>Instance Property</sub>

The name of a group of actions to display in the alert.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var category: String? { get set }
```

## Discussion

The value of this property is the category name associated with a registered [UIUserNotificationSettings](../uiusernotificationsettings.md) object. When the alert for the local notification is displayed, the system uses the string you specify to look up the group and retrieve its actions. It then adds a button to the alert for each action defined by the group. When the user taps one of those buttons, the app is woken up (or launched) and given a chance to perform the designated action. If the specified category name does not belong to a registered group of actions, the alert does not display any additional action buttons.

Specifying custom actions is optional. The value of this property is `nil` by default.

## See Also

### Composing the alert

- [alertBody](alertbody.md) — The message displayed in the notification alert. _(deprecated)_
- [alertAction](alertaction.md) — The title of the action button or slider. _(deprecated)_
- [alertTitle](alerttitle.md) — A short description of the reason for the alert. _(deprecated)_
- [hasAction](hasaction.md) — A Boolean value that controls whether the notification shows or hides the alert action. _(deprecated)_
- [alertLaunchImage](alertlaunchimage.md) — Identifies the image used as the launch image when the user taps (or slides) the action button (or slider). _(deprecated)_
