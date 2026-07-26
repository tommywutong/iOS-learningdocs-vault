---
title: title
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationaction/title
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationaction/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationaction/title.json'
content_hash: 'sha256:a83d3969d980317d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationAction](../unnotificationaction.md)

# title

<sub>Instance Property</sub>

The localized string to use as the title of the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var title: String { get }
```

## Discussion

The system displays this string as the title of the button that the user taps or selects in the notification interface.

## See Also

### Getting Information

- [identifier](identifier.md) — The unique string that your app uses to identify the action.
- [icon](icon.md) — The icon associated with the action.
