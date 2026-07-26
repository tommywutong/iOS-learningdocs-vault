---
title: allowInCarPlay
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcategoryoptions/allowincarplay
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions/allowincarplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcategoryoptions/allowincarplay.json'
content_hash: 'sha256:bf768df85454bb5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationCategoryOptions](../unnotificationcategoryoptions.md)

# allowInCarPlay

<sub>Type Property</sub>

Allow CarPlay to display notifications of this type.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
static var allowInCarPlay: UNNotificationCategoryOptions { get }
```

## Discussion

Apps must be approved for CarPlay overall and then you must enable CarPlay for the notification types you want displayed. If a category doesn’t explicitly contain this option, notifications of that type aren’t displayed in a CarPlay environment.

## See Also

### Customizing a category

- [UNNotificationCategoryOptionAllowAnnouncement](allowannouncement.md) — An option that grants Siri permission to read incoming messages out loud when the user has a compatible audio output device connected. _(deprecated)_
