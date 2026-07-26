---
title: icon
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationaction/icon
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationaction/icon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationaction/icon.json'
content_hash: 'sha256:52fc073b2ce4e778'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationAction](../unnotificationaction.md)

# icon

<sub>Instance Property</sub>

The icon associated with the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@NSCopying var icon: UNNotificationActionIcon? { get }
```

## Discussion

The system displays this icon in the notification interface to help the user identify the app associated with the action.

## See Also

### Getting Information

- [identifier](identifier.md) — The unique string that your app uses to identify the action.
- [title](title.md) — The localized string to use as the title of the action.
