---
title: showingDeleteConfirmation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/showingdeleteconfirmation
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/showingdeleteconfirmation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/showingdeleteconfirmation.json'
content_hash: 'sha256:2045d2536f69632a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# showingDeleteConfirmation

<sub>Instance Property</sub>

A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var showingDeleteConfirmation: Bool { get }
```

## Discussion

When users tap the deletion control (the red circle to the left of the cell), the cell displays a “Delete” button on the right side of the cell; this string is localized.

## See Also

### Editing the cell

- [editing](isediting.md) — A Boolean value that indicates whether the cell is in an editable state.
- [- setEditing:animated:](<setediting(__animated_).md>) — Toggles the cell into and out of editing mode.
- [editingStyle](editingstyle-swift.property.md) — The editing style of the cell.
- [EditingStyle](editingstyle-swift.enum.md) — The editing control used by a cell.
- [showsReorderControl](showsreordercontrol.md) — A Boolean value that determines whether the cell shows the reordering control.
