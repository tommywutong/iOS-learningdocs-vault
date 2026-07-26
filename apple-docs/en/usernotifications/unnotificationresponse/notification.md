---
title: notification
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationresponse/notification
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationresponse/notification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationresponse/notification.json'
content_hash: 'sha256:d4d18004a16750a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationResponse](../unnotificationresponse.md)

# notification

<sub>Instance Property</sub>

The notification to which the user responded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@NSCopying var notification: UNNotification { get }
```

## See Also

### Getting the Response Information

- [actionIdentifier](actionidentifier.md) — The identifier string of the action that the user selected.
- [targetScene](targetscene.md) — The scene where the system reflects the user’s response to a notification.
- [UNNotificationDefaultActionIdentifier](../unnotificationdefaultactionidentifier.md) — An action that indicates the user opened the app from the notification interface.
- [UNNotificationDismissActionIdentifier](../unnotificationdismissactionidentifier.md) — The action that indicates the user explicitly dismissed the notification interface.
