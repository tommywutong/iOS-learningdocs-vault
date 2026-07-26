---
title: hiddenPreviewsBodyPlaceholder
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcategory/hiddenpreviewsbodyplaceholder
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcategory/hiddenpreviewsbodyplaceholder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcategory/hiddenpreviewsbodyplaceholder.json'
content_hash: 'sha256:915cf927e65ce073'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationCategory](../unnotificationcategory.md)

# hiddenPreviewsBodyPlaceholder

<sub>Instance Property</sub>

The placeholder text to display when the system disables notification previews for the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var hiddenPreviewsBodyPlaceholder: String { get }
```

## Discussion

The string in this property may contain the special characters `%u` as a placeholder for the number of messages with the same thread identifier. If your app declares this string in a `.stringsdict` property list, the system formats the preview message using the information in that file. For more information about specifying a `.stringsdict` property file, see [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

## See Also

### Getting the Information

- [identifier](identifier.md) — The unique string assigned to the category.
- [actions](actions.md) — The actions to display when the system delivers notifications of this type.
- [intentIdentifiers](intentidentifiers.md) — The intents related to notifications of this category.
- [categorySummaryFormat](categorysummaryformat.md) — A format string for the summary description used when the system groups the category’s notifications.
