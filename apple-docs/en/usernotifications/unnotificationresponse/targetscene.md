---
title: targetScene
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationresponse/targetscene
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationresponse/targetscene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationresponse/targetscene.json'
content_hash: 'sha256:56f690d570a5eded'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationResponse](../unnotificationresponse.md)

# targetScene

<sub>Instance Property</sub>

The scene where the system reflects the user’s response to a notification.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var targetScene: UIScene? { get }
```

## See Also

### Getting the Response Information

- [actionIdentifier](actionidentifier.md) — The identifier string of the action that the user selected.
- [notification](notification.md) — The notification to which the user responded.
- [UNNotificationDefaultActionIdentifier](../unnotificationdefaultactionidentifier.md) — An action that indicates the user opened the app from the notification interface.
- [UNNotificationDismissActionIdentifier](../unnotificationdismissactionidentifier.md) — The action that indicates the user explicitly dismissed the notification interface.
