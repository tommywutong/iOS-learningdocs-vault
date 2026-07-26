---
title: UITableViewDropItem
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdropitem
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropitem.json'
content_hash: 'sha256:dd2fa20906bca9df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDropItem

<sub>Protocol</sub>

The data associated with an item being dropped into the table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITableViewDropItem : NSObjectProtocol
```

## Overview

When handling a drop, you get instances of this class from the [items](uitableviewdropcoordinator/items.md) property of the [UITableViewDropCoordinator](uitableviewdropcoordinator.md) object. Use them to retrieve the data for the items being dragged and to plan any animations related to dropping the items. You don’t create instances of this class yourself.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the drag item

- [dragItem](uitableviewdropitem/dragitem.md) — The item that was dragged.

### Getting the item information

- [previewSize](uitableviewdropitem/previewsize.md) — The size of the drag item’s preview.
- [sourceIndexPath](uitableviewdropitem/sourceindexpath.md) — The index path of the item in the table view, if any.

## See Also

### Drag and drop

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md) — Initiate drags and handle drops from a table view.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md) — Demonstrates how to enable and implement drag and drop for a table view.
- [UITableViewDragDelegate](uitableviewdragdelegate.md) — The interface for initiating drags from a table view.
- [UITableViewDropDelegate](uitableviewdropdelegate.md) — The interface for handling drops in a table view.
- [UITableViewDropCoordinator](uitableviewdropcoordinator.md) — An interface for coordinating your custom drop-related actions with the table view.
- [UITableViewDropProposal](uitableviewdropproposal.md) — Your proposed solution for handling a drop in a table view.
