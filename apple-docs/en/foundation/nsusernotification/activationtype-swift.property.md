---
title: activationType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/activationtype-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/activationtype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/activationtype-swift.property.json'
content_hash: 'sha256:5ccc737ea4fb8ffd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# activationType

<sub>Instance Property</sub>

Specifies what caused a user notification to occur.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var activationType: NSUserNotification.ActivationType { get }
```

## Discussion

This property specifies why the user notification was sent to to the [NSUserNotificationCenterDelegate](../nsusernotificationcenterdelegate.md) method [- userNotificationCenter:didActivateNotification:](<../nsusernotificationcenterdelegate/usernotificationcenter(__didactivate_).md>). The supported values are described in [ActivationType](activationtype-swift.enum.md).

## See Also

### User Notification Activation Method

- [additionalActivationAction](additionalactivationaction.md) — An additional action selected by the user. _(deprecated)_
- [additionalActions](additionalactions.md) — The actions that can be taken on a notification in addition to the default action. _(deprecated)_
