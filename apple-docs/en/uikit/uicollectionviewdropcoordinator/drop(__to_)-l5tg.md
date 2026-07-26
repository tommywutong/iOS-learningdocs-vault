---
title: 'drop(_:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropcoordinator/drop(_:to:)-l5tg'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:to:)-l5tg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropcoordinator/drop%28_%3Ato%3A%29-l5tg.json'
content_hash: 'sha256:10f74d48a589168c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropCoordinator](../uicollectionviewdropcoordinator.md)

# drop(_:to:)

<sub>Instance Method</sub>

Animates the item to the specified location and inserts a placeholder cell at that location.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drop(_ dragItem: UIDragItem, to placeholder: UICollectionViewDropPlaceholder) -> any UICollectionViewDropPlaceholderContext
```

## Parameters

- `dragItem` — The drag item containing the data to drop.

- `placeholder` — The placeholder to add at the specified location.

## Return Value

The context object that you use to replace or remove the placeholder cell later. Store a reference to this object so that you can call its methods later.

## Discussion

Use this method to insert a temporary placeholder cell (instead of a cell backed by actual data) into the collection view. When calling this method, don’t update your data source object to account for the placeholder. The collection view manages the placeholder until you explicitly remove it using the returned context object.

Typically, you use this method when you must load data asynchronously for a cell. Instead of updating your data source, you insert a placeholder cell. When the data is finally available, update your data source object and call the [- commitInsertionWithDataSourceUpdates:](<../uicollectionviewdropplaceholdercontext/commitinsertion(datasourceupdates_).md>) method of the returned context object to swap out the placeholder cell for an actual cell. You can also remove a placeholder cell that’s no longer needed by calling the [- deletePlaceholder](<../uicollectionviewdropplaceholdercontext/deleteplaceholder().md>) method.

At some point after calling this method, the collection view executes your `cellUpdateHandler` block. Use that block to configure the contents of the placeholder cell. Calling the [- setNeedsCellUpdate](<../uicollectionviewdropplaceholdercontext/setneedscellupdate().md>) method of the returned context object executes your handler again, giving you a way to update the cell later.

## See Also

### Animating Items to Their Destination

- [- dropItem:toItemAtIndexPath:](<drop(__toitemat_).md>) — Animates the item to the specified index path in the collection view.
- [- dropItem:intoItemAtIndexPath:rect:](<drop(__intoitemat_rect_).md>) — Animates the item to the specified rectangle in the collection view.
- [- dropItem:toTarget:](<drop(__to_)-7w5rn.md>) — Animates the item to an arbitrary location in your view hierarchy.
