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
doc_path: '/documentation/uikit/uitableviewdropcoordinator/drop(_:to:)-3znax'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropcoordinator/drop(_:to:)-3znax'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropcoordinator/drop%28_%3Ato%3A%29-3znax.json'
content_hash: 'sha256:1755b03a12526d99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropCoordinator](../uitableviewdropcoordinator.md)

# drop(_:to:)

<sub>Instance Method</sub>

Animates the item to the specified location and inserts a placeholder cell at that location.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drop(_ dragItem: UIDragItem, to placeholder: UITableViewDropPlaceholder) -> any UITableViewDropPlaceholderContext
```

## Parameters

- `dragItem` — The drag item containing the data to drop.

- `placeholder` — The object that contains information about the type of placeholder cell to insert, and where to insert it.

## Return Value

The context object that you use to replace or remove the placeholder cell later. Store a reference to this object so that you can call its methods later.

## Discussion

Use this method to insert a temporary placeholder cell (instead of a cell backed by actual data) into the table view. When calling this method, do not update your data source object to account for the placeholder. The table view manages the placeholder until you explicitly remove it using the returned context object.

Typically, you use this method when you must load data asynchronously for a cell. Instead of updating your data source, you insert a placeholder cell. When the data is finally available, update your data source object and call the [- commitInsertionWithDataSourceUpdates:](<../uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates_).md>) method of the returned context object to swap out the placeholder cell for an actual cell. You can also remove a placeholder cell that is no longer needed by calling the [- deletePlaceholder](<../uitableviewdropplaceholdercontext/deleteplaceholder().md>) method.

At some point after calling this method, the table view executes the [cellUpdateHandler](../uitableviewplaceholder/cellupdatehandler.md) block in the provided `placeholder` object. Use that block to configure the contents of the placeholder cell.

## See Also

### Animating rows to their destination

- [- dropItem:toRowAtIndexPath:](<drop(__torowat_).md>) — Animates the item to the specified index path in the table view.
- [- dropItem:intoRowAtIndexPath:rect:](<drop(__intorowat_rect_).md>)
- [- dropItem:toTarget:](<drop(__to_)-57wx.md>) — Animates the item to an arbitrary location in your view hierarchy.
