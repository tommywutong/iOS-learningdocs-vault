---
title: accessoryType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/accessorytype-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/accessorytype-swift.property.json'
content_hash: 'sha256:6a250ca595d1102f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# accessoryType

<sub>Instance Property</sub>

The type of standard accessory view for the cell to use in the table view’s normal state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var accessoryType: UITableViewCell.AccessoryType { get set }
```

## Discussion

The accessory view appears in the right side of the cell in the table view’s normal (default) state. The standard accessory views include the disclosure chevron; for a description of valid [accessoryType](accessorytype-swift.property.md) constants, see [AccessoryType](accessorytype-swift.enum.md). The default is [UITableViewCellAccessoryNone](accessorytype-swift.enum/none.md). If a custom accessory view is set through the [accessoryView](accessoryview.md) property, the value of this property is ignored. If the cell is enabled and the accessory type is [UITableViewCellAccessoryDetailDisclosureButton](accessorytype-swift.enum/detaildisclosurebutton.md), the accessory view tracks touches and, when tapped, sends the data-source object a [- tableView:accessoryButtonTappedForRowWithIndexPath:](<../uitableviewdelegate/tableview(__accessorybuttontappedforrowwith_).md>) message.

The accessory-type image cross-fades between normal and editing states if it set for both states; use the [editingAccessoryType](editingaccessorytype.md) property to set the accessory type for the cell during editing mode. If this property is not set for both states, the cell is animated to slide in or out, as necessary.

## See Also

### Related Documentation

- [- willTransitionToState:](<willtransition(to_).md>) — Notifies the cell that it’s about to transition to a new cell state.
- [- didTransitionToState:](<didtransition(to_).md>) — Notifies the cell that it transitioned to a new cell state.

### Managing accessory views

- [accessoryView](accessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [editingAccessoryType](editingaccessorytype.md) — The type of standard accessory view for the cell to use in the table view’s editing state.
- [editingAccessoryView](editingaccessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s editing state.
- [AccessoryType](accessorytype-swift.enum.md) — The type of standard accessory control used by a cell.
