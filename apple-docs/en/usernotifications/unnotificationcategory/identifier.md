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
doc_path: /documentation/usernotifications/unnotificationcategory/identifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcategory/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcategory/identifier.json'
content_hash: 'sha256:eaa45c58acf7b9d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationCategory](../unnotificationcategory.md)

# identifier

<sub>Instance Property</sub>

The unique string assigned to the category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var identifier: String { get }
```

## Discussion

Use this string to differentiate the different types of notifications that your app can send. To assign a category to a local notification, assign this string to the [categoryIdentifier](../unmutablenotificationcontent/categoryidentifier.md) property of the content object. To assign a category to a remote notification, use the string as the value of the `category` key in the notification payload `aps` dictionary.

## See Also

### Getting the Information

- [actions](actions.md) — The actions to display when the system delivers notifications of this type.
- [intentIdentifiers](intentidentifiers.md) — The intents related to notifications of this category.
- [hiddenPreviewsBodyPlaceholder](hiddenpreviewsbodyplaceholder.md) — The placeholder text to display when the system disables notification previews for the app.
- [categorySummaryFormat](categorysummaryformat.md) — A format string for the summary description used when the system groups the category’s notifications.
