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
doc_path: /documentation/appkit/nsoutlineview/selectiondidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsoutlineview/selectiondidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsoutlineview/selectiondidchangenotification.json'
content_hash: 'sha256:564bd0b13509800a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSOutlineView](../nsoutlineview.md)

# selectionDidChangeNotification

<sub>Type Property</sub>

Posted after the outline view’s selection changes.

<sub>macOS</sub>

```swift
class let selectionDidChangeNotification: NSNotification.Name
```

## Discussion

The notification object is the outline view whose selection changed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [SelectionDidChangeMessage](selectiondidchangemessage.md).

## See Also

### Notifications

- [NSOutlineViewColumnDidMoveNotification](columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [NSOutlineViewColumnDidResizeNotification](columndidresizenotification.md) — Posted whenever a column is resized in an `NSOutlineView` object.
- [NSOutlineViewItemDidCollapseNotification](itemdidcollapsenotification.md) — Posted whenever an item is collapsed in an `NSOutlineView` object.
- [NSOutlineViewItemDidExpandNotification](itemdidexpandnotification.md) — Posted whenever an item is expanded in an `NSOutlineView` object.
- [NSOutlineViewItemWillCollapseNotification](itemwillcollapsenotification.md) — Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewItemWillExpandNotification](itemwillexpandnotification.md) — Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewSelectionIsChangingNotification](selectionischangingnotification.md) — Posted as the outline view’s selection changes (while the mouse button is still down).
