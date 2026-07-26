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
doc_path: '/documentation/uikit/uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropplaceholdercontext/commitinsertion%28datasourceupdates%3A%29.json'
content_hash: 'sha256:8407ecc8b9ecac86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropPlaceholderContext](../uitableviewdropplaceholdercontext.md)

# commitInsertion(dataSourceUpdates:)

<sub>Instance Method</sub>

Exchanges the placeholder cell for a cell with the final content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func commitInsertion(dataSourceUpdates: (IndexPath) -> Void) -> Bool
```

## Parameters

- `dataSourceUpdates` — The handler block to execute as part of committing your changes. Use this block to update your table view’s data source with the actual data that you received. This block has no return value and takes the following parameter: - **insertionIndexPath** — The location at which to insert any items into your data source. Always use this index path for the insertion point instead of any cached values.

## Return Value

[true](../../swift/true.md) if the placeholder was replaced by your content or [false](../../swift/false.md) if the placeholder was no longer in the table view.

## Discussion

When you receive the actual data for a cell, call this method on your app’s main thread to remove the corresponding placeholder cell and insert the actual cell. If the placeholder cell is still present in the table view, this method calls the `dataSourceUpdates` handler. Use that block only to update the data source object of your table view. Don’t update the table view itself, and don’t call [- reloadData](<../uitableview/reloaddata().md>) on the table view. When your block finishes, the table view updates itself automatically, creating a new cell for your data.

If the placeholder cell is no longer present, this method doesn’t execute your `dataSourceUpdates` block.
