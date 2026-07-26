---
title: textDidEndEditingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscontrol/textdidendeditingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nscontrol/textdidendeditingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscontrol/textdidendeditingnotification.json'
content_hash: 'sha256:bc1ef1d75d2df31a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSControl](../nscontrol.md)

# textDidEndEditingNotification

<sub>Type Property</sub>

Sent when a control with editable cells ends an editing session.

<sub>macOS</sub>

```swift
class let textDidEndEditingNotification: NSNotification.Name
```

## Discussion

The field editor of the edited cell originally sends an [NSControlTextDidEndEditingNotification](textdidendeditingnotification.md) to the control, which passes it on in this form to its delegate. The notification object is the `NSControl` object posting the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `“NSFieldEditor”` | The edited cell’s field editor |

See the [controlTextDidEndEditing:](../../objectivec/nsobject-swift.class/controltextdidendediting_.md) method for details. The system posts this notification on the main actor.

To observe this notification using Swift concurrency, use [TextDidEndEditingMessage](textdidendeditingmessage.md).

## See Also

### Control-Editing Notifications

- [NSControlTextDidBeginEditingNotification](textdidbegineditingnotification.md) — Sent when a control with editable cells begins an edit session.
- [NSControlTextDidChangeNotification](textdidchangenotification.md) — Sent when the text in the receiving control changes.
