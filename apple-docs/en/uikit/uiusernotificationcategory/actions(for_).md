---
title: 'actions(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiusernotificationcategory/actions(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationcategory/actions(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationcategory/actions%28for%3A%29.json'
content_hash: 'sha256:cdc23e8c88a73187'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserNotificationCategory](../uiusernotificationcategory.md)

# actions(for:)

<sub>Instance Method</sub>

Returns the actions to be displayed for the given notification context.

> [!warning] Deprecated
> For more information, see [UIUserNotificationCategory](../uiusernotificationcategory.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func actions(for context: UIUserNotificationActionContext) -> [UIUserNotificationAction]?
```

## Parameters

- `context` — The context in which the notification is displayed. Notifications can have a default context or a minimal context depending on whether the notification was just delivered or the user is looking at it in more detail.

## Return Value

An array of [UIUserNotificationAction](../uiusernotificationaction.md) objects to be displayed in the specified context. The order of the objects in the array represents the order that they are displayed in the resulting notification.

## Discussion

This method returns the actions associated with the specified display context. To set the actions for a given context, you must create a [UIMutableUserNotificationCategory](../uimutableusernotificationcategory.md) object and use its setActions:forContext: method to specify your actions.

## See Also

### Getting the group configuration

- [identifier](identifier.md) — The name of the action group. _(deprecated)_
