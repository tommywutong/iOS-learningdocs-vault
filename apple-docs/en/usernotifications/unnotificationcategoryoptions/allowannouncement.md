---
title: allowAnnouncement
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+（15.0 起废弃）, iPadOS 13.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 6.0+（7.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/usernotifications/unnotificationcategoryoptions/allowannouncement
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions/allowannouncement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcategoryoptions/allowannouncement.json'
content_hash: 'sha256:9075a5f023a46321'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationCategoryOptions](../unnotificationcategoryoptions.md)

# allowAnnouncement

<sub>Type Property</sub>

An option that grants Siri permission to read incoming messages out loud when the user has a compatible audio output device connected.

> [!warning] Deprecated
> Announcement option is ignored

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
static var allowAnnouncement: UNNotificationCategoryOptions { get }
```

## Discussion

When Siri reads an incoming message to the user, Siri reads the message locally on the userʼs device. Siri doesn’t send the message’s contents or sender to Apple servers. For more information about Siri’s on-device processing, visit [Apple’s Privacy Page](https://www.apple.com/privacy/features/).

## See Also

### Customizing a category

- [UNNotificationCategoryOptionAllowInCarPlay](allowincarplay.md) — Allow CarPlay to display notifications of this type.
