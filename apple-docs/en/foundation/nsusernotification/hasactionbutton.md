---
title: hasActionButton
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/hasactionbutton
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/hasactionbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/hasactionbutton.json'
content_hash: 'sha256:5e861f7d745effb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# hasActionButton

<sub>Instance Property</sub>

A Boolean value that specifies whether the notification displays an action button.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var hasActionButton: Bool { get set }
```

## Discussion

Set to [false](../../swift/false.md) if the notification has no action button. This is the case for notifications that are purely for information and have no user action. The default value is [true](../../swift/true.md).

## See Also

### Displayed Notification Buttons

- [actionButtonTitle](actionbuttontitle.md) — Specifies the title of the action button displayed in the notification. _(deprecated)_
- [otherButtonTitle](otherbuttontitle.md) — Specifies a custom title for the close button in an alert-style notification. _(deprecated)_
- [hasReplyButton](hasreplybutton.md) — A Boolean value that specifies whether the notification displays a reply button. _(deprecated)_
