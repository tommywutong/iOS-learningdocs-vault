---
title: categories
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationsettings/categories
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationsettings/categories'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationsettings/categories.json'
content_hash: 'sha256:d018b09ab7e09357'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserNotificationSettings](../uiusernotificationsettings.md)

# categories

<sub>Instance Property</sub>

The app’s registered groups of actions.

> [!warning] Deprecated
> For more information, see [UIUserNotificationSettings](../uiusernotificationsettings.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var categories: Set<UIUserNotificationCategory>? { get }
```

## Discussion

This property contains the [UIUserNotificationCategory](../uiusernotificationcategory.md) objects that you specified when creating the settings object. Each object corresponds to a group of actions that may be displayed in conjunction with a push notification. After registration, this property contains the set of actions you specified in your initial request.

## See Also

### Related Documentation

- [+ settingsForTypes:categories:](<init(types_categories_).md>) — Creates and returns a settings object that you can use to register your requested notification and action types. _(deprecated)_

### Getting the configured settings

- [types](types.md) — A bitmask of the notification types that your app is allowed to use. _(deprecated)_
