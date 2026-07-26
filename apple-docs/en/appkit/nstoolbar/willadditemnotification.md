---
title: willAddItemNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstoolbar/willadditemnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstoolbar/willadditemnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstoolbar/willadditemnotification.json'
content_hash: 'sha256:90fe70930fe80418'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSToolbar](../nstoolbar.md)

# willAddItemNotification

<sub>Type Property</sub>

Posts before the toolbar adds a new item.

<sub>Mac Catalyst, macOS</sub>

```swift
class let willAddItemNotification: NSNotification.Name
```

## Discussion

The notification item is the `NSToolbar` object that’s about to add the item. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| [NSToolbarItemKey](../nstoolbaruserinfokey/itemkey.md) | The `NSToolbarItem` object being added. |

## See Also

### Related Documentation

- [- toolbarWillAddItem:](<../nstoolbardelegate/toolbarwilladditem(__).md>) — Tells the delegate that the toolbar is about to add the specified item.

### Managing items on the toolbar

- [items](items.md) — An array containing the toolbar’s current items, in order.
- [visibleItems](visibleitems.md) — An array containing the toolbar’s currently visible items.
- [centeredItemIdentifiers](centereditemidentifiers.md) — The set of custom items to display in the center of the toolbar.
- [selectedItemIdentifier](selecteditemidentifier.md) — The identifier of the toolbar’s currently selected item.
- [NSToolbarDidRemoveItemNotification](didremoveitemnotification.md) — Posted after an item is removed from a toolbar.
- [- insertItemWithItemIdentifier:atIndex:](<insertitem(withitemidentifier_at_).md>) — Inserts an item into the toolbar at the specified index.
- [- removeItemAtIndex:](<removeitem(at_).md>) — Removes the item at the specified index in the toolbar.
