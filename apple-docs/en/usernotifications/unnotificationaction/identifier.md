---
title: identifier
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationaction/identifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationaction/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationaction/identifier.json'
content_hash: 'sha256:ee4d1865aac73561'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationAction](../unnotificationaction.md)

# identifier

<sub>Instance Property</sub>

The unique string that your app uses to identify the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var identifier: String { get }
```

## Discussion

When the user selects an action, the system reports the value of this string to your app. Because your app handles all actions by using a single delegate method, the identifier strings for all of your app’s actions must be unique.

## See Also

### Getting Information

- [title](title.md) — The localized string to use as the title of the action.
- [icon](icon.md) — The icon associated with the action.
