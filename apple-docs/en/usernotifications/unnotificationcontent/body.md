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
doc_path: /documentation/usernotifications/unnotificationcontent/body
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/body'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/body.json'
content_hash: 'sha256:080c0169c07f68ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# body

<sub>Instance Property</sub>

The localized text that provides the notification’s main content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var body: String { get }
```

## Discussion

The body text contains the final text that you want to display. If your app isn’t authorized to display alert-based notifications, the system ignores this property.

If you specified two percent symbols (`%%`) in the message body, the system replaces it with a single percent symbol (`%`). The system strips all other printf style escape characters from your string prior to display.

## See Also

### Accessing the primary content

- [title](title.md) — The localized text that provides the notification’s primary description.
- [subtitle](subtitle.md) — The localized text that provides the notification’s secondary description.
