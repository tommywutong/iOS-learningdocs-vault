---
title: 'moveRow(at:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/moverow(at:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/moverow(at:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/moverow%28at%3Ato%3A%29.json'
content_hash: 'sha256:fb53ec80f4790c38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# moveRow(at:to:)

<sub>Instance Method</sub>

Moves the row at a specified location to a destination location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func moveRow(at indexPath: IndexPath, to newIndexPath: IndexPath)
```

## Parameters

- `indexPath` — An index path identifying the row to move.

- `newIndexPath` — An index path identifying the row that’s the destination of the row at `indexPath`. The existing row at that location slides up or down to an adjoining index position to make room for it.

## Discussion

You can combine row-move operations with row-insertion and row-deletion operations within a [- beginUpdates](<beginupdates().md>)–[- endUpdates](<endupdates().md>) block to have all changes occur together as a single animation.

Unlike the row-insertion and row-deletion methods, this method doesn’t take an `animation` parameter. For rows that are moved, the moved row animates straight from the starting position to the ending position. Also unlike the other methods, this method allows only one row to be moved per call. If you want multiple rows moved, you can call this method repeatedly within a [- beginUpdates](<beginupdates().md>)–[- endUpdates](<endupdates().md>) block.

## See Also

### Related Documentation

- [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>) — Reloads the specified rows using the provided animation effect.

### Inserting, deleting, and moving rows and sections

- [- insertRowsAtIndexPaths:withRowAnimation:](<insertrows(at_with_).md>) — Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [- deleteRowsAtIndexPaths:withRowAnimation:](<deleterows(at_with_).md>) — Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [- insertSections:withRowAnimation:](<insertsections(__with_).md>) — Inserts one or more sections in the table view, with an option to animate the insertion.
- [- deleteSections:withRowAnimation:](<deletesections(__with_).md>) — Deletes one or more sections in the table view, with an option to animate the deletion.
- [RowAnimation](rowanimation.md) — The type of animation to use when inserting or deleting rows.
- [- moveSection:toSection:](<movesection(__tosection_).md>) — Moves a section to a new location in the table view.
