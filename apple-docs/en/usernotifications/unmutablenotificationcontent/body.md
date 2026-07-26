---
title: body
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/body
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/body'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/body.json'
content_hash: 'sha256:6ce0dd464fc03837'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# body

<sub>Instance Property</sub>

The localized text that provides the notification’s main content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var body: String { get set }
```

## Discussion

Use this property to specify the body of the notification alert. If your app isn’t authorized to display alert-based notifications, the system ignores this property.

The body text should contain the final text that you want to display, and shouldn’t contain any placeholder characters. To include a percent symbol (`%`) in the message body, use two percent symbols (`%%`). The system strips all other printf style escape characters from your string prior to display.

## See Also

### Providing the primary content

- [title](title.md) — The localized text that provides the notification’s primary description.
- [subtitle](subtitle.md) — The localized text that provides the notification’s secondary description.
