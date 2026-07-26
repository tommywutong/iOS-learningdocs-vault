---
title: columnDidResizeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstableview/columndidresizenotification
source_url: 'https://developer.apple.com/documentation/appkit/nstableview/columndidresizenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstableview/columndidresizenotification.json'
content_hash: 'sha256:6d2161b11fef3b96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTableView](../nstableview.md)

# columnDidResizeNotification

<sub>Type Property</sub>

Posted whenever a column is resized in an `NSTableView` object.

<sub>macOS</sub>

```swift
class let columnDidResizeNotification: NSNotification.Name
```

## Discussion

The notification object is the table view in which a column was resized. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `@"NSTableColumn"` | The column that was resized. |
| `@"NSOldWidth"` | An NSNumber containing the integer value of the column’s original width. |

To observe this notification using Swift concurrency, use [ColumnDidResizeMessage](columndidresizemessage.md).

## See Also

### Notifications

- [NSTableViewColumnDidMoveNotification](columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSTableView` object.
- [NSTableViewSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after an `NSTableView` object’s selection changes.
- [NSTableViewSelectionIsChangingNotification](selectionischangingnotification.md) — Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).
