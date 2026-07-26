---
title: selectionIsChangingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstableview/selectionischangingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstableview/selectionischangingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstableview/selectionischangingnotification.json'
content_hash: 'sha256:a0796ab3a9f8c680'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTableView](../nstableview.md)

# selectionIsChangingNotification

<sub>Type Property</sub>

Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).

<sub>macOS</sub>

```swift
class let selectionIsChangingNotification: NSNotification.Name
```

## Discussion

Note that the notification is sent only for mouse events that change the table’s selection, not keyboard events. The notification object is the table view whose selection is changing. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [SelectionIsChangingMessage](selectionischangingmessage.md).

## See Also

### Notifications

- [NSTableViewColumnDidMoveNotification](columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSTableView` object.
- [NSTableViewColumnDidResizeNotification](columndidresizenotification.md) — Posted whenever a column is resized in an `NSTableView` object.
- [NSTableViewSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after an `NSTableView` object’s selection changes.
