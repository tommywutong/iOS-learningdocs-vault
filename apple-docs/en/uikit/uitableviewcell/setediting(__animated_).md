---
title: 'setEditing(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewcell/setediting(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/setediting(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/setediting%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:f3cfee1fb092aa7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# setEditing(_:animated:)

<sub>Instance Method</sub>

Toggles the cell into and out of editing mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setEditing(_ editing: Bool, animated: Bool)
```

## Parameters

- `editing` — [true](../../swift/true.md) to enter editing mode, [false](../../swift/false.md) to leave it. The default value is [false](../../swift/false.md).

- `animated` — [true](../../swift/true.md) to animate the appearance or disappearance of the insertion/deletion control and the reordering control, [false](../../swift/false.md) to make the transition immediate.

## Discussion

When you call this method with the value of `editing` set to [true](../../swift/true.md), and the `UITableViewCell` object is configured to have controls, the cell shows an insertion (green plus) or deletion control (red minus) on the left side of each cell and a reordering control on the right side. This method is called on each visible cell when the [- setEditing:animated:](<../uitableview/setediting(__animated_).md>) method of `UITableView` is invoked. Calling this method with `editing` set to [false](../../swift/false.md) removes the controls from the cell.

## See Also

### Editing the cell

- [editing](isediting.md) — A Boolean value that indicates whether the cell is in an editable state.
- [editingStyle](editingstyle-swift.property.md) — The editing style of the cell.
- [EditingStyle](editingstyle-swift.enum.md) — The editing control used by a cell.
- [showingDeleteConfirmation](showingdeleteconfirmation.md) — A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [showsReorderControl](showsreordercontrol.md) — A Boolean value that determines whether the cell shows the reordering control.
