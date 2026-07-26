---
title: 'removePendingNotificationRequests(withIdentifiers:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unusernotificationcenter/removependingnotificationrequests(withidentifiers:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removependingnotificationrequests(withidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/removependingnotificationrequests%28withidentifiers%3A%29.json'
content_hash: 'sha256:f91e8aef4be44eb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# removePendingNotificationRequests(withIdentifiers:)

<sub>Instance Method</sub>

Removes your app’s local notifications that are pending and match the specified identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removePendingNotificationRequests(withIdentifiers identifiers: [String])
```

## Parameters

- `identifiers` — An array of [NSString](../../foundation/nsstring.md) objects, each of which contains the [identifier](../unnotificationrequest/identifier.md) of an active [UNNotificationRequest](../unnotificationrequest.md) object. If the identifier belongs to a non repeating request, and the trigger condition for that request has already been met, this method ignores the identifier.

## Discussion

This method executes asynchronously, removing the pending notification requests on a secondary thread.

```swift
let center = UNUserNotificationCenter.current()
center.removePendingNotificationRequests(withIdentifiers: ["com.example.mynotification"])
```

## See Also

### Scheduling notifications

- [- addNotificationRequest:withCompletionHandler:](<add(__withcompletionhandler_).md>) — Schedules the delivery of a local notification.
- [- getPendingNotificationRequestsWithCompletionHandler:](<getpendingnotificationrequests(completionhandler_).md>) — Fetches all of your app’s local notifications that are pending delivery.
- [- removeAllPendingNotificationRequests](<removeallpendingnotificationrequests().md>) — Removes all of your app’s pending local notifications.
