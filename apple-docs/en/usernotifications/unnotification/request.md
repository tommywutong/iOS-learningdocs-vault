---
title: request
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotification/request
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotification/request'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotification/request.json'
content_hash: 'sha256:3a3ef9a6b4f6af28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotification](../unnotification.md)

# request

<sub>Instance Property</sub>

The notification request containing the payload and trigger condition for the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var request: UNNotificationRequest { get }
```

## Discussion

For local notifications, the request object is a copy of the one you originally configured. For remote notifications, the system synthesizes the request object from information received from Apple Push Notification service.

## See Also

### Getting the Notification Details

- [date](date.md) — The delivery date of the notification.
