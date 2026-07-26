---
title: didCloseNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nspopover/didclosenotification
source_url: 'https://developer.apple.com/documentation/appkit/nspopover/didclosenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nspopover/didclosenotification.json'
content_hash: 'sha256:5f1c3c9c7b786c15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSPopover](../nspopover.md)

# didCloseNotification

<sub>Type Property</sub>

Sent after the popover has finished animating offscreen.

<sub>macOS</sub>

```swift
class let didCloseNotification: NSNotification.Name
```

## Discussion

The value of the `userInfo` key [NSPopoverCloseReasonKey](closereasonuserinfokey.md) specifies the reason for closing. It can currently be either [NSPopoverCloseReasonStandard](closereason/standard.md) or [NSPopoverCloseReasonDetachToWindow](closereason/detachtowindow.md), although more reasons for closing may be added in the future.

To observe this notification using Swift concurrency, use [DidCloseMessage](didclosemessage.md).

## See Also

### Notifications

- [NSPopoverWillShowNotification](willshownotification.md) — Sent before the popover is shown.
- [NSPopoverDidShowNotification](didshownotification.md) — Sent after the popover has finished animating onscreen.
- [NSPopoverWillCloseNotification](willclosenotification.md) — Sent before the popover is closed.
