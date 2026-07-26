---
title: 'insertRows(at:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/insertrows(at:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/insertrows(at:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/insertrows%28at%3Awith%3A%29.json'
content_hash: 'sha256:619e40b2a67cf429'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# insertRows(at:with:)

<sub>Instance Method</sub>

Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertRows(at indexPaths: [IndexPath], with animation: UITableView.RowAnimation)
```

## Parameters

- `indexPaths` — An array of index path objects, each representing a row index and section index that together identify a row in the table view.

- `animation` — A constant that either specifies the kind of animation to perform when inserting the cell or requests no animation. See [RowAnimation](rowanimation.md) for descriptions of the constants.

## Discussion

`UITableView` calls the relevant delegate and data source methods immediately afterward to get the cells and other content for visible cells.

When this method is called in an animation block defined by the [- beginUpdates](<beginupdates().md>) and [- endUpdates](<endupdates().md>) methods, `UITableView` defers any insertions of rows or sections until after it has handled the deletions of rows or sections. This order is followed regardless of how the insertion and deletion method calls are ordered. This is unlike inserting or removing an item in a mutable array, in which the operation can affect the array index used for the successive insertion or removal operation. For more on this subject, see [Batch Insertion, Deletion, and Reloading of Rows and Sections](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/ManageInsertDeleteRow/ManageInsertDeleteRow.html#//apple_ref/doc/uid/TP40007451-CH10-SW9) in [Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451).

## See Also

### Related Documentation

- [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>) — Reloads the specified rows using the provided animation effect.

### Inserting, deleting, and moving rows and sections

- [- deleteRowsAtIndexPaths:withRowAnimation:](<deleterows(at_with_).md>) — Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [- insertSections:withRowAnimation:](<insertsections(__with_).md>) — Inserts one or more sections in the table view, with an option to animate the insertion.
- [- deleteSections:withRowAnimation:](<deletesections(__with_).md>) — Deletes one or more sections in the table view, with an option to animate the deletion.
- [RowAnimation](rowanimation.md) — The type of animation to use when inserting or deleting rows.
- [- moveRowAtIndexPath:toIndexPath:](<moverow(at_to_).md>) — Moves the row at a specified location to a destination location.
- [- moveSection:toSection:](<movesection(__tosection_).md>) — Moves a section to a new location in the table view.
