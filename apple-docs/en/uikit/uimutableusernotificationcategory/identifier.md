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
doc_path: /documentation/uikit/uimutableusernotificationcategory/identifier
source_url: 'https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableusernotificationcategory/identifier.json'
content_hash: 'sha256:b6596847b2103d82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableUserNotificationCategory](../uimutableusernotificationcategory.md)

# identifier

<sub>Instance Property</sub>

The name of the action group.

> [!warning] Deprecated
> For more information, see [UIMutableUserNotificationCategory](../uimutableusernotificationcategory.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var identifier: String? { get set }
```

## Discussion

This property is a writable version of the one declared by the parent class.

When generating a notification that includes these custom actions, you must use this string to initialize the notification. For local notifications, assign the string to the [category](../uilocalnotification/category.md) property of the [UILocalNotification](../uilocalnotification.md) object. For push notifications, use the string as the value of the `category` key in the push notification’s payload.

## See Also

### Modifying the action settings

- [- setActions:forContext:](<setactions(__for_).md>) — Sets the actions to display for different alert styles. _(deprecated)_
