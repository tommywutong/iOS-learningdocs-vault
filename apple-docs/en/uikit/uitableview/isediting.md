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
doc_path: /documentation/uikit/uitableview/isediting
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/isediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/isediting.json'
content_hash: 'sha256:a566dc0ca25f1c69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# isEditing

<sub>Instance Property</sub>

A Boolean value that determines whether the table view is in editing mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEditing: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the table view is in editing mode: The cells of the table might show an insertion or deletion control on the left side of each cell and a reordering control on the right side, depending on how the cell is configured. (See [UITableViewCell](../uitableviewcell.md) for details.) Tapping a control causes the table view to invoke the data source method [- tableView:commitEditingStyle:forRowAtIndexPath:](<../uitableviewdatasource/tableview(__commit_forrowat_).md>). The default value is [false](../../swift/false.md).

## See Also

### Putting the table into edit mode

- [- setEditing:animated:](<setediting(__animated_).md>) — Toggles the table view into and out of editing mode.
