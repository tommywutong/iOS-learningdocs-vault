---
title: 'performBatchUpdates(_:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/performbatchupdates(_:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/performbatchupdates(_:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/performbatchupdates%28_%3Acompletion%3A%29.json'
content_hash: 'sha256:616dad5e239482f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# performBatchUpdates(_:completion:)

<sub>Instance Method</sub>

Animates multiple insert, delete, reload, and move operations as a group.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func performBatchUpdates(_ updates: (() -> Void)?, completion: ((Bool) -> Void)? = nil)
```

## Parameters

- `updates` — The block that performs the relevant insert, delete, reload, or move operations.

- `completion` — A completion handler block to execute when all of the operations finish. This block takes a single Boolean parameter that contains the value [true](../../swift/true.md) if all of the related animations completed successfully or [false](../../swift/false.md) if they were interrupted. This parameter may be `nil`.

## Discussion

You can use this method in cases where you want to make multiple changes to the collection view in one single animated operation, as opposed to in several separate animations. You might use this method to insert, delete, reload, or move cells or use it to change the layout parameters associated with one or more cells. Use the block passed in the `updates` parameter to specify all of the operations you want to perform.

If the collection view’s layout isn’t up to date before you call this method, a reload may occur. To avoid problems, you should update your data model inside the `updates` block or ensure the layout is updated before you call [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>).

Deletes are processed before inserts in batch operations. This means the indexes for the deletions are processed relative to the indexes of the collection view’s state before the batch operation, and the indexes for the insertions are processed relative to the indexes of the state after all the deletions in the batch operation.

## See Also

### Related Documentation

- [- deleteItemsAtIndexPaths:](<deleteitems(at_).md>) — Deletes the items at the specified index paths.
- [- moveSection:toSection:](<movesection(__tosection_).md>) — Moves a section from one location to another in the collection view.
- [- moveItemAtIndexPath:toIndexPath:](<moveitem(at_to_).md>) — Moves an item from one location to another in the collection view.
- [- insertItemsAtIndexPaths:](<insertitems(at_).md>) — Inserts new items at the specified index paths.
- [- insertSections:](<insertsections(__).md>) — Inserts new sections at the specified indexes.
- [- deleteSections:](<deletesections(__).md>) — Deletes the sections at the specified indexes.
