---
title: 'init(identifier:actions:intentIdentifiers:options:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationcategory/init(identifier:actions:intentidentifiers:options:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcategory/init(identifier:actions:intentidentifiers:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcategory/init%28identifier%3Aactions%3Aintentidentifiers%3Aoptions%3A%29.json'
content_hash: 'sha256:7be5088122bd28e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationCategory](../unnotificationcategory.md)

# init(identifier:actions:intentIdentifiers:options:)

<sub>Initializer</sub>

Creates a category object containing the specified actions and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], options: UNNotificationCategoryOptions = [])
```

## Parameters

- `identifier` — The unique identifier for the category. Each category that your app uses must have a unique identifier. Don’t specify an empty string.

- `actions` — The actions to display when the system delivers notifications of this type. When minimal space is available, the system displays only the first two actions in the array. You may specify an empty array for this parameter if you don’t want to display custom actions.

- `intentIdentifiers` — The intent identifier strings that you want to associate with notifications of this type. The Intents framework defines constants for each type of intent that you can associate with your notifications.

- `options` — Additional options for handling notifications of this type. For a list of possible values, see [UNNotificationCategoryOptions](../unnotificationcategoryoptions.md).

## Return Value

An initialized category object.

## See Also

### Essentials

- [+ categoryWithIdentifier:actions:intentIdentifiers:hiddenPreviewsBodyPlaceholder:options:](<init(identifier_actions_intentidentifiers_hiddenpreviewsbodyplaceholder_options_).md>) — Creates a category object containing the specified actions, options, and placeholder text used when previews aren’t shown.
- [+ categoryWithIdentifier:actions:intentIdentifiers:hiddenPreviewsBodyPlaceholder:categorySummaryFormat:options:](<init(identifier_actions_intentidentifiers_hiddenpreviewsbodyplaceholder_categorysummaryformat_options_).md>) — Creates a category object containing the specified actions, options, placeholder text used when previews aren’t shown, and summary format string.
