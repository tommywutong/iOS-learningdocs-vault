---
title: willShowNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nspopover/willshownotification
source_url: 'https://developer.apple.com/documentation/appkit/nspopover/willshownotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nspopover/willshownotification.json'
content_hash: 'sha256:bfa9ad58d73b98b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSPopover](../nspopover.md)

# willShowNotification

<sub>Type Property</sub>

Sent before the popover is shown.

<sub>macOS</sub>

```swift
class let willShowNotification: NSNotification.Name
```

## Discussion

To observe this notification using Swift concurrency, use [WillShowMessage](willshowmessage.md).

## See Also

### Notifications

- [NSPopoverDidShowNotification](didshownotification.md) — Sent after the popover has finished animating onscreen.
- [NSPopoverWillCloseNotification](willclosenotification.md) — Sent before the popover is closed.
- [NSPopoverDidCloseNotification](didclosenotification.md) — Sent after the popover has finished animating offscreen.
