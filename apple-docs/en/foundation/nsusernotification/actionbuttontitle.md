---
title: actionButtonTitle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/actionbuttontitle
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/actionbuttontitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/actionbuttontitle.json'
content_hash: 'sha256:8557b204e38c6861'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# actionButtonTitle

<sub>Instance Property</sub>

Specifies the title of the action button displayed in the notification.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var actionButtonTitle: String { get set }
```

## Discussion

This value should be localized as it is presented to the user. The string is truncated to a length appropriate for display and the property is modified to reflect the truncation.

## See Also

### Displayed Notification Buttons

- [hasActionButton](hasactionbutton.md) — A Boolean value that specifies whether the notification displays an action button. _(deprecated)_
- [otherButtonTitle](otherbuttontitle.md) — Specifies a custom title for the close button in an alert-style notification. _(deprecated)_
- [hasReplyButton](hasreplybutton.md) — A Boolean value that specifies whether the notification displays a reply button. _(deprecated)_
