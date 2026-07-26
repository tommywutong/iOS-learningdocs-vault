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
doc_path: /documentation/appkit/nsoutlineview/columndidresizenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsoutlineview/columndidresizenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsoutlineview/columndidresizenotification.json'
content_hash: 'sha256:b5f638a65bc74494'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSOutlineView](../nsoutlineview.md)

# columnDidResizeNotification

<sub>Type Property</sub>

Posted whenever a column is resized in an `NSOutlineView` object.

<sub>macOS</sub>

```swift
class let columnDidResizeNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSOutlineView` object in which a column was resized. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `@"NSTableColumn"` | The column that was resized. |
| `@"NSOldWidth"` | An [NSNumber](../../foundation/nsnumber.md) object containing the column’s original width |

To observe this notification using Swift concurrency, use [ColumnDidResizeMessage](columndidresizemessage.md).

## See Also

### Notifications

- [NSOutlineViewColumnDidMoveNotification](columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [NSOutlineViewItemDidCollapseNotification](itemdidcollapsenotification.md) — Posted whenever an item is collapsed in an `NSOutlineView` object.
- [NSOutlineViewItemDidExpandNotification](itemdidexpandnotification.md) — Posted whenever an item is expanded in an `NSOutlineView` object.
- [NSOutlineViewItemWillCollapseNotification](itemwillcollapsenotification.md) — Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewItemWillExpandNotification](itemwillexpandnotification.md) — Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after the outline view’s selection changes.
- [NSOutlineViewSelectionIsChangingNotification](selectionischangingnotification.md) — Posted as the outline view’s selection changes (while the mouse button is still down).
