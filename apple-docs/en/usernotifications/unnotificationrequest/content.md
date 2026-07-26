---
title: content
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationrequest/content
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationrequest/content'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationrequest/content.json'
content_hash: 'sha256:7d1e1051d0cbb6f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationRequest](../unnotificationrequest.md)

# content

<sub>Instance Property</sub>

The content associated with the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var content: UNNotificationContent { get }
```

## Discussion

Use this property to access the contents of the notification.

## See Also

### Getting the Request Details

- [identifier](identifier.md) — The unique identifier for this notification request.
- [trigger](trigger.md) — The conditions that trigger the delivery of the notification.
