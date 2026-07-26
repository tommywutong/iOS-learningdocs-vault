---
title: title
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/title
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/title.json'
content_hash: 'sha256:7286e3035727e236'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# title

<sub>Instance Property</sub>

The localized text that provides the notification’s primary description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var title: String { get set }
```

## Discussion

Use this property to specify the title of your notification alert. If your app isn’t authorized to display alert-based notifications, the system ignores this property.

Title strings should be short, usually only a couple of words describing the reason for the notification. In watchOS, the system displays the title string as part of the short look notification interface, which has limited space.

## See Also

### Providing the primary content

- [subtitle](subtitle.md) — The localized text that provides the notification’s secondary description.
- [body](body.md) — The localized text that provides the notification’s main content.
