---
title: editingAccessoryType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/editingaccessorytype
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/editingaccessorytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/editingaccessorytype.json'
content_hash: 'sha256:e945bf8ba452f688'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# editingAccessoryType

<sub>Instance Property</sub>

The type of standard accessory view for the cell to use in the table view’s editing state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var editingAccessoryType: UITableViewCell.AccessoryType { get set }
```

## Discussion

The accessory view appears in the right side of the cell when the table view is in editing mode. The standard accessory views include the disclosure chevron; for a description of valid constants, see [AccessoryType](accessorytype-swift.enum.md). The default is [UITableViewCellAccessoryNone](accessorytype-swift.enum/none.md). If a custom accessory view for editing mode is set through the [editingAccessoryView](editingaccessoryview.md) property, the value of this property is ignored. If the cell is enabled and the accessory type is [UITableViewCellAccessoryDetailDisclosureButton](accessorytype-swift.enum/detaildisclosurebutton.md), the accessory view tracks touches and, when tapped, sends the delegate object a [- tableView:accessoryButtonTappedForRowWithIndexPath:](<../uitableviewdelegate/tableview(__accessorybuttontappedforrowwith_).md>) message.

The accessory type cross-fades between normal and editing states if it set for both states; use the [accessoryType](accessorytype-swift.property.md) property to set the accessory view for the cell during the table view’s normal state. If this property is not set for both states, the cell is animated to slide or out, as necessary.

## See Also

### Related Documentation

- [- willTransitionToState:](<willtransition(to_).md>) — Notifies the cell that it’s about to transition to a new cell state.
- [- didTransitionToState:](<didtransition(to_).md>) — Notifies the cell that it transitioned to a new cell state.

### Managing accessory views

- [accessoryType](accessorytype-swift.property.md) — The type of standard accessory view for the cell to use in the table view’s normal state.
- [accessoryView](accessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [editingAccessoryView](editingaccessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s editing state.
- [AccessoryType](accessorytype-swift.enum.md) — The type of standard accessory control used by a cell.
