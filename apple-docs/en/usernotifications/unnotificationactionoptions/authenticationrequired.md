---
title: authenticationRequired
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationactionoptions/authenticationrequired
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions/authenticationrequired'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationactionoptions/authenticationrequired.json'
content_hash: 'sha256:bd29988c3a0636ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationActionOptions](../unnotificationactionoptions.md)

# authenticationRequired

<sub>Type Property</sub>

The action can be performed only on an unlocked device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static var authenticationRequired: UNNotificationActionOptions { get }
```

## Discussion

When the user selects an action with this option, the system prompts the user to unlock the device. After unlocking, the system notifies your app of the selected action. You might use option to perform actions that require accessing data that is encrypted while the device is locked.

## See Also

### Constants

- [UNNotificationActionOptionDestructive](destructive.md) — The action performs a destructive task.
- [UNNotificationActionOptionForeground](foreground.md) — The action causes the app to launch in the foreground.
