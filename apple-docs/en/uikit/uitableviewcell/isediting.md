---
title: isEditing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/isediting
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/isediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/isediting.json'
content_hash: 'sha256:2a301465f46164ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# isEditing

<sub>Instance Property</sub>

A Boolean value that indicates whether the cell is in an editable state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEditing: Bool { get set }
```

## Discussion

When a cell is in an editable state, it displays the editing controls specified for it: the green insertion control, the red deletion control, or (on the right side) the reordering control. Use [editingStyle](editingstyle-swift.property.md) and [showsReorderControl](showsreordercontrol.md) to specify these controls for the cell.

## See Also

### Editing the cell

- [- setEditing:animated:](<setediting(__animated_).md>) — Toggles the cell into and out of editing mode.
- [editingStyle](editingstyle-swift.property.md) — The editing style of the cell.
- [EditingStyle](editingstyle-swift.enum.md) — The editing control used by a cell.
- [showingDeleteConfirmation](showingdeleteconfirmation.md) — A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [showsReorderControl](showsreordercontrol.md) — A Boolean value that determines whether the cell shows the reordering control.
