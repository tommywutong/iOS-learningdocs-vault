---
title: separatorStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/separatorstyle
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/separatorstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/separatorstyle.json'
content_hash: 'sha256:f11937f0d21a63fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# separatorStyle

<sub>Instance Property</sub>

The style for table cells to use as separators.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var separatorStyle: UITableViewCell.SeparatorStyle { get set }
```

## Discussion

The value of this property is one of the separator-style constants described in [UITableViewCell](../uitableviewcell.md). `UITableView` uses this property to set the separator style on the cell returned from the delegate in [- tableView:cellForRowAtIndexPath:](<../uitableviewdatasource/tableview(__cellforrowat_).md>).

## See Also

### Customizing the separator appearance

- [SeparatorStyle](../uitableviewcell/separatorstyle.md) — The style for cells to use as separators.
- [separatorColor](separatorcolor.md) — The color of separator rows in the table view.
- [separatorEffect](separatoreffect.md) — The effect to apply to table separators.
- [separatorInset](separatorinset.md) — The default inset of cell separators.
- [separatorInsetReference](separatorinsetreference-swift.property.md) — An indicator of how to interpret the separator inset value.
- [SeparatorInsetReference](separatorinsetreference-swift.enum.md) — Constants that indicate how to interpret the separator inset value of a table view.
