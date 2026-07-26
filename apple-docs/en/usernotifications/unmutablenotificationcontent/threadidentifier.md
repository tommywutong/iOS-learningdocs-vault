---
title: threadIdentifier
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/threadidentifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/threadidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/threadidentifier.json'
content_hash: 'sha256:516d203dbe31f281'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# threadIdentifier

<sub>Instance Property</sub>

The identifier that groups related notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var threadIdentifier: String { get set }
```

## Discussion

You may specify any value for the string, but assign the same thread identifier string to all notifications that you want to group together visually.

## See Also

### Grouping notifications

- [categoryIdentifier](categoryidentifier.md) — The identifier of the notification’s category.
- [summaryArgument](summaryargument.md) — The text the system adds to the notification summary to provide additional context. _(deprecated)_
- [summaryArgumentCount](summaryargumentcount.md) — The number the system adds to the notification summary when the notification represents multiple items. _(deprecated)_
