---
title: announcement
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+（15.0 起废弃）, iPadOS 13.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 6.0+（7.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/usernotifications/unauthorizationoptions/announcement
source_url: 'https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/announcement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unauthorizationoptions/announcement.json'
content_hash: 'sha256:4b6d3b31e9d04617'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNAuthorizationOptions](../unauthorizationoptions.md)

# announcement

<sub>Type Property</sub>

The ability for Siri to automatically read out messages over AirPods.

> [!warning] Deprecated
> Announcement authorization is always included

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
static var announcement: UNAuthorizationOptions { get }
```

## See Also

### Deprecated

- [UNAuthorizationOptionTimeSensitive](timesensitive.md) _(deprecated)_
