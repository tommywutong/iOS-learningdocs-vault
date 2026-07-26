---
title: allowsMultipleSelectionDuringEditing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/allowsmultipleselectionduringediting
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/allowsmultipleselectionduringediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/allowsmultipleselectionduringediting.json'
content_hash: 'sha256:38ac39cb1426ac03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# allowsMultipleSelectionDuringEditing

<sub>Instance Property</sub>

A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsMultipleSelectionDuringEditing: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). If you set it to [true](../../swift/true.md), check marks appear next to selected rows in editing mode. In addition, [UITableView](../uitableview.md) doesn’t query for editing styles when it goes into editing mode. If you access [indexPathsForSelectedRows](indexpathsforselectedrows.md), you can get the index paths that identify the selected rows.

## See Also

### Selecting rows

- [indexPathForSelectedRow](indexpathforselectedrow.md) — An index path that identifies the row and section of the selected row.
- [indexPathsForSelectedRows](indexpathsforselectedrows.md) — The index paths that represent the selected rows.
- [- selectRowAtIndexPath:animated:scrollPosition:](<selectrow(at_animated_scrollposition_).md>) — Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.
- [- deselectRowAtIndexPath:animated:](<deselectrow(at_animated_).md>) — Deselects a row that an index path identifies, with an option to animate the deselection.
- [allowsSelection](allowsselection.md) — A Boolean value that determines whether users can select a row.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether users can select more than one row outside of editing mode.
- [allowsSelectionDuringEditing](allowsselectionduringediting.md) — A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
- [UITableViewSelectionDidChangeNotification](selectiondidchangenotification.md) — A notification that posts when the selected row in the posting table view changes.
