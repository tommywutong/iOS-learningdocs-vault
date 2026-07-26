---
title: selectionDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstableview/selectiondidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nstableview/selectiondidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstableview/selectiondidchangenotification.json'
content_hash: 'sha256:0af0923760e760db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTableView](../nstableview.md)

# selectionDidChangeNotification

<sub>Type Property</sub>

Posted after an `NSTableView` object’s selection changes.

<sub>macOS</sub>

```swift
class let selectionDidChangeNotification: NSNotification.Name
```

## Discussion

The notification object is the table view whose selection changed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [SelectionDidChangeMessage](selectiondidchangemessage.md).

## See Also

### Notifications

- [NSTableViewColumnDidMoveNotification](columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSTableView` object.
- [NSTableViewColumnDidResizeNotification](columndidresizenotification.md) — Posted whenever a column is resized in an `NSTableView` object.
- [NSTableViewSelectionIsChangingNotification](selectionischangingnotification.md) — Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).
