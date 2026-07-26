---
title: 'collectionView(_:itemsForBeginning:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:itemsforbeginning:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:itemsforbeginning:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdragdelegate/collectionview%28_%3Aitemsforbeginning%3Aat%3A%29.json'
content_hash: 'sha256:77f03b2f7806aad9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDragDelegate](../uicollectionviewdragdelegate.md)

# collectionView(_:itemsForBeginning:at:)

<sub>Instance Method</sub>

Provides the initial set of items (if any) to drag.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func collectionView(_ collectionView: UICollectionView, itemsForBeginning session: any UIDragSession, at indexPath: IndexPath) -> [UIDragItem]
```

## Parameters

- `collectionView` — The collection view from which the drag operation originated.

- `session` — The current drag session object.

- `indexPath` — The index path of the item to drag.

## Return Value

An array of [UIDragItem](../uidragitem.md) objects containing the details of the items to drag. Return an empty array to prevent the item from being dragged.

## Discussion

You must implement this method to allow the dragging of items from your collection view. In your implementation, create one or more [UIDragItem](../uidragitem.md) objects for the item at the specified `indexPath`. Normally, you return only one drag item, but if the specified item has children or can’t be dragged without one or more associated items, include those items as well.

The collection view calls this method one or more times when a new drag begins within its bounds. Specifically, if the user begins the drag from a selected item, the collection view calls this method once for each item that’s part of the selection. If the user begins the drag from an unselected item, the collection view calls the method only once for that item.

## See Also

### Providing the items to drag

- [- collectionView:itemsForAddingToDragSession:atIndexPath:point:](<collectionview(__itemsforaddingto_at_point_).md>) — Adds the specified items to an existing drag session.
