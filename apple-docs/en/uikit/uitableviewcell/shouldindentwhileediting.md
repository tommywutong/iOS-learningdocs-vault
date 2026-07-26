---
title: shouldIndentWhileEditing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/shouldindentwhileediting
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/shouldindentwhileediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/shouldindentwhileediting.json'
content_hash: 'sha256:3aa3f61512afb720'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# shouldIndentWhileEditing

<sub>Instance Property</sub>

A Boolean value that controls whether the cell background is indented when the table view is in editing mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shouldIndentWhileEditing: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md). This property is unrelated to [indentationLevel](indentationlevel.md). The delegate can override this value in [- tableView:shouldIndentWhileEditingRowAtIndexPath:](<../uitableviewdelegate/tableview(__shouldindentwhileeditingrowat_).md>). This property has an effect only on table views created in the grouped style ([UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md)); it has no effect on [UITableViewStylePlain](../uitableview/style-swift.enum/plain.md) table views.

## See Also

### Managing content indentation

- [indentationLevel](indentationlevel.md) — The indentation level of the cell’s content.
- [indentationWidth](indentationwidth.md) — The width for each level of indentation of a cell’s content.
- [separatorInset](separatorinset.md) — The inset values for the separator line drawn beneath the cell.
- [SeparatorStyle](separatorstyle.md) — The style for cells to use as separators.
