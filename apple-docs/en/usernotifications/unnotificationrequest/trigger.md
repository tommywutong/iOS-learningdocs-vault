---
title: trigger
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationrequest/trigger
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationrequest/trigger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationrequest/trigger.json'
content_hash: 'sha256:c174306c7b764b85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationRequest](../unnotificationrequest.md)

# trigger

<sub>Instance Property</sub>

The conditions that trigger the delivery of the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var trigger: UNNotificationTrigger? { get }
```

## Discussion

For notifications that the system has delivered, use this property to determine what caused the delivery to occur. For remote notifications, this property contains a [UNPushNotificationTrigger](../unpushnotificationtrigger.md) object. For other notifications, the system sets this type using the trigger condition specified in the original request.

## See Also

### Getting the Request Details

- [identifier](identifier.md) — The unique identifier for this notification request.
- [content](content.md) — The content associated with the notification.
