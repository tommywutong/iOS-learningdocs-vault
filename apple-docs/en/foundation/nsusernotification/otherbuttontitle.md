---
title: otherButtonTitle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/otherbuttontitle
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/otherbuttontitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/otherbuttontitle.json'
content_hash: 'sha256:f087a79d2e2938b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# otherButtonTitle

<sub>Instance Property</sub>

Specifies a custom title for the close button in an alert-style notification.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var otherButtonTitle: String { get set }
```

## Discussion

This value should be localized as it is presented to the user. The string is truncated to a length appropriate for display and the property is modified to reflect the truncation.

An empty string will cause the default localized text to be used. A `nil` value is invalid.

## See Also

### Displayed Notification Buttons

- [hasActionButton](hasactionbutton.md) — A Boolean value that specifies whether the notification displays an action button. _(deprecated)_
- [actionButtonTitle](actionbuttontitle.md) — Specifies the title of the action button displayed in the notification. _(deprecated)_
- [hasReplyButton](hasreplybutton.md) — A Boolean value that specifies whether the notification displays a reply button. _(deprecated)_
