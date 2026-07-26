---
title: UICollectionViewDropItem
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropitem
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropitem.json'
content_hash: 'sha256:ed4a9287d4d88f5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDropItem

<sub>Protocol</sub>

The data associated with an item being dropped into the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UICollectionViewDropItem : NSObjectProtocol
```

## Overview

When handling a drop, you get instances of this class from the [items](uicollectionviewdropcoordinator/items.md) property of the [UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md) object. Use them to retrieve the data for the items being dragged and to plan any animations related to dropping the items. You do not create instances of this class yourself.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the Drag Item

- [dragItem](uicollectionviewdropitem/dragitem.md) — The item that was dragged.

### Getting the Item Information

- [previewSize](uicollectionviewdropitem/previewsize.md) — The size of the drag item’s preview.
- [sourceIndexPath](uicollectionviewdropitem/sourceindexpath.md) — The index path of the item in the collection view, if any.

## See Also

### Drag and drop

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md) — Initiate drags and handle drops from a collection view.
- [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md) — The interface for initiating drags from a collection view.
- [UICollectionViewDropDelegate](uicollectionviewdropdelegate.md) — The interface for handling drops in a collection view.
- [UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md) — An interface for coordinating your custom drop-related actions with the collection view.
- [UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md) — A placeholder for an item dropped on a collection view.
- [UICollectionViewDropProposal](uicollectionviewdropproposal.md) — Your proposed solution for handling a drop in a collection view.
- [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md) — An object that contains information about a placeholder in the collection view.
- [UIDataSourceTranslating](uidatasourcetranslating.md) — An advanced interface for managing a data source object.
- [UICollectionViewPlaceholder](uicollectionviewplaceholder.md) — A placeholder for an item dragged or dropped on a collection view.
