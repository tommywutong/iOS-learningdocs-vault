---
title: 'insertSections(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/insertsections(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/insertsections(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/insertsections%28_%3Awith%3A%29.json'
content_hash: 'sha256:95913209e488b375'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# insertSections(_:with:)

<sub>Instance Method</sub>

Inserts one or more sections in the table view, with an option to animate the insertion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertSections(_ sections: IndexSet, with animation: UITableView.RowAnimation)
```

## Parameters

- `sections` — An index set that specifies the sections to insert in the table view. If a section already exists at the specified index location, it is moved down one index location.

- `animation` — A constant that indicates how the insertion is to be animated, for example, fade in or slide in from the left. See [RowAnimation](rowanimation.md) for descriptions of these constants.

## Discussion

`UITableView` calls the relevant delegate and data source methods immediately afterward to get the cells and other content for visible cells.

When this method is called in an animation block defined by the [- beginUpdates](<beginupdates().md>) and [- endUpdates](<endupdates().md>) methods, `UITableView` defers any insertions of rows or sections until after it has handled the deletions of rows or sections. This order is followed regardless of how the insertion and deletion method calls are ordered. This is unlike inserting or removing an item in a mutable array, in which the operation can affect the array index used for the successive insertion or removal operation. For more on this subject, see [Batch Insertion, Deletion, and Reloading of Rows and Sections](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/ManageInsertDeleteRow/ManageInsertDeleteRow.html#//apple_ref/doc/uid/TP40007451-CH10-SW9) in [Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451).

## See Also

### Related Documentation

- [- reloadSections:withRowAnimation:](<reloadsections(__with_).md>) — Reloads the specified sections using the provided animation effect.

### Inserting, deleting, and moving rows and sections

- [- insertRowsAtIndexPaths:withRowAnimation:](<insertrows(at_with_).md>) — Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [- deleteRowsAtIndexPaths:withRowAnimation:](<deleterows(at_with_).md>) — Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [- deleteSections:withRowAnimation:](<deletesections(__with_).md>) — Deletes one or more sections in the table view, with an option to animate the deletion.
- [RowAnimation](rowanimation.md) — The type of animation to use when inserting or deleting rows.
- [- moveRowAtIndexPath:toIndexPath:](<moverow(at_to_).md>) — Moves the row at a specified location to a destination location.
- [- moveSection:toSection:](<movesection(__tosection_).md>) — Moves a section to a new location in the table view.
