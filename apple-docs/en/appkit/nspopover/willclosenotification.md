---
title: willCloseNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nspopover/willclosenotification
source_url: 'https://developer.apple.com/documentation/appkit/nspopover/willclosenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nspopover/willclosenotification.json'
content_hash: 'sha256:59cd3d0fde684572'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSPopover](../nspopover.md)

# willCloseNotification

<sub>Type Property</sub>

Sent before the popover is closed.

<sub>macOS</sub>

```swift
class let willCloseNotification: NSNotification.Name
```

## Discussion

The `userInfo` key [NSPopoverCloseReasonKey](closereasonuserinfokey.md) specifies the reason for closing. It can currently be either [NSPopoverCloseReasonStandard](closereason/standard.md) or [NSPopoverCloseReasonDetachToWindow](closereason/detachtowindow.md), although more reasons for closing may be added in the future.

To observe this notification using Swift concurrency, use [WillCloseMessage](willclosemessage.md).

## See Also

### Notifications

- [NSPopoverWillShowNotification](willshownotification.md) — Sent before the popover is shown.
- [NSPopoverDidShowNotification](didshownotification.md) — Sent after the popover has finished animating onscreen.
- [NSPopoverDidCloseNotification](didclosenotification.md) — Sent after the popover has finished animating offscreen.
