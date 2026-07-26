---
title: indexPathForSelectedRow
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/indexpathforselectedrow
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/indexpathforselectedrow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/indexpathforselectedrow.json'
content_hash: 'sha256:80ccbe13534606c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# indexPathForSelectedRow

<sub>Instance Property</sub>

An index path that identifies the row and section of the selected row.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indexPathForSelectedRow: IndexPath? { get }
```

## Discussion

The value of this property is an index path identifying the row and section indexes of the selected row, or `nil` if the index path is invalid. If there are multiple selections, this property contains the first index-path object in the array of row selections; this object has the lowest index values for section and row.

## See Also

### Selecting rows

- [indexPathsForSelectedRows](indexpathsforselectedrows.md) — The index paths that represent the selected rows.
- [- selectRowAtIndexPath:animated:scrollPosition:](<selectrow(at_animated_scrollposition_).md>) — Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.
- [- deselectRowAtIndexPath:animated:](<deselectrow(at_animated_).md>) — Deselects a row that an index path identifies, with an option to animate the deselection.
- [allowsSelection](allowsselection.md) — A Boolean value that determines whether users can select a row.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether users can select more than one row outside of editing mode.
- [allowsSelectionDuringEditing](allowsselectionduringediting.md) — A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [allowsMultipleSelectionDuringEditing](allowsmultipleselectionduringediting.md) — A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
- [UITableViewSelectionDidChangeNotification](selectiondidchangenotification.md) — A notification that posts when the selected row in the posting table view changes.
