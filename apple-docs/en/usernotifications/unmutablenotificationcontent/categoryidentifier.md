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
doc_path: /documentation/usernotifications/unmutablenotificationcontent/categoryidentifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/categoryidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/categoryidentifier.json'
content_hash: 'sha256:e758ca3c5baf2377'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# categoryIdentifier

<sub>Instance Property</sub>

The identifier of the notification’s category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var categoryIdentifier: String { get set }
```

## Discussion

Use notification types to distinguish between the different types of notifications your app supports. You use this support primarily to create actionable notifications with custom action buttons to redirect your notifications through either your notification service app extension or your notification content app extension.

Assign a value to this property that matches the [identifier](../unnotificationcategory/identifier.md) property of one of the [UNNotificationCategory](../unnotificationcategory.md) objects you previously registered with your app. If you assign a string that doesn’t match one of your registered categories, the system displays your notification without custom actions and without routing it through your app extensions.

## See Also

### Grouping notifications

- [threadIdentifier](threadidentifier.md) — The identifier that groups related notifications.
- [summaryArgument](summaryargument.md) — The text the system adds to the notification summary to provide additional context. _(deprecated)_
- [summaryArgumentCount](summaryargumentcount.md) — The number the system adds to the notification summary when the notification represents multiple items. _(deprecated)_
