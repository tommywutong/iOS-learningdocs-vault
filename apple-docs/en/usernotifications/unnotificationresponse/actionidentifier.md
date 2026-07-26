---
title: actionIdentifier
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationresponse/actionidentifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationresponse/actionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationresponse/actionidentifier.json'
content_hash: 'sha256:978a30c643fbce1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationResponse](../unnotificationresponse.md)

# actionIdentifier

<sub>Instance Property</sub>

The identifier string of the action that the user selected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var actionIdentifier: String { get }
```

## Discussion

This parameter may contain one the identifier of one of your [UNNotificationAction](../unnotificationaction.md) objects or it may contain a system-defined identifier. The system defined identifiers are [UNNotificationDefaultActionIdentifier](../unnotificationdefaultactionidentifier.md) and [UNNotificationDismissActionIdentifier](../unnotificationdismissactionidentifier.md), which indicate that the user opened the app or dismissed the notification without any further actions.

For more information about defining custom actions, see [Declaring your actionable notification types](../declaring-your-actionable-notification-types.md).

## See Also

### Getting the Response Information

- [notification](notification.md) — The notification to which the user responded.
- [targetScene](targetscene.md) — The scene where the system reflects the user’s response to a notification.
- [UNNotificationDefaultActionIdentifier](../unnotificationdefaultactionidentifier.md) — An action that indicates the user opened the app from the notification interface.
- [UNNotificationDismissActionIdentifier](../unnotificationdismissactionidentifier.md) — The action that indicates the user explicitly dismissed the notification interface.
