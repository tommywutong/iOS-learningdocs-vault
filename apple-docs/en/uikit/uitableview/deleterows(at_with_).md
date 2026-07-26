---
title: 'deleteRows(at:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/deleterows(at:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/deleterows(at:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/deleterows%28at%3Awith%3A%29.json'
content_hash: 'sha256:85d74c04f1346258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# deleteRows(at:with:)

<sub>Instance Method</sub>

Deletes the rows that an array of index paths identifies, with an option to animate the deletion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func deleteRows(at indexPaths: [IndexPath], with animation: UITableView.RowAnimation)
```

## Parameters

- `indexPaths` — An array of [NSIndexPath](../../foundation/nsindexpath.md) objects identifying the rows to delete.

- `animation` — A constant that indicates how the deletion is to be animated, for example, fade out or slide out from the bottom. See [RowAnimation](rowanimation.md) for descriptions of these constants.

## Discussion

When this method is called in an animation block defined by the [- beginUpdates](<beginupdates().md>) and [- endUpdates](<endupdates().md>) methods, `UITableView` defers any insertions of rows or sections until after it has handled the deletions of rows or sections. This order is followed regardless how the insertion and deletion method calls are ordered. This is unlike inserting or removing an item in a mutable array, in which the operation can affect the array index used for the successive insertion or removal operation. For more on this subject, see [Batch Insertion, Deletion, and Reloading of Rows and Sections](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/ManageInsertDeleteRow/ManageInsertDeleteRow.html#//apple_ref/doc/uid/TP40007451-CH10-SW9) in [Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451).

## See Also

### Related Documentation

- [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>) — Reloads the specified rows using the provided animation effect.

### Inserting, deleting, and moving rows and sections

- [- insertRowsAtIndexPaths:withRowAnimation:](<insertrows(at_with_).md>) — Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [- insertSections:withRowAnimation:](<insertsections(__with_).md>) — Inserts one or more sections in the table view, with an option to animate the insertion.
- [- deleteSections:withRowAnimation:](<deletesections(__with_).md>) — Deletes one or more sections in the table view, with an option to animate the deletion.
- [RowAnimation](rowanimation.md) — The type of animation to use when inserting or deleting rows.
- [- moveRowAtIndexPath:toIndexPath:](<moverow(at_to_).md>) — Moves the row at a specified location to a destination location.
- [- moveSection:toSection:](<movesection(__tosection_).md>) — Moves a section to a new location in the table view.
