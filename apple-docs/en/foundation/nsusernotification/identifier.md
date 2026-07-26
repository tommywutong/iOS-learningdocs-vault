---
title: identifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotification/identifier
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotification/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotification/identifier.json'
content_hash: 'sha256:adc28a0c7fe3999d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotification](../nsusernotification.md)

# identifier

<sub>Instance Property</sub>

A string that uniquely identifies a notification.

<sub>macOS</sub>

```swift
var identifier: String? { get set }
```

## Discussion

The identifier is unique to a notification. A notification delivered with the same identifier as an existing notification replaces the existing notification rather than causing the display of a new notification.

## See Also

### Display Information

- [title](title.md) — Specifies the title of the notification. _(deprecated)_
- [subtitle](subtitle.md) — Specifies the subtitle of the notification. _(deprecated)_
- [informativeText](informativetext.md) — The body text of the notification. _(deprecated)_
- [contentImage](contentimage.md) — Image shown in the content of the notification. _(deprecated)_
- [response](response.md) — The response with which the user responded to a notification. _(deprecated)_
- [responsePlaceholder](responseplaceholder.md) — Optional placeholder string for inline reply field. _(deprecated)_
