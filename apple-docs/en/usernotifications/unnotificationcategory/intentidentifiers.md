---
title: intentIdentifiers
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcategory/intentidentifiers
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcategory/intentidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcategory/intentidentifiers.json'
content_hash: 'sha256:d29bb276f2c3e5cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationCategory](../unnotificationcategory.md)

# intentIdentifiers

<sub>Instance Property</sub>

The intents related to notifications of this category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var intentIdentifiers: [String] { get }
```

## Discussion

When the system delivers a notification, the presence of an intent identifier lets the system know that the notification is potentially related to the handling of a request made through Siri.

## See Also

### Getting the Information

- [identifier](identifier.md) — The unique string assigned to the category.
- [actions](actions.md) — The actions to display when the system delivers notifications of this type.
- [hiddenPreviewsBodyPlaceholder](hiddenpreviewsbodyplaceholder.md) — The placeholder text to display when the system disables notification previews for the app.
- [categorySummaryFormat](categorysummaryformat.md) — A format string for the summary description used when the system groups the category’s notifications.
