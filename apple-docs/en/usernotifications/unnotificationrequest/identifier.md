---
title: identifier
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationrequest/identifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationrequest/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationrequest/identifier.json'
content_hash: 'sha256:7431dd78a4d32ce6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationRequest](../unnotificationrequest.md)

# identifier

<sub>Instance Property</sub>

The unique identifier for this notification request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identifier: String { get }
```

## Discussion

Use this string to identify notifications in your app. For example, you can pass this string to the [- removePendingNotificationRequestsWithIdentifiers:](<../unusernotificationcenter/removependingnotificationrequests(withidentifiers_).md>) method to cancel a previously scheduled notification.

If you use the same identifier when scheduling a new notification, the system removes the previously scheduled notification with that identifier and replaces it with the new one.

For local notifications, the system sets this property to the value passed to the request’s initializer (see the [+ requestWithIdentifier:content:trigger:](<init(identifier_content_trigger_).md>) method). For remote notifications, the system sets this property to the value of the `apns-collapse-id` key that you specified in the APNs request header when generating the remote notification. If your app doesn’t set a value, the system automatically assigns an identifier.

## See Also

### Getting the Request Details

- [content](content.md) — The content associated with the notification.
- [trigger](trigger.md) — The conditions that trigger the delivery of the notification.
