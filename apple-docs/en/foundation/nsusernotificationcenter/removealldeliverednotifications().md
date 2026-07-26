---
title: removeAllDeliveredNotifications()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotificationcenter/removealldeliverednotifications()
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenter/removealldeliverednotifications()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenter/removealldeliverednotifications%28%29.json'
content_hash: 'sha256:8774c76140619cea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenter](../nsusernotificationcenter.md)

# removeAllDeliveredNotifications()

<sub>Instance Method</sub>

Remove all delivered user notifications from the user notification center.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
func removeAllDeliveredNotifications()
```

## See Also

### Managing the Delivered Notifications

- [- deliverNotification:](<deliver(__).md>) — Deliver the specified user notification. _(deprecated)_
- [deliveredNotifications](deliverednotifications.md) — An array of all user notifications delivered to the notification center. _(deprecated)_
- [- removeDeliveredNotification:](<removedeliverednotification(__).md>) — Remove a delivered user notification from the user notification center. _(deprecated)_
