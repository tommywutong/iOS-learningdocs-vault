---
title: categoryIdentifier
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcontent/categoryidentifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/categoryidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/categoryidentifier.json'
content_hash: 'sha256:0e8eca670fb64f31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# categoryIdentifier

<sub>Instance Property</sub>

The identifier of the notification’s category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var categoryIdentifier: String { get }
```

## Discussion

Use notification types to distinguish between the different types of notifications your app supports. You use this support primarily to create actionable notifications with custom action buttons, and to redirect your notifications through either your notification service app extension or your notification content app extension.

For remote notifications, the system sets this property to the value of the `category` key in the `aps` dictionary.

## See Also

### Retrieving group information

- [threadIdentifier](threadidentifier.md) — The identifier that groups related notifications.
- [summaryArgument](summaryargument.md) — The text the system adds to the notification summary to provide additional context. _(deprecated)_
- [summaryArgumentCount](summaryargumentcount.md) — The number the system adds to the notification summary when the notification represents multiple items. _(deprecated)_
