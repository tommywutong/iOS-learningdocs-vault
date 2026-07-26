---
title: UITableView.RowAnimation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/rowanimation
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/rowanimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/rowanimation.json'
content_hash: 'sha256:0060bb5617f409ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# UITableView.RowAnimation

<sub>Enumeration</sub>

The type of animation to use when inserting or deleting rows.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum RowAnimation
```

## Overview

You specify one of these constants as a parameter of the [- insertRowsAtIndexPaths:withRowAnimation:](<insertrows(at_with_).md>), [- insertSections:withRowAnimation:](<insertsections(__with_).md>), [- deleteRowsAtIndexPaths:withRowAnimation:](<deleterows(at_with_).md>),[- deleteSections:withRowAnimation:](<deletesections(__with_).md>), [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>), and [- reloadSections:withRowAnimation:](<reloadsections(__with_).md>) methods.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITableViewRowAnimationFade](rowanimation/fade.md) — The inserted or deleted row or rows fade into or out of the table view.
- [UITableViewRowAnimationRight](rowanimation/right.md) — The inserted row or rows slide in from the right; the deleted row or rows slide out to the right.
- [UITableViewRowAnimationLeft](rowanimation/left.md) — The inserted row or rows slide in from the left; the deleted row or rows slide out to the left.
- [UITableViewRowAnimationTop](rowanimation/top.md) — The inserted row or rows slide in from the top; the deleted row or rows slide out toward the top.
- [UITableViewRowAnimationBottom](rowanimation/bottom.md) — The inserted row or rows slide in from the bottom; the deleted row or rows slide out toward the bottom.
- [UITableViewRowAnimationNone](rowanimation/none.md) — The inserted or deleted rows use the default animations.
- [UITableViewRowAnimationMiddle](rowanimation/middle.md) — The table view attempts to keep the old and new cells centered in the space they did or will occupy.
- [UITableViewRowAnimationAutomatic](rowanimation/automatic.md) — The table view chooses an appropriate animation style for you.

### Initializers

- [init(rawValue:)](<rowanimation/init(rawvalue_).md>)

## See Also

### Inserting, deleting, and moving rows and sections

- [- insertRowsAtIndexPaths:withRowAnimation:](<insertrows(at_with_).md>) — Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [- deleteRowsAtIndexPaths:withRowAnimation:](<deleterows(at_with_).md>) — Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [- insertSections:withRowAnimation:](<insertsections(__with_).md>) — Inserts one or more sections in the table view, with an option to animate the insertion.
- [- deleteSections:withRowAnimation:](<deletesections(__with_).md>) — Deletes one or more sections in the table view, with an option to animate the deletion.
- [- moveRowAtIndexPath:toIndexPath:](<moverow(at_to_).md>) — Moves the row at a specified location to a destination location.
- [- moveSection:toSection:](<movesection(__tosection_).md>) — Moves a section to a new location in the table view.
