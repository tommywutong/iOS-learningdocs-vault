---
title: 'commitInsertion(dataSourceUpdates:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropplaceholdercontext/commitinsertion(datasourceupdates:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropplaceholdercontext/commitinsertion(datasourceupdates:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropplaceholdercontext/commitinsertion%28datasourceupdates%3A%29.json'
content_hash: 'sha256:6b076b715e50b96b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropPlaceholderContext](../uicollectionviewdropplaceholdercontext.md)

# commitInsertion(dataSourceUpdates:)

<sub>Instance Method</sub>

Exchanges the placeholder cell for a cell with the final content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func commitInsertion(dataSourceUpdates: (IndexPath) -> Void) -> Bool
```

## Parameters

- `dataSourceUpdates` — The handler block to execute as part of committing your changes. Use this block to update your collection view’s data source with the actual data that you received. This block has no return value and takes the following parameter: - **insertionIndexPath** — The location at which to insert any items. Always use this index path for the insertion point instead of any cached values.

## Return Value

[true](../../swift/true.md) if the placeholder was replaced by your content or [false](../../swift/false.md) if the placeholder was no longer in the collection view.

## Discussion

When you receive the actual data for a cell, call this method to remove the corresponding placeholder cell and insert the actual cell. If the placeholder cell is still present in the collection view, this method calls the `dataSourceUpdates` handler. Use that handler block to update the data source object of the collection view. Do not update the collection view itself. This method automatically updates the collection view, creating a new cell for your data.

If the placeholder cell is no longer present, this method does not execute your `dataSourceUpdates` block.

## See Also

### Updating the Placeholder Cell

- [- setNeedsCellUpdate](<setneedscellupdate().md>) — Updates the contents of the placeholder cell.
