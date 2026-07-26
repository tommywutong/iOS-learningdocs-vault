---
title: NSUserNotificationCenterDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsusernotificationcenterdelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenterdelegate.json'
content_hash: 'sha256:8b62ca56e0cc815d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserNotificationCenterDelegate

<sub>Protocol</sub>

An interface that enables customizing the behavior of the default notification center.

<sub>Mac Catalyst, macOS</sub>

```swift
protocol NSUserNotificationCenterDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### User Notification Delivery Information

- [- userNotificationCenter:didDeliverNotification:](<nsusernotificationcenterdelegate/usernotificationcenter(__diddeliver_).md>) — Sent to the delegate when a notification delivery date has arrived. _(deprecated)_
- [- userNotificationCenter:didActivateNotification:](<nsusernotificationcenterdelegate/usernotificationcenter(__didactivate_).md>) — Sent to the delegate when a user clicks on a user notification presented by the user notification center. _(deprecated)_

### User Notification Display Override

- [- userNotificationCenter:shouldPresentNotification:](<nsusernotificationcenterdelegate/usernotificationcenter(__shouldpresent_).md>) — Sent to the delegate when the user notification center has decided not to present your notification. _(deprecated)_

## See Also

### User Notifications

- [NSUserNotification](nsusernotification.md) — A notification that can be scheduled for display in the notification center. _(deprecated)_
- [NSUserNotificationAction](nsusernotificationaction.md) — An action that the user can take in response to receiving a notification. _(deprecated)_
- [NSUserNotificationCenter](nsusernotificationcenter.md) — An object that delivers notifications from apps to the user. _(deprecated)_
