---
title: response
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/response
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/response'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/response.json'
content_hash: 'sha256:1c036d1f02fc262a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# response

<sub>Instance Property</sub>

The response with which the user responded to a notification.

<sub>macOS</sub>

```swift
@NSCopying var response: NSAttributedString? { get }
```

## Discussion

When the user responds to a notification, the [NSUserNotificationCenterDelegate](../nsusernotificationcenterdelegate.md) method [- userNotificationCenter:didActivateNotification:](<../nsusernotificationcenterdelegate/usernotificationcenter(__didactivate_).md>) is called with the notification, the [activationType](activationtype-swift.property.md) property set to [NSUserNotificationActivationTypeReplied](activationtype-swift.enum/replied.md), and this property is set with the user’s response.

## See Also

### Display Information

- [title](title.md) — Specifies the title of the notification. _(deprecated)_
- [subtitle](subtitle.md) — Specifies the subtitle of the notification. _(deprecated)_
- [informativeText](informativetext.md) — The body text of the notification. _(deprecated)_
- [contentImage](contentimage.md) — Image shown in the content of the notification. _(deprecated)_
- [identifier](identifier.md) — A string that uniquely identifies a notification. _(deprecated)_
- [responsePlaceholder](responseplaceholder.md) — Optional placeholder string for inline reply field. _(deprecated)_
