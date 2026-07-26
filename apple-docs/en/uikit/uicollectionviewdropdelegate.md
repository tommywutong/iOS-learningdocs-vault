---
title: UICollectionViewDropDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropdelegate.json'
content_hash: 'sha256:25a0fbd34e564caf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDropDelegate

<sub>Protocol</sub>

The interface for handling drops in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UICollectionViewDropDelegate : NSObjectProtocol
```

## Overview

Implement this protocol in the object that you use to incorporate dropped data into your collection view. The only required method of this protocol is the [- collectionView:performDropWithCoordinator:](<uicollectionviewdropdelegate/collectionview(__performdropwith_).md>) method, but you can implement other methods as needed to customize the drop behavior of your collection view.

Assign your custom delegate object to the [dropDelegate](uicollectionview/dropdelegate.md) property of your collection view.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Declaring support for handling drops

- [- collectionView:canHandleDropSession:](<uicollectionviewdropdelegate/collectionview(__canhandle_).md>) — Asks your delegate whether the collection view can accept a drop with the specified type of data.

### Incorporating the dropped data

- [- collectionView:performDropWithCoordinator:](<uicollectionviewdropdelegate/collectionview(__performdropwith_).md>) — Tells your delegate to incorporate the drop data into the collection view.

### Tracking the drag movements

- [- collectionView:dropSessionDidUpdate:withDestinationIndexPath:](<uicollectionviewdropdelegate/collectionview(__dropsessiondidupdate_withdestinationindexpath_).md>) — Tells your delegate that the position of the dragged data over the collection view changed.
- [- collectionView:dropSessionDidEnter:](<uicollectionviewdropdelegate/collectionview(__dropsessiondidenter_).md>) — Notifies you when dragged content enters the collection view’s bounds rectangle.
- [- collectionView:dropSessionDidExit:](<uicollectionviewdropdelegate/collectionview(__dropsessiondidexit_).md>) — Notifies you when dragged content exits the collection view’s bounds rectangle.
- [- collectionView:dropSessionDidEnd:](<uicollectionviewdropdelegate/collectionview(__dropsessiondidend_).md>) — Notifies you when the drag operation ends.

### Providing a custom preview

- [- collectionView:dropPreviewParametersForItemAtIndexPath:](<uicollectionviewdropdelegate/collectionview(__droppreviewparametersforitemat_).md>) — Returns custom information about how to display the item at the specified location during the drop.

## See Also

### Drag and drop

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md) — Initiate drags and handle drops from a collection view.
- [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md) — The interface for initiating drags from a collection view.
- [UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md) — An interface for coordinating your custom drop-related actions with the collection view.
- [UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md) — A placeholder for an item dropped on a collection view.
- [UICollectionViewDropProposal](uicollectionviewdropproposal.md) — Your proposed solution for handling a drop in a collection view.
- [UICollectionViewDropItem](uicollectionviewdropitem.md) — The data associated with an item being dropped into the collection view.
- [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md) — An object that contains information about a placeholder in the collection view.
- [UIDataSourceTranslating](uidatasourcetranslating.md) — An advanced interface for managing a data source object.
- [UICollectionViewPlaceholder](uicollectionviewplaceholder.md) — A placeholder for an item dragged or dropped on a collection view.
