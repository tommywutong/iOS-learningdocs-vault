---
title: UICollectionViewDragDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdragdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdragdelegate.json'
content_hash: 'sha256:bae758ab791586a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDragDelegate

<sub>Protocol</sub>

The interface for initiating drags from a collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UICollectionViewDragDelegate : NSObjectProtocol
```

## Overview

Implement this protocol in the object that you use to initiate drags from your collection view. The only required method of this protocol is the [- collectionView:itemsForBeginningDragSession:atIndexPath:](<uicollectionviewdragdelegate/collectionview(__itemsforbeginning_at_).md>) method, but you can implement other methods as needed to customize the drag behavior of your collection view.

Assign your custom delegate object to the [dragDelegate](uicollectionview/dragdelegate.md) property of your collection view.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing the items to drag

- [- collectionView:itemsForBeginningDragSession:atIndexPath:](<uicollectionviewdragdelegate/collectionview(__itemsforbeginning_at_).md>) — Provides the initial set of items (if any) to drag.
- [- collectionView:itemsForAddingToDragSession:atIndexPath:point:](<uicollectionviewdragdelegate/collectionview(__itemsforaddingto_at_point_).md>) — Adds the specified items to an existing drag session.

### Tracking the drag session

- [- collectionView:dragSessionWillBegin:](<uicollectionviewdragdelegate/collectionview(__dragsessionwillbegin_).md>) — Notifies you that a drag session is about to begin for the collection view.
- [- collectionView:dragSessionDidEnd:](<uicollectionviewdragdelegate/collectionview(__dragsessiondidend_).md>) — Notifies you that a drag session ended for the collection view.

### Providing a custom preview

- [- collectionView:dragPreviewParametersForItemAtIndexPath:](<uicollectionviewdragdelegate/collectionview(__dragpreviewparametersforitemat_).md>) — Returns custom information about how to display the item at the specified location during the drag.

### Controlling the drag session

- [- collectionView:dragSessionAllowsMoveOperation:](<uicollectionviewdragdelegate/collectionview(__dragsessionallowsmoveoperation_).md>) — Returns a Boolean value that determines whether a move operation is allowed for a drag session.
- [- collectionView:dragSessionIsRestrictedToDraggingApplication:](<uicollectionviewdragdelegate/collectionview(__dragsessionisrestrictedtodraggingapplication_).md>) — Returns a Boolean value that determines whether the source app and destination app must be the same for a drag session.

## See Also

### Drag and drop

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md) — Initiate drags and handle drops from a collection view.
- [UICollectionViewDropDelegate](uicollectionviewdropdelegate.md) — The interface for handling drops in a collection view.
- [UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md) — An interface for coordinating your custom drop-related actions with the collection view.
- [UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md) — A placeholder for an item dropped on a collection view.
- [UICollectionViewDropProposal](uicollectionviewdropproposal.md) — Your proposed solution for handling a drop in a collection view.
- [UICollectionViewDropItem](uicollectionviewdropitem.md) — The data associated with an item being dropped into the collection view.
- [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md) — An object that contains information about a placeholder in the collection view.
- [UIDataSourceTranslating](uidatasourcetranslating.md) — An advanced interface for managing a data source object.
- [UICollectionViewPlaceholder](uicollectionviewplaceholder.md) — A placeholder for an item dragged or dropped on a collection view.
