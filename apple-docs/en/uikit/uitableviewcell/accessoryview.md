---
title: accessoryView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/accessoryview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/accessoryview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/accessoryview.json'
content_hash: 'sha256:053e2a3e1aa1811f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# accessoryView

<sub>Instance Property</sub>

The view to use on the right side of the cell, typically as a control, in the table view’s normal state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var accessoryView: UIView? { get set }
```

## Discussion

If the value of this property is not `nil`, the `UITableViewCell` class uses the given view for the accessory view in the table view’s normal (default) state; it ignores the value of the [accessoryType](accessorytype-swift.property.md) property. The provided accessory view can be a framework-provided control or label or a custom view. The accessory view appears in the right side of the cell.

The accessory view cross-fades between normal and editing states if it set for both states; use the [editingAccessoryView](editingaccessoryview.md) property to set the accessory view for the cell during editing mode. If this property is not set for both states, the cell is animated to slide in or out, as necessary.

## See Also

### Related Documentation

- [- willTransitionToState:](<willtransition(to_).md>) — Notifies the cell that it’s about to transition to a new cell state.
- [- didTransitionToState:](<didtransition(to_).md>) — Notifies the cell that it transitioned to a new cell state.

### Managing accessory views

- [accessoryType](accessorytype-swift.property.md) — The type of standard accessory view for the cell to use in the table view’s normal state.
- [editingAccessoryType](editingaccessorytype.md) — The type of standard accessory view for the cell to use in the table view’s editing state.
- [editingAccessoryView](editingaccessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s editing state.
- [AccessoryType](accessorytype-swift.enum.md) — The type of standard accessory control used by a cell.
