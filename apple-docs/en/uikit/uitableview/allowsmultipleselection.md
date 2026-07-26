---
title: allowsMultipleSelection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/allowsmultipleselection
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/allowsmultipleselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/allowsmultipleselection.json'
content_hash: 'sha256:33d5a419f753cc94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# allowsMultipleSelection

<sub>Instance Property</sub>

A Boolean value that determines whether users can select more than one row outside of editing mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsMultipleSelection: Bool { get set }
```

## Discussion

This property controls whether a user can select multiple rows simultaneously outside of editing mode. Selected rows acquire a selected appearance.

In iOS, when the value of this property is [true](../../swift/true.md), the user can select additional rows by tapping on them. The user must tap a currently selected row to deselect it.

In macOS, when the value of this property is [true](../../swift/true.md), the user can select additional rows by holding the Command or Shift key while clicking on the additional rows they want to select. If the user isn’t holding a modifier key, clicking on another row clears the current selection and selects only the clicked row. This behavior resembles the selection behavior of [NSTableView](../../appkit/nstableview.md).

If you access [indexPathsForSelectedRows](indexpathsforselectedrows.md), you can get the index paths that identify the selected rows.

The default value of this property is [false](../../swift/false.md).

## See Also

### Selecting rows

- [indexPathForSelectedRow](indexpathforselectedrow.md) — An index path that identifies the row and section of the selected row.
- [indexPathsForSelectedRows](indexpathsforselectedrows.md) — The index paths that represent the selected rows.
- [- selectRowAtIndexPath:animated:scrollPosition:](<selectrow(at_animated_scrollposition_).md>) — Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.
- [- deselectRowAtIndexPath:animated:](<deselectrow(at_animated_).md>) — Deselects a row that an index path identifies, with an option to animate the deselection.
- [allowsSelection](allowsselection.md) — A Boolean value that determines whether users can select a row.
- [allowsSelectionDuringEditing](allowsselectionduringediting.md) — A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [allowsMultipleSelectionDuringEditing](allowsmultipleselectionduringediting.md) — A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
- [UITableViewSelectionDidChangeNotification](selectiondidchangenotification.md) — A notification that posts when the selected row in the posting table view changes.
