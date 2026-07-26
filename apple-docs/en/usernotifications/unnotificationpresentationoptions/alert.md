---
title: alert
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+（14.0 起废弃）, iPadOS 10.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.14+（11.0 起废弃）, tvOS 10.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 3.0+（7.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/usernotifications/unnotificationpresentationoptions/alert
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions/alert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationpresentationoptions/alert.json'
content_hash: 'sha256:639352ac80d0153b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationPresentationOptions](../unnotificationpresentationoptions.md)

# alert

<sub>Type Property</sub>

Display the alert using the content provided by the notification.

> [!warning] Deprecated
> Use [UNNotificationPresentationOptionList](list.md) and [UNNotificationPresentationOptionBanner](banner.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var alert: UNNotificationPresentationOptions { get }
```

## See Also

### Constants

- [UNNotificationPresentationOptionBadge](badge.md) — Apply the notification’s badge value to the app’s icon.
- [UNNotificationPresentationOptionBanner](banner.md) — Present the notification as a banner.
- [UNNotificationPresentationOptionList](list.md) — Show the notification in Notification Center.
- [UNNotificationPresentationOptionSound](sound.md) — Play the sound associated with the notification.
