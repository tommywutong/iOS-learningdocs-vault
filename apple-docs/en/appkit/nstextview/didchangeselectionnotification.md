---
title: didChangeSelectionNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextview/didchangeselectionnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstextview/didchangeselectionnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextview/didchangeselectionnotification.json'
content_hash: 'sha256:ff8d5dd66da8521e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextView](../nstextview.md)

# didChangeSelectionNotification

<sub>Type Property</sub>

Posted when the selected range of characters changes.

<sub>macOS</sub>

```swift
class let didChangeSelectionNotification: NSNotification.Name
```

## Discussion

`NSTextView` posts this notification whenever [- setSelectedRange:affinity:stillSelecting:](<setselectedrange(__affinity_stillselecting_).md>) is invoked, either directly or through the many methods ([- mouseDown:](<../nsresponder/mousedown(with_).md>), [- selectAll:](<../nstext/selectall(__).md>), and so on) that invoke it indirectly. When the user is selecting text, this notification is posted only once, at the end of the selection operation. The text view’s delegate receives a [- textViewDidChangeSelection:](<../nstextviewdelegate/textviewdidchangeselection(__).md>) message when this notification is posted.

The notification object is the notifying text view. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `@"NSOldSelectedCharacterRange"` | An `NSValue` object containing an `NSRange` structure with the originally selected range. |

To observe this notification using Swift concurrency, use [DidChangeSelectionMessage](didchangeselectionmessage.md).

## See Also

### Notifications

- [NSTextViewWillChangeNotifyingTextViewNotification](willchangenotifyingtextviewnotification.md) — Posted when a new text view is established as the text view that sends notifications.
- [NSTextViewDidChangeTypingAttributesNotification](didchangetypingattributesnotification.md) — Posted when there is a change in the typing attributes within a text view.
- [NSTextViewDidSwitchToNSLayoutManagerNotification](didswitchtonslayoutmanagernotification.md) — Posted by the framework after switching to using the compatibility mode layout manager.
- [NSTextViewWillSwitchToNSLayoutManagerNotification](willswitchtonslayoutmanagernotification.md) — Posted by the framework before switching to the compatibility mode layout manager.
