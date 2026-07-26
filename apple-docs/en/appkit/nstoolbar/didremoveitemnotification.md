---
title: didRemoveItemNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstoolbar/didremoveitemnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstoolbar/didremoveitemnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstoolbar/didremoveitemnotification.json'
content_hash: 'sha256:69edd973683275e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSToolbar](../nstoolbar.md)

# didRemoveItemNotification

<sub>Type Property</sub>

Posted after an item is removed from a toolbar.

<sub>Mac Catalyst, macOS</sub>

```swift
class let didRemoveItemNotification: NSNotification.Name
```

## Discussion

The notification item is the `NSToolbar` object that removed the item. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| [NSToolbarItemKey](../nstoolbaruserinfokey/itemkey.md) | The `NSToolbarItem` object that was removed. |

## See Also

### Related Documentation

- [- toolbarDidRemoveItem:](<../nstoolbardelegate/toolbardidremoveitem(__).md>) — Tells the delegate that the toolbar removed the specified item.

### Managing items on the toolbar

- [items](items.md) — An array containing the toolbar’s current items, in order.
- [visibleItems](visibleitems.md) — An array containing the toolbar’s currently visible items.
- [centeredItemIdentifiers](centereditemidentifiers.md) — The set of custom items to display in the center of the toolbar.
- [selectedItemIdentifier](selecteditemidentifier.md) — The identifier of the toolbar’s currently selected item.
- [NSToolbarWillAddItemNotification](willadditemnotification.md) — Posts before the toolbar adds a new item.
- [- insertItemWithItemIdentifier:atIndex:](<insertitem(withitemidentifier_at_).md>) — Inserts an item into the toolbar at the specified index.
- [- removeItemAtIndex:](<removeitem(at_).md>) — Removes the item at the specified index in the toolbar.
