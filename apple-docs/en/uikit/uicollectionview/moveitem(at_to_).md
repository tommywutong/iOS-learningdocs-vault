---
title: 'moveItem(at:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/moveitem(at:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/moveitem(at:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/moveitem%28at%3Ato%3A%29.json'
content_hash: 'sha256:67e925e6dec95421'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# moveItem(at:to:)

<sub>Instance Method</sub>

Moves an item from one location to another in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func moveItem(at indexPath: IndexPath, to newIndexPath: IndexPath)
```

## Parameters

- `indexPath` — The index path of the item you want to move. This parameter must not be `nil`.

- `newIndexPath` — The index path of the item’s new location. This parameter must not be `nil`.

## Discussion

Use this method to reorganize existing data items. You might do this when you rearrange the items within your data source object or in response to user interactions with the collection view. You can move items between sections or within the same section. The collection view updates the layout as needed to account for the move, animating cells into position as needed.

You can also call this method from a block passed to the [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## See Also

### Inserting, moving, and deleting Items

- [- insertItemsAtIndexPaths:](<insertitems(at_).md>) — Inserts new items at the specified index paths.
- [- deleteItemsAtIndexPaths:](<deleteitems(at_).md>) — Deletes the items at the specified index paths.
