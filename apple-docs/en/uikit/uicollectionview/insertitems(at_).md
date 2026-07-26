---
title: 'insertItems(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/insertitems(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/insertitems(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/insertitems%28at%3A%29.json'
content_hash: 'sha256:4b7055343ea09ff3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# insertItems(at:)

<sub>Instance Method</sub>

Inserts new items at the specified index paths.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertItems(at indexPaths: [IndexPath])
```

## Parameters

- `indexPaths` — An array of [NSIndexPath](../../foundation/nsindexpath.md) objects, each of which contains a section index and item index at which to insert a new cell. This parameter must not be `nil`.

## Discussion

Call this method to insert one or more new items into the collection view. You might do this when your data source object receives data for new items or in response to user interactions with the collection view. The collection view gets the layout information for the new cells as part of calling this method. And if the layout information indicates that the cells should appear onscreen, the collection view asks your data source to provide the appropriate views, animating them into position as needed.

You can also call this method from a block passed to the [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## See Also

### Inserting, moving, and deleting Items

- [- moveItemAtIndexPath:toIndexPath:](<moveitem(at_to_).md>) — Moves an item from one location to another in the collection view.
- [- deleteItemsAtIndexPaths:](<deleteitems(at_).md>) — Deletes the items at the specified index paths.
