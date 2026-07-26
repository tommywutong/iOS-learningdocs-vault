---
title: badge
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiremotenotificationtype/badge
source_url: 'https://developer.apple.com/documentation/uikit/uiremotenotificationtype/badge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiremotenotificationtype/badge.json'
content_hash: 'sha256:72fbc7653ad6cbee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRemoteNotificationType](../uiremotenotificationtype.md)

# badge

<sub>Type Property</sub>

The app accepts notifications that badge the app icon.

> [!warning] Deprecated
> Use [requestAuthorization(options:completionHandler:)](<../../usernotifications/unusernotificationcenter/requestauthorization(options_completionhandler_).md>) and [setNotificationCategories(_:)](<../../usernotifications/unusernotificationcenter/setnotificationcategories(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var badge: UIRemoteNotificationType { get }
```

## See Also

### Constants

- [UIRemoteNotificationTypeSound](sound.md) — The app accepts alert sounds as notifications. _(deprecated)_
- [UIRemoteNotificationTypeAlert](alert.md) — The app accepts alert messages as notifications. _(deprecated)_
- [UIRemoteNotificationTypeNewsstandContentAvailability](newsstandcontentavailability.md) — The app accepts notifications that start the downloading of issue assets for Newsstand apps. _(deprecated)_
