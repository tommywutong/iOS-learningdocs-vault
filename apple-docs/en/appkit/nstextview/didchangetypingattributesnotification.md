---
title: didChangeTypingAttributesNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextview/didchangetypingattributesnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstextview/didchangetypingattributesnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextview/didchangetypingattributesnotification.json'
content_hash: 'sha256:08b203c20a4ed25f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextView](../nstextview.md)

# didChangeTypingAttributesNotification

<sub>Type Property</sub>

Posted when there is a change in the typing attributes within a text view.

<sub>macOS</sub>

```swift
class let didChangeTypingAttributesNotification: NSNotification.Name
```

## Discussion

This notification is posted, via the [- textViewDidChangeTypingAttributes:](<../nstextviewdelegate/textviewdidchangetypingattributes(__).md>) delegate method, whether or not text has changed as a result of the attribute change.

To observe this notification using Swift concurrency, use [DidChangeTypingAttributesMessage](didchangetypingattributesmessage.md).

## See Also

### Notifications

- [NSTextViewDidChangeSelectionNotification](didchangeselectionnotification.md) — Posted when the selected range of characters changes.
- [NSTextViewWillChangeNotifyingTextViewNotification](willchangenotifyingtextviewnotification.md) — Posted when a new text view is established as the text view that sends notifications.
- [NSTextViewDidSwitchToNSLayoutManagerNotification](didswitchtonslayoutmanagernotification.md) — Posted by the framework after switching to using the compatibility mode layout manager.
- [NSTextViewWillSwitchToNSLayoutManagerNotification](willswitchtonslayoutmanagernotification.md) — Posted by the framework before switching to the compatibility mode layout manager.
