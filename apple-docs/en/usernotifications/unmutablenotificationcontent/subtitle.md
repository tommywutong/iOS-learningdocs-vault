---
title: subtitle
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/subtitle
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/subtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/subtitle.json'
content_hash: 'sha256:54f0dc2cb1151028'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# subtitle

<sub>Instance Property</sub>

The localized text that provides the notification’s secondary description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var subtitle: String { get set }
```

## Discussion

Use this property to specify additional context about the purpose of the notification. Subtitles offer additional context in cases where the title alone isn’t clear. Subtitles aren’t displayed in all cases. If your app isn’t authorized to display alert-based notifications, the system ignores this property.

## See Also

### Providing the primary content

- [title](title.md) — The localized text that provides the notification’s primary description.
- [body](body.md) — The localized text that provides the notification’s main content.
