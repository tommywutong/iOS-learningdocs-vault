---
title: editingAccessoryView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/editingaccessoryview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/editingaccessoryview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/editingaccessoryview.json'
content_hash: 'sha256:1fc15830b7e79000'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# editingAccessoryView

<sub>Instance Property</sub>

The view to use on the right side of the cell, typically as a control, in the table view’s editing state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var editingAccessoryView: UIView? { get set }
```

## Discussion

If the value of this property is not `nil`, the `UITableViewCell` class uses the given view for the accessory view in the table view’s editing state; it ignores the value of the [editingAccessoryType](editingaccessorytype.md) property. The provided accessory view can be a framework-provided control or label or a custom view. The accessory view appears in the right side of the cell.

The accessory type cross-fades between normal and editing states if it set for both states; use the [accessoryType](accessorytype-swift.property.md) property to set the accessory view for the cell during the table view’s normal state. If this property is not set for both states, the cell is animated to slide or out, as necessary.

## See Also

### Related Documentation

- [- willTransitionToState:](<willtransition(to_).md>) — Notifies the cell that it’s about to transition to a new cell state.
- [- didTransitionToState:](<didtransition(to_).md>) — Notifies the cell that it transitioned to a new cell state.

### Managing accessory views

- [accessoryType](accessorytype-swift.property.md) — The type of standard accessory view for the cell to use in the table view’s normal state.
- [accessoryView](accessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [editingAccessoryType](editingaccessorytype.md) — The type of standard accessory view for the cell to use in the table view’s editing state.
- [AccessoryType](accessorytype-swift.enum.md) — The type of standard accessory control used by a cell.
