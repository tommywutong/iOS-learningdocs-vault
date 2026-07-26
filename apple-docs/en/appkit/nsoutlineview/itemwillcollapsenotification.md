---
title: itemWillCollapseNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsoutlineview/itemwillcollapsenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsoutlineview/itemwillcollapsenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsoutlineview/itemwillcollapsenotification.json'
content_hash: 'sha256:7e00386659f31269'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSOutlineView](../nsoutlineview.md)

# itemWillCollapseNotification

<sub>Type Property</sub>

Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).

<sub>macOS</sub>

```swift
class let itemWillCollapseNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSOutlineView` object that contains the item about to be collapsed. A collapsed item’s children will lose their status as being selected. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `@"NSObject"` | The item about to be collapsed (an id) |

To observe this notification using Swift concurrency, use [ItemWillCollapseMessage](itemwillcollapsemessage.md).

## See Also

### Notifications

- [NSOutlineViewColumnDidMoveNotification](columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [NSOutlineViewColumnDidResizeNotification](columndidresizenotification.md) — Posted whenever a column is resized in an `NSOutlineView` object.
- [NSOutlineViewItemDidCollapseNotification](itemdidcollapsenotification.md) — Posted whenever an item is collapsed in an `NSOutlineView` object.
- [NSOutlineViewItemDidExpandNotification](itemdidexpandnotification.md) — Posted whenever an item is expanded in an `NSOutlineView` object.
- [NSOutlineViewItemWillExpandNotification](itemwillexpandnotification.md) — Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [NSOutlineViewSelectionDidChangeNotification](selectiondidchangenotification.md) — Posted after the outline view’s selection changes.
- [NSOutlineViewSelectionIsChangingNotification](selectionischangingnotification.md) — Posted as the outline view’s selection changes (while the mouse button is still down).
