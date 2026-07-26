---
title: 'removeDeliveredNotifications(withIdentifiers:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unusernotificationcenter/removedeliverednotifications(withidentifiers:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removedeliverednotifications(withidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/removedeliverednotifications%28withidentifiers%3A%29.json'
content_hash: 'sha256:3e788ce4490c3a2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# removeDeliveredNotifications(withIdentifiers:)

<sub>Instance Method</sub>

Removes your app’s notifications from Notification Center that match the specified identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func removeDeliveredNotifications(withIdentifiers identifiers: [String])
```

## Parameters

- `identifiers` — An array of [NSString](../../foundation/nsstring.md) objects, each of which corresponds to a value in the [identifier](../unnotificationrequest/identifier.md) property of a [UNNotificationRequest](../unnotificationrequest.md) object. This method ignores the identifiers of requests whose notifications are not currently displayed in Notification Center.

## Discussion

Use this method to selectively remove notifications that you no longer want displayed in Notification Center. The method executes asynchronously, returning immediately and removing the specified notifications on a background thread.

## See Also

### Removing delivered notifications

- [- getDeliveredNotificationsWithCompletionHandler:](<getdeliverednotifications(completionhandler_).md>) — Fetches all of your app’s delivered notifications that are still present in Notification Center.
- [- removeAllDeliveredNotifications](<removealldeliverednotifications().md>) — Removes all of your app’s delivered notifications from Notification Center.
