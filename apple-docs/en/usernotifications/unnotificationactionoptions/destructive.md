---
title: destructive
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationactionoptions/destructive
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions/destructive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationactionoptions/destructive.json'
content_hash: 'sha256:0b2b909e7ef37e53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationActionOptions](../unnotificationactionoptions.md)

# destructive

<sub>Type Property</sub>

The action performs a destructive task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static var destructive: UNNotificationActionOptions { get }
```

## Discussion

Use this option for actions that delete user data or change the app irrevocably. The action button is displayed with special highlighting to indicate that it performs a destructive task.

## See Also

### Constants

- [UNNotificationActionOptionAuthenticationRequired](authenticationrequired.md) — The action can be performed only on an unlocked device.
- [UNNotificationActionOptionForeground](foreground.md) — The action causes the app to launch in the foreground.
