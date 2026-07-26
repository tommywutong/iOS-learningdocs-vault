---
title: itemDidCollapseNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsoutlineview/itemdidcollapsenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsoutlineview/itemdidcollapsenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsoutlineview/itemdidcollapsenotification.json'
content_hash: 'sha256:a558936f1b51c4f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSOutlineView](../nsoutlineview.md)

# itemDidCollapseNotification

<sub>Type Property</sub>

Posted whenever an item is collapsed in an `NSOutlineView` object.

<sub>macOS</sub>

```swift
class let itemDidCollapseNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSOutlineView` object in which an item was collapsed. A collapsed item’s children lose their status as being selected. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `@"NSObject"` | The item that was collapsed (an id) |

To observe this notification using Swift concurrency, use [ItemDidCollapseMessage](itemdidcollapsemessage.md).

## See Also

### Notifications

- [NSOutlineViewColumnDidMoveNotification](columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [NSOutlineViewColumnDidResizeNotification](columndidresizenotification.md) — Posted whenever a column is resized in an `NSOutlineView` object.
- [NSOutlineViewItemDidExpandNotification](itemdidexpandnotification.md) — Posted whenever an item is expanded in an `NSOutlineView` object.
- [NSOutlineViewItemWillCollapseNotification](itemwillcollapsenotification.md) — Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewItemWillExpandNotification](itemwillexpandnotification.md) — Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after the outline view’s selection changes.
- [NSOutlineViewSelectionIsChangingNotification](selectionischangingnotification.md) — Posted as the outline view’s selection changes (while the mouse button is still down).
