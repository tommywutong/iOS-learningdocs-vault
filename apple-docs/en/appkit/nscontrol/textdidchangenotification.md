---
title: textDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscontrol/textdidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nscontrol/textdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscontrol/textdidchangenotification.json'
content_hash: 'sha256:41c307d9f54f0ace'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSControl](../nscontrol.md)

# textDidChangeNotification

<sub>Type Property</sub>

Sent when the text in the receiving control changes.

<sub>macOS</sub>

```swift
class let textDidChangeNotification: NSNotification.Name
```

## Discussion

The field editor of the edited cell originally sends an [NSTextDidChangeNotification](../nstext/didchangenotification.md) to the control, which passes it on in this form to its delegate. The notification object is the `NSControl` object posting the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `“NSFieldEditor”` | The edited cell’s field editor |

See the [controlTextDidChange:](../../objectivec/nsobject-swift.class/controltextdidchange_.md) method for details. The system posts this notification on the main actor.

To observe this notification using Swift concurrency, use [TextDidChangeMessage](textdidchangemessage.md).

## See Also

### Control-Editing Notifications

- [NSControlTextDidBeginEditingNotification](textdidbegineditingnotification.md) — Sent when a control with editable cells begins an edit session.
- [NSControlTextDidEndEditingNotification](textdidendeditingnotification.md) — Sent when a control with editable cells ends an editing session.
