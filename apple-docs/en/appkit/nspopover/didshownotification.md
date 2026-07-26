---
title: didShowNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nspopover/didshownotification
source_url: 'https://developer.apple.com/documentation/appkit/nspopover/didshownotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nspopover/didshownotification.json'
content_hash: 'sha256:e512086123c955e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSPopover](../nspopover.md)

# didShowNotification

<sub>Type Property</sub>

Sent after the popover has finished animating onscreen.

<sub>macOS</sub>

```swift
class let didShowNotification: NSNotification.Name
```

## Discussion

To observe this notification using Swift concurrency, use [DidShowMessage](didshowmessage.md).

## See Also

### Notifications

- [NSPopoverWillShowNotification](willshownotification.md) — Sent before the popover is shown.
- [NSPopoverWillCloseNotification](willclosenotification.md) — Sent before the popover is closed.
- [NSPopoverDidCloseNotification](didclosenotification.md) — Sent after the popover has finished animating offscreen.
