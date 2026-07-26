---
title: badge
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationpresentationoptions/badge
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions/badge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationpresentationoptions/badge.json'
content_hash: 'sha256:ca42e685da70bb05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationPresentationOptions](../unnotificationpresentationoptions.md)

# badge

<sub>Type Property</sub>

Apply the notification’s badge value to the app’s icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var badge: UNNotificationPresentationOptions { get }
```

## See Also

### Constants

- [UNNotificationPresentationOptionBanner](banner.md) — Present the notification as a banner.
- [UNNotificationPresentationOptionList](list.md) — Show the notification in Notification Center.
- [UNNotificationPresentationOptionSound](sound.md) — Play the sound associated with the notification.
- [UNNotificationPresentationOptionAlert](alert.md) — Display the alert using the content provided by the notification. _(deprecated)_
