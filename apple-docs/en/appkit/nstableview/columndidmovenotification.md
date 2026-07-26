---
title: columnDidMoveNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstableview/columndidmovenotification
source_url: 'https://developer.apple.com/documentation/appkit/nstableview/columndidmovenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstableview/columndidmovenotification.json'
content_hash: 'sha256:fd6accecdcbf82d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTableView](../nstableview.md)

# columnDidMoveNotification

<sub>Type Property</sub>

Posted whenever a column is moved by user action in an `NSTableView` object.

<sub>macOS</sub>

```swift
class let columnDidMoveNotification: NSNotification.Name
```

## Discussion

The notification object is the table view in which a column moved. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `@"NSOldColumn"` | An `NSNumber` object containing the integer value of the column’s original index. |
| `@"NSNewColumn"` | An `NSNumber` object containing the integer value of the column’s present index. |

## See Also

### Related Documentation

- [- moveColumn:toColumn:](<movecolumn(__tocolumn_).md>) — Moves the column and heading at the specified index to the new specified index.

### Notifications

- [NSTableViewColumnDidResizeNotification](columndidresizenotification.md) — Posted whenever a column is resized in an `NSTableView` object.
- [NSTableViewSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after an `NSTableView` object’s selection changes.
- [NSTableViewSelectionIsChangingNotification](selectionischangingnotification.md) — Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).
