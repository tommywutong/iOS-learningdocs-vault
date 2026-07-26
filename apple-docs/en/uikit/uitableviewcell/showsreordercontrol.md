---
title: showsReorderControl
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/showsreordercontrol
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/showsreordercontrol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/showsreordercontrol.json'
content_hash: 'sha256:bc4704a2f30a889a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# showsReorderControl

<sub>Instance Property</sub>

A Boolean value that determines whether the cell shows the reordering control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var showsReorderControl: Bool { get set }
```

## Discussion

The reordering control is gray, multiple horizontal bar control on the right side of the cell. Users can drag this control to reorder the cell within the table. The default value is [false](../../swift/false.md). If the value is [true](../../swift/true.md) , the reordering control temporarily replaces any accessory view.

For the reordering control to appear, you must not only set this property but implement the [UITableViewDataSource](../uitableviewdatasource.md) method [- tableView:moveRowAtIndexPath:toIndexPath:](<../uitableviewdatasource/tableview(__moverowat_to_).md>). In addition, if the data source implements [- tableView:canMoveRowAtIndexPath:](<../uitableviewdatasource/tableview(__canmoverowat_).md>) to return [false](../../swift/false.md), the reordering control doesn’t appear in that designated row.

## See Also

### Editing the cell

- [editing](isediting.md) — A Boolean value that indicates whether the cell is in an editable state.
- [- setEditing:animated:](<setediting(__animated_).md>) — Toggles the cell into and out of editing mode.
- [editingStyle](editingstyle-swift.property.md) — The editing style of the cell.
- [EditingStyle](editingstyle-swift.enum.md) — The editing control used by a cell.
- [showingDeleteConfirmation](showingdeleteconfirmation.md) — A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
