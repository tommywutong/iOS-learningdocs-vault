---
title: textDidBeginEditingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscontrol/textdidbegineditingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nscontrol/textdidbegineditingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscontrol/textdidbegineditingnotification.json'
content_hash: 'sha256:51e4a81d08a6f7b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSControl](../nscontrol.md)

# textDidBeginEditingNotification

<sub>Type Property</sub>

Sent when a control with editable cells begins an edit session.

<sub>macOS</sub>

```swift
class let textDidBeginEditingNotification: NSNotification.Name
```

## Discussion

The field editor of the edited cell originally sends an [NSTextDidBeginEditingNotification](../nstext/didbegineditingnotification.md) to the control, which passes it on in this form to its delegate. The notification object is the `NSControl` object posting the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `“NSFieldEditor”` | The edited cell’s field editor |

See the [controlTextDidEndEditing:](../../objectivec/nsobject-swift.class/controltextdidendediting_.md) method for details. The system posts this notification on the main actor.

To observe this notification using Swift concurrency, use [TextDidBeginEditingMessage](textdidbegineditingmessage.md).

## See Also

### Control-Editing Notifications

- [NSControlTextDidChangeNotification](textdidchangenotification.md) — Sent when the text in the receiving control changes.
- [NSControlTextDidEndEditingNotification](textdidendeditingnotification.md) — Sent when a control with editable cells ends an editing session.
