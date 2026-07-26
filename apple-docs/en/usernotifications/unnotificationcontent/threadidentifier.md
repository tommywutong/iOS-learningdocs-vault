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
doc_path: /documentation/usernotifications/unnotificationcontent/threadidentifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/threadidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/threadidentifier.json'
content_hash: 'sha256:c45d2c36327579ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# threadIdentifier

<sub>Instance Property</sub>

The identifier that groups related notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var threadIdentifier: String { get }
```

## Discussion

For remote notifications, the system sets this property to the value of the `thread-id` key in the `aps` dictionary.

## See Also

### Retrieving group information

- [categoryIdentifier](categoryidentifier.md) — The identifier of the notification’s category.
- [summaryArgument](summaryargument.md) — The text the system adds to the notification summary to provide additional context. _(deprecated)_
- [summaryArgumentCount](summaryargumentcount.md) — The number the system adds to the notification summary when the notification represents multiple items. _(deprecated)_
