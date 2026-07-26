---
title: editingStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/editingstyle-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/editingstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/editingstyle-swift.property.json'
content_hash: 'sha256:6a930399e916f576'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# editingStyle

<sub>Instance Property</sub>

The editing style of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var editingStyle: UITableViewCell.EditingStyle { get }
```

## Discussion

One of the constants described in [EditingStyle](editingstyle-swift.enum.md) is used as the value of this property; it specifies whether the cell is in an editable state and, if it is, whether it shows an insertion or deletion control. The default value is [UITableViewCellEditingStyleNone](editingstyle-swift.enum/none.md) (not editable). The delegate returns the value of this property for a particular cell in its implementation of the [- tableView:editingStyleForRowAtIndexPath:](<../uitableviewdelegate/tableview(__editingstyleforrowat_).md>) method.

## See Also

### Editing the cell

- [editing](isediting.md) — A Boolean value that indicates whether the cell is in an editable state.
- [- setEditing:animated:](<setediting(__animated_).md>) — Toggles the cell into and out of editing mode.
- [EditingStyle](editingstyle-swift.enum.md) — The editing control used by a cell.
- [showingDeleteConfirmation](showingdeleteconfirmation.md) — A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [showsReorderControl](showsreordercontrol.md) — A Boolean value that determines whether the cell shows the reordering control.
