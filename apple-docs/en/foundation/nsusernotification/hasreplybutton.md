---
title: hasReplyButton
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/hasreplybutton
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/hasreplybutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/hasreplybutton.json'
content_hash: 'sha256:72216a3baa2c63fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# hasReplyButton

<sub>Instance Property</sub>

A Boolean value that specifies whether the notification displays a reply button.

<sub>macOS</sub>

```swift
var hasReplyButton: Bool { get set }
```

## Discussion

Set to [true](../../swift/true.md) if the notification has a reply button. The default value is [false](../../swift/false.md). If this property and [hasActionButton](hasactionbutton.md) are both [true](../../swift/true.md), the reply button is shown.

## See Also

### Displayed Notification Buttons

- [hasActionButton](hasactionbutton.md) — A Boolean value that specifies whether the notification displays an action button. _(deprecated)_
- [actionButtonTitle](actionbuttontitle.md) — Specifies the title of the action button displayed in the notification. _(deprecated)_
- [otherButtonTitle](otherbuttontitle.md) — Specifies a custom title for the close button in an alert-style notification. _(deprecated)_
