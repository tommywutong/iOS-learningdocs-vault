---
title: additionalActivationAction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/additionalactivationaction
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/additionalactivationaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/additionalactivationaction.json'
content_hash: 'sha256:9c64b75ff42c0337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# additionalActivationAction

<sub>Instance Property</sub>

An additional action selected by the user.

<sub>macOS</sub>

```swift
@NSCopying var additionalActivationAction: NSUserNotificationAction? { get }
```

## Discussion

This property specifies an additional action selected by the user when the user notification is sent to to the [NSUserNotificationCenterDelegate](../nsusernotificationcenterdelegate.md) method [- userNotificationCenter:didActivateNotification:](<../nsusernotificationcenterdelegate/usernotificationcenter(__didactivate_).md>). The supported values are described in [ActivationType](activationtype-swift.enum.md).

## See Also

### User Notification Activation Method

- [activationType](activationtype-swift.property.md) — Specifies what caused a user notification to occur. _(deprecated)_
- [additionalActions](additionalactions.md) — The actions that can be taken on a notification in addition to the default action. _(deprecated)_
