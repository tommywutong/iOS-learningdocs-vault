---
title: subtitle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/subtitle
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/subtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/subtitle.json'
content_hash: 'sha256:9d50ba41a0e2fba6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# subtitle

<sub>Instance Property</sub>

Specifies the subtitle of the notification.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
var subtitle: String? { get set }
```

## Discussion

This value should be localized as it is presented to the user. The string is truncated to a length appropriate for display and the property is modified to reflect the truncation.

## See Also

### Display Information

- [title](title.md) — Specifies the title of the notification. _(deprecated)_
- [informativeText](informativetext.md) — The body text of the notification. _(deprecated)_
- [contentImage](contentimage.md) — Image shown in the content of the notification. _(deprecated)_
- [identifier](identifier.md) — A string that uniquely identifies a notification. _(deprecated)_
- [response](response.md) — The response with which the user responded to a notification. _(deprecated)_
- [responsePlaceholder](responseplaceholder.md) — Optional placeholder string for inline reply field. _(deprecated)_
