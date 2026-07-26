---
title: UITableViewDropCoordinator
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdropcoordinator
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropcoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropcoordinator.json'
content_hash: 'sha256:d7da2ad187126af1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDropCoordinator

<sub>Protocol</sub>

An interface for coordinating your custom drop-related actions with the table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITableViewDropCoordinator : NSObjectProtocol
```

## Overview

Don’t create instances of this class yourself. When a drop occurs in the table view, UIKit creates an instance of this class and passes it to your [- tableView:performDropWithCoordinator:](<uitableviewdropdelegate/tableview(__performdropwith_).md>) method. Use the object to let the table view know how you want to animate the dropped items into position.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the dragged items

- [items](uitableviewdropcoordinator/items.md) — The items being dragged.

### Getting the drop location

- [destinationIndexPath](uitableviewdropcoordinator/destinationindexpath.md) — The index path at which to insert the item into the table view.

### Animating rows to their destination

- [- dropItem:toRowAtIndexPath:](<uitableviewdropcoordinator/drop(__torowat_).md>) — Animates the item to the specified index path in the table view.
- [- dropItem:intoRowAtIndexPath:rect:](<uitableviewdropcoordinator/drop(__intorowat_rect_).md>)
- [- dropItem:toTarget:](<uitableviewdropcoordinator/drop(__to_)-57wx.md>) — Animates the item to an arbitrary location in your view hierarchy.
- [- dropItem:toPlaceholder:](<uitableviewdropcoordinator/drop(__to_)-3znax.md>) — Animates the item to the specified location and inserts a placeholder cell at that location.

### Getting the session information

- [session](uitableviewdropcoordinator/session.md) — The drop session containing information about the transaction.
- [proposal](uitableviewdropcoordinator/proposal.md) — The proposal for how to incorporate the dropped items.

## See Also

### Drag and drop

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md) — Initiate drags and handle drops from a table view.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md) — Demonstrates how to enable and implement drag and drop for a table view.
- [UITableViewDragDelegate](uitableviewdragdelegate.md) — The interface for initiating drags from a table view.
- [UITableViewDropDelegate](uitableviewdropdelegate.md) — The interface for handling drops in a table view.
- [UITableViewDropItem](uitableviewdropitem.md) — The data associated with an item being dropped into the table view.
- [UITableViewDropProposal](uitableviewdropproposal.md) — Your proposed solution for handling a drop in a table view.
