---
title: identifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationcategory/identifier
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationcategory/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationcategory/identifier.json'
content_hash: 'sha256:79e8285f35089df8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserNotificationCategory](../uiusernotificationcategory.md)

# identifier

<sub>Instance Property</sub>

The name of the action group.

> [!warning] Deprecated
> For more information, see [UIUserNotificationCategory](../uiusernotificationcategory.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var identifier: String? { get }
```

## Discussion

When generating a notification that includes these custom actions, you must use this string to initialize the notification. For local notifications, assign the string to the [category](../uilocalnotification/category.md) property of the [UILocalNotification](../uilocalnotification.md) object. For push notifications, use the string as the value of the `category` key in the push notification’s payload.

## See Also

### Getting the group configuration

- [- actionsForContext:](<actions(for_).md>) — Returns the actions to be displayed for the given notification context. _(deprecated)_
