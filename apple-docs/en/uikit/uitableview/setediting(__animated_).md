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
doc_path: '/documentation/uikit/uitableview/setediting(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/setediting(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/setediting%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:8aa84f5bdb9ad5e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# setEditing(_:animated:)

<sub>Instance Method</sub>

Toggles the table view into and out of editing mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setEditing(_ editing: Bool, animated: Bool)
```

## Parameters

- `editing` — [true](../../swift/true.md) to enter editing mode; [false](../../swift/false.md) to leave it. The default value is [false](../../swift/false.md).

- `animated` — [true](../../swift/true.md) to animate the transition to editing mode; [false](../../swift/false.md) to make the transition immediate.

## Discussion

When you call this method with the value of `editing` set to [true](../../swift/true.md), the table view goes into editing mode by calling [- setEditing:animated:](<../uitableviewcell/setediting(__animated_).md>) on each visible `UITableViewCell` object. Calling this method with `editing` set to [false](../../swift/false.md) turns off editing mode. In editing mode, the cells of the table might show an insertion or deletion control on the left side of each cell and a reordering control on the right side, depending on how the cell is configured. (See [UITableViewCell](../uitableviewcell.md) for details.) The data source of the table view can selectively exclude cells from editing mode by implementing [- tableView:canEditRowAtIndexPath:](<../uitableviewdatasource/tableview(__caneditrowat_).md>).

## See Also

### Putting the table into edit mode

- [editing](isediting.md) — A Boolean value that determines whether the table view is in editing mode.
