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
doc_path: /documentation/appkit/nsoutlineview/selectionischangingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsoutlineview/selectionischangingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsoutlineview/selectionischangingnotification.json'
content_hash: 'sha256:33660351a9680e57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSOutlineView](../nsoutlineview.md)

# selectionIsChangingNotification

<sub>Type Property</sub>

Posted as the outline view’s selection changes (while the mouse button is still down).

<sub>macOS</sub>

```swift
class let selectionIsChangingNotification: NSNotification.Name
```

## Discussion

The notification object is the outline view whose selection is changing. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [SelectionIsChangingMessage](selectionischangingmessage.md).

## See Also

### Notifications

- [NSOutlineViewColumnDidMoveNotification](columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [NSOutlineViewColumnDidResizeNotification](columndidresizenotification.md) — Posted whenever a column is resized in an `NSOutlineView` object.
- [NSOutlineViewItemDidCollapseNotification](itemdidcollapsenotification.md) — Posted whenever an item is collapsed in an `NSOutlineView` object.
- [NSOutlineViewItemDidExpandNotification](itemdidexpandnotification.md) — Posted whenever an item is expanded in an `NSOutlineView` object.
- [NSOutlineViewItemWillCollapseNotification](itemwillcollapsenotification.md) — Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewItemWillExpandNotification](itemwillexpandnotification.md) — Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after the outline view’s selection changes.
