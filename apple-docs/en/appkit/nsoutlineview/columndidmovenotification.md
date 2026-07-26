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
doc_path: /documentation/appkit/nsoutlineview/columndidmovenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsoutlineview/columndidmovenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsoutlineview/columndidmovenotification.json'
content_hash: 'sha256:2f7dfaae8857c5f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSOutlineView](../nsoutlineview.md)

# columnDidMoveNotification

<sub>Type Property</sub>

Posted whenever a column is moved by user action in an `NSOutlineView` object.

<sub>macOS</sub>

```swift
class let columnDidMoveNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSOutlineView` object in which a column moved. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `@"NSOldColumn"` | An [NSNumber](../../foundation/nsnumber.md) object containing the integer value of the column’s original index |
| `@"NSNewColumn"` | An [NSNumber](../../foundation/nsnumber.md) object containing the integer value of the column’s present index |

## See Also

### Related Documentation

- [- moveColumn:toColumn:](<../nstableview/movecolumn(__tocolumn_).md>) — Moves the column and heading at the specified index to the new specified index.

### Notifications

- [NSOutlineViewColumnDidResizeNotification](columndidresizenotification.md) — Posted whenever a column is resized in an `NSOutlineView` object.
- [NSOutlineViewItemDidCollapseNotification](itemdidcollapsenotification.md) — Posted whenever an item is collapsed in an `NSOutlineView` object.
- [NSOutlineViewItemDidExpandNotification](itemdidexpandnotification.md) — Posted whenever an item is expanded in an `NSOutlineView` object.
- [NSOutlineViewItemWillCollapseNotification](itemwillcollapsenotification.md) — Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewItemWillExpandNotification](itemwillexpandnotification.md) — Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after the outline view’s selection changes.
- [NSOutlineViewSelectionIsChangingNotification](selectionischangingnotification.md) — Posted as the outline view’s selection changes (while the mouse button is still down).
