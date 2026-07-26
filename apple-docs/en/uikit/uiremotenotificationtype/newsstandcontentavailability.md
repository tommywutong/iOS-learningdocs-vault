---
title: newsstandContentAvailability
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiremotenotificationtype/newsstandcontentavailability
source_url: 'https://developer.apple.com/documentation/uikit/uiremotenotificationtype/newsstandcontentavailability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiremotenotificationtype/newsstandcontentavailability.json'
content_hash: 'sha256:a13a62514e4634d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRemoteNotificationType](../uiremotenotificationtype.md)

# newsstandContentAvailability

<sub>Type Property</sub>

The app accepts notifications that start the downloading of issue assets for Newsstand apps.

> [!warning] Deprecated
> Use [requestAuthorization(options:completionHandler:)](<../../usernotifications/unusernotificationcenter/requestauthorization(options_completionhandler_).md>) and [setNotificationCategories(_:)](<../../usernotifications/unusernotificationcenter/setnotificationcategories(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var newsstandContentAvailability: UIRemoteNotificationType { get }
```

## See Also

### Constants

- [UIRemoteNotificationTypeBadge](badge.md) — The app accepts notifications that badge the app icon. _(deprecated)_
- [UIRemoteNotificationTypeSound](sound.md) — The app accepts alert sounds as notifications. _(deprecated)_
- [UIRemoteNotificationTypeAlert](alert.md) — The app accepts alert messages as notifications. _(deprecated)_
