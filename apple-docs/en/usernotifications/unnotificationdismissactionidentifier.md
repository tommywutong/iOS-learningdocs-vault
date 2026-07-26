---
title: UNNotificationDismissActionIdentifier
framework: User Notifications
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationdismissactionidentifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationdismissactionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationdismissactionidentifier.json'
content_hash: 'sha256:682b5fff5abcc304'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationDismissActionIdentifier

<sub>Global Variable</sub>

The action that indicates the user explicitly dismissed the notification interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let UNNotificationDismissActionIdentifier: String
```

## Discussion

The system delivers this action only if your app configured the notification’s category object with the [UNNotificationCategoryOptionCustomDismissAction](unnotificationcategoryoptions/customdismissaction.md) option. To trigger this action, the user must explicitly dismiss the notification interface. For example, the user must tap the Dismiss button or swipe down on the notification interface in watchOS to trigger this action.

Ignoring a notification or flicking away a notification banner doesn’t trigger this action.

## See Also

### Getting the Response Information

- [actionIdentifier](unnotificationresponse/actionidentifier.md) — The identifier string of the action that the user selected.
- [notification](unnotificationresponse/notification.md) — The notification to which the user responded.
- [targetScene](unnotificationresponse/targetscene.md) — The scene where the system reflects the user’s response to a notification.
- [UNNotificationDefaultActionIdentifier](unnotificationdefaultactionidentifier.md) — An action that indicates the user opened the app from the notification interface.
