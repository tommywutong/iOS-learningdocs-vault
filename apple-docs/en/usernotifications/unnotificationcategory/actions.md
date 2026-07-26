---
title: actions
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcategory/actions
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcategory/actions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcategory/actions.json'
content_hash: 'sha256:b48131d10ba45f90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationCategory](../unnotificationcategory.md)

# actions

<sub>Instance Property</sub>

The actions to display when the system delivers notifications of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var actions: [UNNotificationAction] { get }
```

## Discussion

When displaying a notification assigned to this category, the system adds a button to the notification interface for each action in this property. The system displays these buttons after the notification’s content but before the Dismiss button.

When displaying banner notifications, the system displays only the first two actions.

## See Also

### Getting the Information

- [identifier](identifier.md) — The unique string assigned to the category.
- [intentIdentifiers](intentidentifiers.md) — The intents related to notifications of this category.
- [hiddenPreviewsBodyPlaceholder](hiddenpreviewsbodyplaceholder.md) — The placeholder text to display when the system disables notification previews for the app.
- [categorySummaryFormat](categorysummaryformat.md) — A format string for the summary description used when the system groups the category’s notifications.
