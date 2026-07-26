---
title: removeAllPendingNotificationRequests()
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unusernotificationcenter/removeallpendingnotificationrequests()
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removeallpendingnotificationrequests()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/removeallpendingnotificationrequests%28%29.json'
content_hash: 'sha256:9bb7277a14ad696f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# removeAllPendingNotificationRequests()

<sub>Instance Method</sub>

Removes all of your app’s pending local notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeAllPendingNotificationRequests()
```

## Discussion

This method executes asynchronously, removing all pending notification requests on a secondary thread.

```swift
let center = UNUserNotificationCenter.current()
center.removeAllPendingNotificationRequests()
```

## See Also

### Scheduling notifications

- [- addNotificationRequest:withCompletionHandler:](<add(__withcompletionhandler_).md>) — Schedules the delivery of a local notification.
- [- getPendingNotificationRequestsWithCompletionHandler:](<getpendingnotificationrequests(completionhandler_).md>) — Fetches all of your app’s local notifications that are pending delivery.
- [- removePendingNotificationRequestsWithIdentifiers:](<removependingnotificationrequests(withidentifiers_).md>) — Removes your app’s local notifications that are pending and match the specified identifiers.
