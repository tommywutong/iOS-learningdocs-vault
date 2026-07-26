---
title: additionalActions
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/additionalactions
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/additionalactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/additionalactions.json'
content_hash: 'sha256:52a3cbb3e204d1ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# additionalActions

<sub>Instance Property</sub>

The actions that can be taken on a notification in addition to the default action.

<sub>macOS</sub>

```swift
var additionalActions: [NSUserNotificationAction]? { get set }
```

## Discussion

This array contains `NSUserNotificationAction` objects that describe the different actions for a notification in addition to the default action described by [actionButtonTitle](actionbuttontitle.md).

## See Also

### Related Documentation

- [otherButtonTitle](otherbuttontitle.md) — Specifies a custom title for the close button in an alert-style notification. _(deprecated)_
- [actionButtonTitle](actionbuttontitle.md) — Specifies the title of the action button displayed in the notification. _(deprecated)_

### User Notification Activation Method

- [activationType](activationtype-swift.property.md) — Specifies what caused a user notification to occur. _(deprecated)_
- [additionalActivationAction](additionalactivationaction.md) — An additional action selected by the user. _(deprecated)_
