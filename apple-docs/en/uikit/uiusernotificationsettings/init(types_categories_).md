---
title: 'init(types:categories:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiusernotificationsettings/init(types:categories:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationsettings/init(types:categories:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationsettings/init%28types%3Acategories%3A%29.json'
content_hash: 'sha256:bb511c39663a71fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserNotificationSettings](../uiusernotificationsettings.md)

# init(types:categories:)

<sub>Initializer</sub>

Creates and returns a settings object that you can use to register your requested notification and action types.

> [!warning] Deprecated
> For more information, see [UIUserNotificationSettings](../uiusernotificationsettings.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
convenience init(types: UIUserNotificationType, categories: Set<UIUserNotificationCategory>?)
```

## Parameters

- `types` — The notification types that your app supports. For a list of possible values, see the constants for the [UIUserNotificationType](../uiusernotificationtype.md) type.

- `categories` — A set of [UIUserNotificationCategory](../uiusernotificationcategory.md) objects that define the groups of actions a notification may include.

## Return Value

A new user notification settings object that you can register with the [UIApplication](../uiapplication.md) object.

## Discussion

Use this method to create a new settings object that you intend to register with the app. When calling this method, specify the types of notifications you intend to deliver to the user such as alerts or sounds. If you intend to display custom actions in your notifications, use this method to register those actions as well.

After creating a new settings object, register that object by calling the [- registerUserNotificationSettings:](<../uiapplication/registerusernotificationsettings(__).md>) method of the shared [UIApplication](../uiapplication.md) object.
