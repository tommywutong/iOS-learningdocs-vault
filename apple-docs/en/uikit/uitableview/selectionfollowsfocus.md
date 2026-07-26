---
title: selectionFollowsFocus
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/selectionfollowsfocus
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/selectionfollowsfocus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/selectionfollowsfocus.json'
content_hash: 'sha256:c25e5432f023158d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# selectionFollowsFocus

<sub>Instance Property</sub>

A Boolean value that triggers an automatic selection when focus moves to a cell.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var selectionFollowsFocus: Bool { get set }
```

## Discussion

The system determines the default value of this property according to the platform and other properties of the table view.

## See Also

### Selecting rows

- [indexPathForSelectedRow](indexpathforselectedrow.md) — An index path that identifies the row and section of the selected row.
- [indexPathsForSelectedRows](indexpathsforselectedrows.md) — The index paths that represent the selected rows.
- [- selectRowAtIndexPath:animated:scrollPosition:](<selectrow(at_animated_scrollposition_).md>) — Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.
- [- deselectRowAtIndexPath:animated:](<deselectrow(at_animated_).md>) — Deselects a row that an index path identifies, with an option to animate the deselection.
- [allowsSelection](allowsselection.md) — A Boolean value that determines whether users can select a row.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether users can select more than one row outside of editing mode.
- [allowsSelectionDuringEditing](allowsselectionduringediting.md) — A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [allowsMultipleSelectionDuringEditing](allowsmultipleselectionduringediting.md) — A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [UITableViewSelectionDidChangeNotification](selectiondidchangenotification.md) — A notification that posts when the selected row in the posting table view changes.
