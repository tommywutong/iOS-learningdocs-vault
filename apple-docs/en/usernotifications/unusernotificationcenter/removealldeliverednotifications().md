---
title: removeAllDeliveredNotifications()
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unusernotificationcenter/removealldeliverednotifications()
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removealldeliverednotifications()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/removealldeliverednotifications%28%29.json'
content_hash: 'sha256:19e19051fea09858'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# removeAllDeliveredNotifications()

<sub>Instance Method</sub>

Removes all of your app’s delivered notifications from Notification Center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func removeAllDeliveredNotifications()
```

## Discussion

Use this method to remove all of your app’s delivered notifications from Notification Center. The method executes asynchronously, returning immediately and removing the identifiers on a background thread. This method does not affect any notification requests that are scheduled, but have not yet been delivered.

## See Also

### Removing delivered notifications

- [- getDeliveredNotificationsWithCompletionHandler:](<getdeliverednotifications(completionhandler_).md>) — Fetches all of your app’s delivered notifications that are still present in Notification Center.
- [- removeDeliveredNotificationsWithIdentifiers:](<removedeliverednotifications(withidentifiers_).md>) — Removes your app’s notifications from Notification Center that match the specified identifiers.
