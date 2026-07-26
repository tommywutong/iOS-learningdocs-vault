---
title: 'moveSection(_:toSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/movesection(_:tosection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/movesection(_:tosection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/movesection%28_%3Atosection%3A%29.json'
content_hash: 'sha256:11d711ebfa05c841'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# moveSection(_:toSection:)

<sub>Instance Method</sub>

Moves a section to a new location in the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func moveSection(_ section: Int, toSection newSection: Int)
```

## Parameters

- `section` — The index of the section to move.

- `newSection` — The index in the table view that’s the destination of the move for the section. The existing section at that location slides up or down to an adjoining index position to make room for it.

## Discussion

You can combine section-move operations with section-insertion and section-deletion operations within a [- beginUpdates](<beginupdates().md>)–[- endUpdates](<endupdates().md>) block to have all changes occur together as a single animation.

Unlike the section-insertion section row-deletion methods, this method doesn’t take an animation parameter. For sections that are moved, the moved section animates straight from the starting position to the ending position. Also unlike the other methods, this method allows only one section to be moved per call. If you want multiple section moved, call this method repeatedly within a [- beginUpdates](<beginupdates().md>)–[- endUpdates](<endupdates().md>) block.

## See Also

### Inserting, deleting, and moving rows and sections

- [- insertRowsAtIndexPaths:withRowAnimation:](<insertrows(at_with_).md>) — Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [- deleteRowsAtIndexPaths:withRowAnimation:](<deleterows(at_with_).md>) — Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [- insertSections:withRowAnimation:](<insertsections(__with_).md>) — Inserts one or more sections in the table view, with an option to animate the insertion.
- [- deleteSections:withRowAnimation:](<deletesections(__with_).md>) — Deletes one or more sections in the table view, with an option to animate the deletion.
- [RowAnimation](rowanimation.md) — The type of animation to use when inserting or deleting rows.
- [- moveRowAtIndexPath:toIndexPath:](<moverow(at_to_).md>) — Moves the row at a specified location to a destination location.
