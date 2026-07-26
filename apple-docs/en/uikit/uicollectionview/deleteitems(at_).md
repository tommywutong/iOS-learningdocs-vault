---
title: 'deleteItems(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/deleteitems(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/deleteitems(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/deleteitems%28at%3A%29.json'
content_hash: 'sha256:7734826d490ba971'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# deleteItems(at:)

<sub>Instance Method</sub>

Deletes the items at the specified index paths.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func deleteItems(at indexPaths: [IndexPath])
```

## Parameters

- `indexPaths` — An array of [NSIndexPath](../../foundation/nsindexpath.md) objects, each of which contains a section index and item index for the item you want to delete from the collection view. This parameter must not be `nil`.

## Discussion

Use this method to remove items from the collection view. You might do this when you remove the items from your data source object or in response to user interactions with the collection view. The collection view updates the layout of the remaining items to account for the deletions, animating the remaining items into position as needed.

You can also call this method from a block passed to the [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## See Also

### Inserting, moving, and deleting Items

- [- insertItemsAtIndexPaths:](<insertitems(at_).md>) — Inserts new items at the specified index paths.
- [- moveItemAtIndexPath:toIndexPath:](<moveitem(at_to_).md>) — Moves an item from one location to another in the collection view.
