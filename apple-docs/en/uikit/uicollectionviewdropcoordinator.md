---
title: UICollectionViewDropCoordinator
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropcoordinator
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropcoordinator.json'
content_hash: 'sha256:50813d8eb4190d7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDropCoordinator

<sub>Protocol</sub>

An interface for coordinating your custom drop-related actions with the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UICollectionViewDropCoordinator : NSObjectProtocol
```

## Overview

You don’t create instances of this class yourself. When a drop occurs in the collection view, UIKit creates an instance of this class and passes it to your [- collectionView:performDropWithCoordinator:](<uicollectionviewdropdelegate/collectionview(__performdropwith_).md>) method. Use the object to let the collection view know how you want to animate the dropped items into position.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the Dragged Items

- [items](uicollectionviewdropcoordinator/items.md) — The items being dragged.

### Getting the Drop Location

- [destinationIndexPath](uicollectionviewdropcoordinator/destinationindexpath.md) — The index path at which to insert the item in the collection view.

### Animating Items to Their Destination

- [- dropItem:toItemAtIndexPath:](<uicollectionviewdropcoordinator/drop(__toitemat_).md>) — Animates the item to the specified index path in the collection view.
- [- dropItem:intoItemAtIndexPath:rect:](<uicollectionviewdropcoordinator/drop(__intoitemat_rect_).md>) — Animates the item to the specified rectangle in the collection view.
- [- dropItem:toTarget:](<uicollectionviewdropcoordinator/drop(__to_)-7w5rn.md>) — Animates the item to an arbitrary location in your view hierarchy.
- [- dropItem:toPlaceholder:](<uicollectionviewdropcoordinator/drop(__to_)-l5tg.md>) — Animates the item to the specified location and inserts a placeholder cell at that location.

### Getting the Session Information

- [session](uicollectionviewdropcoordinator/session.md) — The drop session containing information about the transaction.
- [proposal](uicollectionviewdropcoordinator/proposal.md) — The current proposal for how to incorporate the dropped items.

## See Also

### Drag and drop

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md) — Initiate drags and handle drops from a collection view.
- [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md) — The interface for initiating drags from a collection view.
- [UICollectionViewDropDelegate](uicollectionviewdropdelegate.md) — The interface for handling drops in a collection view.
- [UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md) — A placeholder for an item dropped on a collection view.
- [UICollectionViewDropProposal](uicollectionviewdropproposal.md) — Your proposed solution for handling a drop in a collection view.
- [UICollectionViewDropItem](uicollectionviewdropitem.md) — The data associated with an item being dropped into the collection view.
- [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md) — An object that contains information about a placeholder in the collection view.
- [UIDataSourceTranslating](uidatasourcetranslating.md) — An advanced interface for managing a data source object.
- [UICollectionViewPlaceholder](uicollectionviewplaceholder.md) — A placeholder for an item dragged or dropped on a collection view.
